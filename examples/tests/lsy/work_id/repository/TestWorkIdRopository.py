import unittest
from database_work_id.entity.DatabaseWorkId import WorkId
from database_work_id.repository.DatabaseWorkIdRepositoryImpl import WorkIdDatabaseRepositoryImpl
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

        }
        work_id = WorkId(**work_id_data)

        result = repository.save(work_id)

        self.assertTrue(result)

    def testFindById(self):
        repository = WorkIdDatabaseRepositoryImpl.getInstance()
        findedId = repository.findById(8)

        self.assertIsNotNone(findedId)
        self.assertEqual(findedId.get_id(), 8)

    def testDeleteById(self):
        repository = WorkIdDatabaseRepositoryImpl.getInstance()

        id: int = 8

        findedId = repository.findById(id)
        self.assertIsNotNone(findedId)

        deletedId = repository.deleteById(id)
        self.assertIsNone(deletedId)
