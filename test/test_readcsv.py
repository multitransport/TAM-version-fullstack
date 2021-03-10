import unittest
import multitransport.readcsv as readcsv
import multitransport.listes_all as la
from multitransport.download_csv import download


class TestReadCSV(unittest.TestCase):
    def test_readcsv(self):
        self.assertIsNotNone(readcsv.readcsv("Montpellier"))
        self.assertIs(type(readcsv.readcsv("Montpellier")), list)
        # for town in la.listes_all_town():
        #     self.assertIsNotNone(readcsv.readcsv(town))
        #     self.assertIs(type(readcsv.readcsv(town)), list)


class TestListeCSVTown(unittest.TestCase):
    def test_liste_csv_MPL(self):
        with open(download("Montpellier"), newline='', encoding='utf-8') as f:
            self.assertIs(type(readcsv.liste_csv_MPL(f)), list)
        # for town in la.listes_all_town():
        #     with open(download(town), newline='', encoding='utf-8') as f:
        #         self.assertIs(type(readcsv.liste_csv_MPL(f)), list)

    # def test_liste_csv_RNS(self):
    #     with open(download("Rennes"), newline='', encoding='utf-8') as f:
    #             self.assertIsNotNone(readcsv.liste_csv_RNS(f))
    #             self.assertIs(type(readcsv.liste_csv_RNS(f)), list)
    #     # for town in la.listes_all_town():
    #     #     with open(download(town), newline='', encoding='utf-8') as f:
    #     #         self.assertIsNotNone(readcsv.liste_csv_RNS(f))
    #     #         self.assertIs(type(readcsv.liste_csv_RNS(f)), list)
