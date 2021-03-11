import unittest
from multitransport.create_db import *


# class TestFonctions(unittest.TestCase):
    # def test_connection(self):
    #     self.connection = sqlite3.connect(":memory:")


#     def test_liste_stations(self):
#         conn = sqlite3.connect(":memory:")
#        cursor = conn.cursor()
#        cursor.execute("""DROP TABLE IF EXISTS table_test""")
#        cursor.execute("""CREATE TABLE IF NOT EXISTS "table_test" (
#        "Ligne"	TEXT,
#        "Arrêt"	TEXT,
#        "Destination"	TEXT,
#        "Temps_attente"	INTEGER,
#        "Ville"	TEXT
#        );""")
#        cursor.execute(


class TestCreateDb(unittest.TestCase):

    def test_create_schema(self):
        conn, c = connect(":memory:")
        create_schema(c)
        c.execute(
            """
            SELECT * FROM 'info_trafic';
            """)
        self.assertEqual(c.fetchone(), None)
        conn.commit()
        conn.close()

    def test_clear_rows(self):
        conn, c = connect(":memory:")
        create_schema(c)
        c.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                  ('1', 'test1', 'test1', '12:00:00', 'Montpellier'))
        c.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                  ('2', 'test2', 'test2', '14:00:00', 'Montpellier'))
        clear_rows(c, "Montpellier")
        # tester la longueur du tableau pour vérifier qu'il est égal à 0
        self.assertEqual(c.fetchone(), None)

    def test_insert_csv_row(self):
        conn, c = connect(":memory:")
        create_schema(c)
        row1 = ['3', 'test3', 'test3', '16:30:00', "Montpellier"]
        insert_csv_row(row1, c)
        requete = c.execute("""SELECT * FROM info_trafic WHERE ligne = '3'""")
        self.assertEqual(c.fetchone(), ('3', 'test3', 'test3', '16:30:00',
                                        'Montpellier'))

    # def test_load_csv(self):
    #     conn, c = connect(":memory:")

    def test_remove_table(self):
        conn, c = connect(":memory:")
        create_schema(c)
        c.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                  ('1', 'test1', 'test1', '12:00:00', 'Montpellier'))
        c.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                  ('2', 'test2', 'test2', '14:00:00', 'Montpellier'))
        remove_table(c)
        self.assertEqual(c.fetchone(), None)

    def test_create_schema(self):
        conn, c = connect(":memory:")
        create_schema(c)
        c.execute(
            """
            SELECT * FROM 'info_trafic';
            """)
        self.assertEqual(c.fetchone(), None)
        conn.commit()
        conn.close()

    # def set_up(self):
    #     conn = sqlite3.connect(":memory:")
    #     c = conn.cursor()
    #     create_schema(c)
    #     c.execute(
    #         """
    #         SELECT * FROM 'info_trafic';
    #         """)

    #     with open('./test/TAM_test.csv', "r", encoding="utf-8") as f:
    #         f.readline()
    #         line = f.readline()
    #         while line:
    #             insert_csv_row(line.strip().split(';'), c)
    #             line = f.readline()


if __name__ == '__main__':
    unittest.main()
