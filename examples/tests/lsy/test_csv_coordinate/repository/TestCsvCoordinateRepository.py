import unittest
from csv_coordinate.repository.csv_coordinate_repository_impl import CsvCoordinateRepositoryImpl


class TestWorkIdRepository(unittest.TestCase):

    def testSaveCoordinateData(self):
        repository = CsvCoordinateRepositoryImpl.getInstance()

        work_id = 2
        X_coordinate = 100.5
        Y_coordinate = 10.2
        Z_coordinate = -50.3
        Waypoint_ID = "1012345678"
        Town_Number = "Town03"

        result = repository.saveToCsv(work_id, X_coordinate, Y_coordinate, Z_coordinate, Waypoint_ID, Town_Number)

        self.assertTrue(result)
