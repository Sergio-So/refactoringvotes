import csv
from collections import defaultdict

def count_votes(file_path):
    results = defaultdict(int)
    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            candidate = row["candidate"]
            try:
                votes = int(row["votes"])
            except ValueError:
                print(f"Advertencia: votos inválidos para {candidate} en {row['city']}")
                continue
            
            results[candidate] += votes

    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votos")
    
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    
    if len(sorted_results) > 1 and sorted_results[0][1] == sorted_results[1][1]:
        print("Hay un empate entre los candidatos:")
        for candidate, votes in sorted_results:
            if votes == sorted_results[0][1]:
                print(f"{candidate} con {votes} votos")
    else:
        print(f"El ganador es {sorted_results[0][0]} con {sorted_results[0][1]} votos")
