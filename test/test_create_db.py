import sqlite3
import unittest


class TestFonctions(unittest.TestCase):
    # def test_connection(self):
    #     self.connection = sqlite3.connect(":memory:")


    def test_liste_stations(self):
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE IF EXISTS table_test""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS "table_test" (
        "Ligne"	TEXT,
        "Arrêt"	TEXT,
        "Destination"	TEXT,
        "Temps_attente"	INTEGER,
        "Ville"	TEXT
        );""")
        cursor.execute(
            """
            SELECT * FROM 'table_test';
            """)
        self.assertEqual(cursor.fetchone(), None)
        with open('TAM_test.csv', "r", encoding="utf-8") as f:
            f.readline()
            line = f.readline()
            while line:
                cursor.execute("""
                INSERT INTO table_test VALUES (?,?,?,?,?)
                """, line.strip().split(";"))
                line = f.readline()
        conn.commit()
        cursor.execute(
            """
            SELECT * FROM 'table_test';
            """)
        self.assertEqual(
            cursor.fetchone(),
            ('1', 'ANTIGONE', 'MOSSON', '21:05:23', 'Montpellier')
            )


if __name__ == '__main__':
    unittest.main()
