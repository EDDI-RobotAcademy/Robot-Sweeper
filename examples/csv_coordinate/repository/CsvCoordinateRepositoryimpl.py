import os
import pandas as pd

from database_work_id.repository.DatabaseWorkIdRepositoryImpl import DatabaseWorkIdRepositoryImpl
from csv_coordinate.repository.CsvCoordinateRepository import CsvCoordinateRepository
from csv_coordinate.entity.CoordinateInfoFromCsv import CoordinateInfoFromCsv
from csv_coordinate.entity.CsvCoordinate import CsvCoordinate


class CsvCoordinateRepositoryImpl(CsvCoordinateRepository):
    __instance = None
    __csvNumberDictionary = []
    __workIdDictionary = {}
    __xCoordinateDictionary = {}
    __yCoordinateDictionary = {}
    __zCoordinateDictionary = {}
    __wayPointIdDictionary = {}
    __townNumberDictionary = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.databaseWorkIdRepository = DatabaseWorkIdRepositoryImpl().getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save_coordinate_in_csv(self, work_id, x_coordinate, y_coordinate, z_coordinate, way_point_id, town_number) -> bool:
        print("CsvCoordinateRepositoryImpl: saveCoordinateInCsv()")
        print("work_id: ", work_id)
        print("x_coordinate: ", x_coordinate)
        print("y_coordinate: ", y_coordinate)
        print("z_coordinate: ", z_coordinate)
        print("wayPointId: ", way_point_id)
        print("townNumber: ", town_number)

        bind_data_for_saving = {
            'work_id': [work_id],
            'x_coordinate': [x_coordinate],
            'y_coordinate': [y_coordinate],
            'z_coordinate': [z_coordinate],
            'wayPointId': [way_point_id],
            'townNumber': [town_number],
        }

        data_frame = pd.DataFrame(bind_data_for_saving)
        file_path = 'waypoint_data.csv'
        header = not os.path.exists(file_path)
        data_frame.to_csv(file_path, mode='a', index=False, header=header)

        return True

    def read_waypoint_data_from_csv(self, work_id):
        print("CsvCoordinateRepositoryImpl: read_waypoint_data_from_csv()")
        print("work_id: ", work_id)

        data_frame = pd.read_csv('waypoint_data.csv')
        filtered_data_frame = data_frame[data_frame['work_id'] == work_id]

        print("filtered_data_frame: ", filtered_data_frame)

        find_row_number = 1
        find_row = filtered_data_frame.iloc[find_row_number]
        x_coordinate = find_row['x_coordinate']
        y_coordinate = find_row['y_coordinate']
        z_coordinate = find_row['z_coordinate']
        way_point_id = find_row['wayPointId']

        print("x_coordinate: ", x_coordinate)
        print("y_coordinate: ", y_coordinate)
        print("z_coordinate: ", z_coordinate)
        print("way_point_id: ", way_point_id)

        return filtered_data_frame.itertuples()

    def build_dictionaries(self, csv_data):
        print("CsvCoordinateRepositoryImpl: build_dictionaries()")

        count_number = 0
        for record in csv_data:

            try:
                coordinate_info = CoordinateInfoFromCsv(record)

                self.__csvNumberDictionary.append(count_number)
                self.__workIdDictionary[count_number] = coordinate_info.get_work_id()
                self.__xCoordinateDictionary[count_number] = coordinate_info.get_x_coordinate()
                self.__yCoordinateDictionary[count_number] = coordinate_info.get_y_coordinate()
                self.__zCoordinateDictionary[count_number] = coordinate_info.get_z_coordinate()
                self.__wayPointIdDictionary[count_number] = coordinate_info.get_way_point_id()
                self.__townNumberDictionary[count_number] = coordinate_info.get_town_number()

                count_number += 1

            except Exception as e:
                print("Error : ", e)

    def get_csv_number(self):
        return self.__csvNumberDictionary

    def get_work_id(self, csv_number):
        return self.__workIdDictionary[csv_number]

    def get_x_coordinate(self, csv_number):
        return self.__xCoordinateDictionary[csv_number]

    def get_y_coordinate(self, csv_number):
        return self.__yCoordinateDictionary[csv_number]

    def get_z_coordinate(self, csv_number):
        return self.__zCoordinateDictionary[csv_number]

    def get_way_point_id(self, csv_number):
        return self.__wayPointIdDictionary[csv_number]

    def get_town_number(self, csv_number):
        return self.__townNumberDictionary[csv_number]
