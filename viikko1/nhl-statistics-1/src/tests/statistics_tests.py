import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_haku(self):
        search_result = self.statistics.search('Yzerman')
        self.assertEqual(search_result.name, 'Yzerman')
        self.assertEqual(search_result.team, 'DET')
        

    def test_top_pisteyttajat(self):
        top_scorers = self.statistics.top_scorers(5)
        self.assertEqual(top_scorers[0].name, 'Lemieux')
        self.assertEqual(top_scorers[-1].name, 'Kurri')
        
    def test_toimiiko_tiimihaku(self):
        team_result = self.statistics.team('EDM')
        self.assertEqual(len(team_result), 3)
        self.assertEqual(team_result[0].name, 'Gretzky')
        
    def test_top_piste_raja(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(len(top_scorers), 3)
        
    def test_ei_palauta_ei_loytynytta_pelaajaa(self):
        search_result = self.statistics.search('Semenko')
        self.assertEqual(search_result, None)
