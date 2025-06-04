from database.DB_connect import DBConnect
from model.dtos import Stato

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def _getStatiVicinanze(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        try:
            query = """select c.StateAbb as s1abb, c.CCode as s1code, c.StateNme as s1name,
                            c3.StateAbb as s2abb, c3.CCode as s2code, c3.StateNme as s2name
                        from country c, contiguity c2 , country c3 
                        where c.StateAbb  = c2.state1ab  and c3.StateAbb = c2.state2ab and c.StateAbb < c2.state2ab
                            and c2.`year` <= %s and c2.conttype = 1"""
            cursor.execute(query, (year,))
            result = []
            for row in cursor.fetchall():
                result.append((Stato(row['s1abb'], row['s1code'], row['s1name']),
                               Stato(row['s2abb'], row['s2code'], row['s2name'])))
            return result
        finally:
            cursor.close()
            cnx.close()