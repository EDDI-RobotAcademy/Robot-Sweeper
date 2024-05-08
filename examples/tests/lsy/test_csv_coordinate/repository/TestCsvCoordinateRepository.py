import unittest
import os
import pandas as pd

from csv_coordinate.repository.CsvCoordinateRepository import CsvCoordinateRepository
from csv_coordinate.repository.CsvCoordinateRepositoryImpl import CsvCoordinateRepositoryImpl


class TestCsvCoordinateRepository(unittest.TestCase):

    def testSaveCoordinate(self):
        repository = CsvCoordinateRepositoryImpl()

        work_id = 5
        x_coordinate = 555.2
        y_coordinate = -300.5
        z_coordinate = -77.7
        waypoint_id = "1012345678"
        town_number = "Town03"

        result = repository.saveCoordinateInCsv(work_id, x_coordinate, y_coordinate, z_coordinate, waypoint_id,
                                                town_number)

        self.assertTrue(result)

    def testReadCoordinate(self):
        repository = CsvCoordinateRepositoryImpl()

        result = repository.read_waypoint_data_from_csv()

        print("result: ", result)

        self.assertTrue(result)

    def testBuildDictionariesFromCSV(self):
        repository = CsvCoordinateRepositoryImpl()

        work_id = 3

        read_info = repository.read_waypoint_data_from_csv(work_id)
        build_info = repository.build_dictionaries(read_info)

        coordinate_numbers = repository.get_csv_number()
        print("csv_number: ", coordinate_numbers)

        for coordinate_number in coordinate_numbers:
            x = repository.get_x_coordinate(coordinate_number)
            y = repository.get_y_coordinate(coordinate_number)
            z = repository.get_z_coordinate(coordinate_number)
            way_point_id = repository.get_way_point_id(coordinate_number)
            town_number = repository.get_town_number(coordinate_number)

            print("coordinate_number: ", coordinate_number)
            print("x: ", x)
            print("y: ", y)
            print("z: ", z)
            print("way_point_id: ", way_point_id)
            print("town_number: ", town_number)

        self.assertIsNone(build_info)

    def test_count_work_id(self):
        repository = CsvCoordinateRepositoryImpl()

        result = repository.count_work_id()

        print("result: ", result)

        self.assertTrue(result)
