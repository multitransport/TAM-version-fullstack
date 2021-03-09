import urllib.request
import os
import unittest

class DownloadCsv(unittest.TestCase):
    # check response status is 200
    def test_download_MTP(self):
        url = 'https://data.montpellier3m.fr/sites/default/files/ressources' \
                '/TAM_MMM_TpsReel.csv'
        dl = "test_TpsReel_MPL.csv"
        urllib.request.urlretrieve(url, dl)
        # actual_file_path = app.config.get('BASE_DIR') + '/static/uploads/' + filename
        # self.assertEqual(file_path, actual_file_path)
        self.assertTrue(os.path.exists(dl))

    # def test_download_RNS(self):
    #     url = 'https://data.rennesmetropole.fr/explore/dataset/prochains-pa' \
    #             'ssages-des-lignes-de-metro-du-reseau-star-en-temps-reel/do' \
    #             'wnload/?format=csv&timezone=Europe/Berlin&lang=fr&use_labe' \
    #             'ls_for_header=true&csv_separator=%3B'
    #     dl = "test_TpsReel_RNS.csv"
    #     urllib.request.urlretrieve(url, dl)
    #     self.assertTrue(os.path.exists(dl))

    # def test_download_LIL(self):
    #     url = 'https://opendata.lillemetropole.fr/explore/dataset/ilevia-pr' \
    #             'ochainspassages/download/?format=csv&timezone=Europe/Paris' \
    #             '&lang=fr&use_labels_for_header=true&csv_separator=%3B'
    #     dl = "test_TpsReel_LIL.csv"
    #     urllib.request.urlretrieve(url, dl)
    #     self.assertTrue(os.path.exists(dl))

    # def test_download_ANE(self):
    #     url = 'https://data.angers.fr/explore/dataset/bus-tram-circulation-' \
    #             'passages/download/?format=csv&timezone=Europe/Berlin&lang=' \
    #             'fr&use_labels_for_header=true&csv_separator=%3B'
    #     dl = "test_TpsReel_ANE.csv"
    #     urllib.request.urlretrieve(url, dl)
    #     self.assertTrue(os.path.exists(dl))


if __name__ == "__main__":
    unittest.main()