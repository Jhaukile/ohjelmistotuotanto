import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_returnaa_pelaajan(self):
        name = "Semenko"
        self.assertEqual(self.stats.search(name).name, name)
    
    def test_pelaajaa_ei_loydy(self):
        name = "Kekkonen"
        self.assertIsNone(self.stats.search(name))

    def test_returnaa_joukkueen_pelaajat(self):
        team = "EDM"
        players = self.stats.team(team)
        self.assertEqual(len(players), 3)
        for player in players:
            self.assertEqual(player.team, team)
    
    def test_returnaa_top_pistemiehet(self):
        top_scorers = self.stats.top(3)
        self.assertEqual(len(top_scorers), 4)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")
        self.assertEqual(top_scorers[3].name, "Kurri")