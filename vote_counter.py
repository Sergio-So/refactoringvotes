import csv
from collections import defaultdict

def count_votes(file_path):
    # Usamos defaultdict para inicializar automáticamente valores en 0 al agregar un nuevo candidato.
    # Esto simplifica el código al no necesitar verificar si el candidato ya existe en el diccionario.
    results = defaultdict(int)
    
    # Abrimos el archivo CSV usando 'DictReader' para mejorar la legibilidad del código.
    # 'DictReader' permite acceder a las columnas del archivo por nombre en lugar de índices.
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            candidate = row["candidate"]
            try:
                # Intentamos convertir los votos a un número entero.
                # Este manejo de errores específico con 'ValueError' permite ignorar los datos inválidos
                # en lugar de interrumpir la ejecución, mejorando la robustez del código.
                votes = int(row["votes"])
            except ValueError:
                # Si ocurre un error de conversión, imprimimos una advertencia y continuamos sin sumar votos inválidos.
                print(f"Advertencia: votos inválidos para {candidate} en {row['city']}")
                continue
            
            # Acumulamos los votos para cada candidato; defaultdict maneja la inicialización automática en 0.
            results[candidate] += votes

    # Iteramos sobre los resultados para imprimir el total de votos por candidato.
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votos")
    
    # Ordenamos los resultados por votos en orden descendente para identificar el candidato con más votos.
    # La función lambda 'key=lambda item: item[1]' permite ordenar basándonos en los votos.
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    
    # Verificación de empate: Comparamos el total de votos del primer y segundo candidato.
    # Si son iguales, imprimimos un mensaje de empate; de lo contrario, mostramos al ganador.
    if len(sorted_results) > 1 and sorted_results[0][1] == sorted_results[1][1]:
        print("Hay un empate entre los candidatos:")
        for candidate, votes in sorted_results:
            if votes == sorted_results[0][1]:
                print(f"{candidate} con {votes} votos")
    else:
        # Si no hay empate, imprimimos el ganador con el mayor número de votos.
        print(f"El ganador es {sorted_results[0][0]} con {sorted_results[0][1]} votos")
