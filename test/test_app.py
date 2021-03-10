import unittest
from multitransport.app import app


class TestAllStations(unittest.TestCase):

    def test_all_stations_status(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations")
        self.assertEqual(result.status_code, 200)

    def test_all_stations_type(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations")
        self.assertEqual(result.content_type, "application/json")

    def test_all_stations_data(self):
        ''' verification of the data in the results '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations")
        self.assertTrue(b'ANTIGONE' in result.data)


class TestNextTrains(unittest.TestCase):

    def test_next_trains_status(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations/ODYSSEUM")
        self.assertEqual(result.status_code, 200)

    def test_next_trains_type(self):
        ''' verifies the type of data
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations/ODYSSEUM")
        self.assertEqual(result.content_type, "application/json")

    def test_next_trains_data(self):
        ''' verifies the type of data '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/stations/ODYSSEUM")
        self.assertTrue(b'ODYSSEUM' in result.data)


class TestNextPassages(unittest.TestCase):

    def test_next_passages_status(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/next/?line=1&station"
                              "=ODYSSEUM&destination=MOSSON")
        self.assertEqual(result.status_code, 200)

    def test_next_passages_type(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/Montpellier/next/?line=1&station"
                              "=ODYSSEUM&destination=MOSSON")
        self.assertEqual(result.content_type, "application/json")

    def test_next_passages_data(self):
        self.app = app.test_client()
        result = self.app.get("/Montpellier/next/?line=1&station"
                              "=ODYSSEUM&destination=MOSSON")
        self.assertTrue(b'ODYSSEUM' in result.data)


if __name__ == '__main__':
    unittest.main()
