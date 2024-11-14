# test_vote_counter.py

import unittest
from unittest.mock import patch, mock_open
from vote_counter import count_votes  # Assuming starter version is in `vote_counter.py`

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Expected output after tallying votes
        mock_print.assert_any_call("Alice: 3200 votes")
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simulate a CSV file with invalid votes data
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Expect Alice to be skipped due to invalid data, only Bob's votes should print correctly
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Alice: 2000 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)

        @patch("builtins.print")
    def test_count_votes_tie(self, mock_print):
        # Simulamos un archivo CSV con un empate entre dos candidatos
        mock_csv = """city,candidate,votes
        Springfield,Alice,1500
        Springfield,Bob,1500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        mock_print.assert_any_call("Alice: 1500 votos")
        mock_print.assert_any_call("Bob: 1500 votos")
        mock_print.assert_any_call("Hay un empate entre los candidatos:")
        mock_print.assert_any_call("Alice con 1500 votos")
        mock_print.assert_any_call("Bob con 1500 votos")
        self.assertEqual(mock_print.call_count, 5)

if __name__ == "__main__":
    unittest.main()

