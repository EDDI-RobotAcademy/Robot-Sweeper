import unittest
from database_work_id.repository.DatabaseWorkIdRepositoryImpl import DatabaseWorkIdRepositoryImpl
from database_coordinate.repository.DatabaseCoordinateRepositoryImpl import DatabaseCoordinateRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase

class TestWorkIdRepository(unittest.TestCase):

    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSaveCoordinateData(self):
        repository = DatabaseCoordinateRepositoryImpl.getInstance()
        work_id: int = 2
        coordinate_data = {
            'X_coordinate': 3.5,
            'Y_coordinate': 10.2,
            'Z_coordinate': -5.3,
            'Waypoint_ID': "1234567890",
            'Town_Number': "Town03"
        }

        result = repository.saveCoordinate(work_id, coordinate_data)

        self.assertTrue(result)

    def testFindById(self):
        repository = DatabaseWorkIdRepositoryImpl.getInstance()
        findedId = repository.findById(8)

        self.assertIsNotNone(findedId)
        self.assertEqual(findedId.get_id(), 1)

    def testDeleteById(self):
        repository = DatabaseWorkIdRepositoryImpl.getInstance()

        id: int = 8

        findedId = repository.findById(id)
        self.assertIsNotNone(findedId)

        deletedId = repository.deleteById(id)
        self.assertIsNone(deletedId)

    def testFindCoordinateById(self):
        repository = DatabaseCoordinateRepositoryImpl.getInstance()
        result = repository.findCoordinate(18)

        print("result:", result)

        self.assertIsNotNone(result)
