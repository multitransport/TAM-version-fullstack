import sqlite3
import unittest
from multitransport.create_db import *


class TestCreateDb(unittest.TestCase):
    
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


    def test_create_schema(self):
        # set_up(self)
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
        self.assertEqual(c.fetchone(),('3', 'test3', 'test3', '16:30:00', 'Montpellier'))


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
        # test = c.execute(
        #     """
        #     SELECT * FROM 'info_trafic';
        #     """)
        # try:
        #     c.execute("""SELECT * 
        #          FROM info_trafic""")
        #     print('table existe')
        # except: 
        #     print("table n'existe pas")
        # self.assertEqual(c.fetchone(),('1', 'test1', 'test1', '12:00:00', 'Montpellier'))
        
        # try:
        #     c.execute("""SELECT * 
        #          FROM info_trafic""")
        #     print('table existe')
        # except: 
        #     print("table n'existe pas")
        
                 
                 
        # f c.fetchone()[0]==1 : 
        #     print('Table exists.')
        # else :
        #     print('Table does not exist.')
        # remove_table(c)
        # # if c.fetchone()[0]==1 : {
        # #     print('Table exists.')
        # # }
        # self.assertEqual(c.fetchone(), None)


    # def test_liste_stations(self):
    #     conn, c = connect(":memory:")
    #     self.connection = sqlite3.connect(":memory:")
    #     create_schema(c)
    #     c.execute(
    #         """
    #         SELECT * FROM 'info_trafic';
    #         """)
    #     self.assertEqual(c.fetchone(), None)
    #     with open('./test/TAM_test.csv', "r", encoding="utf-8") as f:
    #         f.readline()
    #         line = f.readline()
    #         while line:
    #             insert_csv_row(line.strip().split(';'), c)
    #             line = f.readline()
    #     c.execute(
    #         """
    #         SELECT * FROM 'info_trafic';
    #         """)
    #     self.assertEqual(
    #         c.fetchone(),
    #         ('1', 'ANTIGONE', 'MOSSON', '21:05:23', 'Montpellier')
    #         )

    #     # clear_rows(c, "Montpellier")
    #     # self.assertEqual(c.fetchone(), None)
    #     result = c.execute(
    #         """
    #         SELECT exists (select * from info_trafic);
    #         """).fetchall()
    #     self.assertEqual(result, [(1,)])
    #     remove_table(c)


        

        # conn.close()
        # with open('./test/TAM_test.csv', "r", encoding="utf-8") as f:
        #     f.readline()
        #     line = f.readline()
        #     while line:
        #         cursor.execute("""
        #         INSERT INTO table_test VALUES (?,?,?,?,?)
        #         """, line.strip().split(";"))
        #         line = f.readline()
        # conn.commit()
        # cursor.execute(
        #     """
        #     SELECT * FROM 'table_test';
        #     """)
        # self.assertEqual(
        #     cursor.fetchone(),
        #     ('1', 'ANTIGONE', 'MOSSON', '21:05:23', 'Montpellier')
        #     )


if __name__ == '__main__':
    unittest.main()
