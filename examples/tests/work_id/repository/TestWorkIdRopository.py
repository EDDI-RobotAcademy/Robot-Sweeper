import unittest
from work_id_database.entity.WorkIdDatabase import WorkId
from work_id_database.repository.WorkIdDatabaseRepositoryImpl import WorkIdDatabaseRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase

class TestWorkIdRepository(unittest.TestCase):

    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSaveWorkId(self):
        repository = WorkIdDatabaseRepositoryImpl.getInstance()
        work_id_data = {
            "x_coordinate": 10.2,
            "y_coordinate": 3.3,
            "z_coordinate": -5.8
        }
        work_id = WorkId(**work_id_data)

        result = repository.saveWorkId(work_id)
        self.assertTrue(result)