import unittest
from database_coordinate.service.DatabaseCoordinateServiceImpl import DatabaseCoordinateServiceImpl
from mysql.MySQLDatabase import MySQLDatabase


class TestWorkIdRepository(unittest.TestCase):

    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSaveDateListType(self):
        service = DatabaseCoordinateServiceImpl.getInstance()

        data_01 = {"X_coordinate": 1.1, "Y_coordinate": 2.1, "Z_coordinate": 3.1, "Waypoint_ID": "1234", "Town_Number": "Town03"}
        data_02 = {"X_coordinate": 4.2, "Y_coordinate": 5.2, "Z_coordinate": 6.2, "Waypoint_ID": "5678", "Town_Number": "Town03"}
        data_03 = {"X_coordinate": 7.3, "Y_coordinate": 8.3, "Z_coordinate": 9.3, "Waypoint_ID": "9000", "Town_Number": "Town03"}

        print("data_01", data_01)
        print("data_02", data_02)
        print("data_03", data_03)

        data_List: list = []

        data_List.append(data_01)
        data_List.append(data_02)
        data_List.append(data_03)

        print("dataList: ", data_List)

        result = service.saveCoordinateData(data_List)

        self.assertTrue(result)
