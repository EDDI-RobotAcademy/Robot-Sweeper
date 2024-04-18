import unittest
from csv_coordinate.repository.CsvCoordinateRepositoryimpl import CsvCoordinateRepositoryImpl


class TestCsvCoordinateRepository(unittest.TestCase):

    def testSaveCoordinate(self):
        repository = CsvCoordinateRepositoryImpl()

        work_id = 2
        X_coordinate = 100.2
        Y_coordinate = 4.5
        Z_coordinate = -7.8
        Waypoint_ID = "1012345678"
        Town_Number = "Town03"

        result = repository.saveCoordinateInCsv(work_id, X_coordinate, Y_coordinate, Z_coordinate, Waypoint_ID,
                                                Town_Number)

        self.assertTrue(result)

