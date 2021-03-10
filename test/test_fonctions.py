import unittest
# import multitransport.listes_all as la
# from multitransport.readcsv import readcsv
from multitransport.fonctions import liste_trains, liste_next, liste_stations


class TestFonctions(unittest.TestCase):
    def test_liste_stations(self):
        self.assertIs(type(liste_stations("Montpellier")), list)
        self.assertIsNotNone((liste_stations("Montpellier")))
        # for town in la.listes_all_town():
        #     self.assertIs(type(liste_stations(town)), list)
        #     self.assertIsNotNone((liste_stations(town)))

    def test_liste_trains(self):
        self.assertIs(type(liste_trains('ODYSSEUM', "Montpellier")), list)
        self.assertIsNotNone((liste_trains("SABINES", "Montpellier")))
        # for town in la.listes_all_town():
        #     for station in la.liste_all_station(town):
        #         self.assertIs(type(liste_trains(station, town)), list)
        #         self.assertIsNotNone((liste_trains(station, town)))

    def test_liste_next(self):
        self.assertIs(type(liste_next(
                    'OCCITANIE', 'MOSSON', "1", "Montpellier")
                    ), list)
        self.assertIsNotNone((liste_next("SABINES",
                                         "JACOU", "2", "Montpellier")))
        # for town in la.listes_all_town():
        #     for ligne in readcsv(town):
        #         self.assertIs(
        #             type(liste_next(
        #                 ligne[1], ligne[2], ligne[0], town)
        #                 ), list)
        #         self.assertIsNotNone(
        #             (liste_next(ligne[1], ligne[2], ligne[0], town)))


if __name__ == '__main__':
    unittest.main()
