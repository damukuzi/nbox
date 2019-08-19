import os
import unittest
from Postgres import Postgresdb

class TestCnnctn(unittest.TestCase):

    def test_connection(self):
        db = Postgresdb()
        self.assertEqual(db.connect(),
                            'connection successful')

if __name__ == "__main__":
    unittest.main()
