# import urllib.request
import os
import unittest
from multitransport.download_csv import download


class DownloadCsv(unittest.TestCase):
    # check response status is 200
    def test_download_MTP(self):
        dl = download("Montpellier")
        self.assertTrue(os.path.exists(dl))
        os.remove(dl)

    def test_download_RNS(self):
        dl = download("Rennes")
        self.assertTrue(os.path.exists(dl))
        os.remove(dl)

#     # def test_download_LIL(self):
#     #     dl = download("Lille")
#     #     self.assertTrue(os.path.exists(dl))
#     #     os.remove(dl)

#     # def test_download_ANE(self):
#     #     dl = download("Angers")
#     #     self.assertTrue(os.path.exists(dl))
#     #     os.remove(dl)


if __name__ == "__main__":
    unittest.main()
