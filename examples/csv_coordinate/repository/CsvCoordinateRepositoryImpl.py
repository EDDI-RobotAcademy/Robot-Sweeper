import os
import pandas as pd

from csv_coordinate.repository.CsvCoordinateRepository import CsvCoordinateRepository
from csv_coordinate.entity.CoordinateInfoFromCsv import CoordinateInfoFromCsv


class CsvCoordinateRepositoryImpl(CsvCoordinateRepository):
    HEADER = ['work_id', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'wayPointId', 'townNumber']
    HEADER_WORK_ID = ['work_id', 'temp_work_id']

    def __init__(self):
        self.csv_file_path = 'coordinates.csv'

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
            # cls.__instance.databaseWorkIdRepository = DatabaseWorkIdRepositoryImpl().getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def saveCoordinateInCsv(self, work_id, x_coordinate, y_coordinate, z_coordinate, wayPointId, townNumber):
        print("CsvCoordinateRepositoryImpl: saveCoordinateInCsv()")

        bind_data_for_saving = {
            'work_id': [work_id],
            'x_coordinate': [x_coordinate],
            'y_coordinate': [y_coordinate],
            'z_coordinate': [z_coordinate],
            'wayPointId': [wayPointId],
            'townNumber': [townNumber],
        }

        data_frame = pd.DataFrame(bind_data_for_saving)
        data_frame = data_frame[self.HEADER]
        header = not os.path.exists(self.csv_file_path)

        if header:
            data_frame.to_csv(self.csv_file_path, mode='w', index=False, header=self.HEADER)
        else:
            data_frame.to_csv(self.csv_file_path, mode='a', index=False, header=False)

        return True

    def read_waypoint_data_from_csv(self):
        print("CsvCoordinateRepositoryImpl: read_waypoint_data_from_csv()")

        try:
            data_frame = pd.read_csv('coordinates.csv')

            for index, row in data_frame.iterrows():
                print("work_id: {}".format(row['work_id']))
                print("x_coordinate: {}".format(row['x_coordinate']))
                print("y_coordinate: {}".format(row['y_coordinate']))
                print("z_coordinate: {}".format(row['z_coordinate']))
                print("wayPointId: {}".format(row['wayPointId']))
                print("townNumber: {}".format(row['townNumber']))
                print()

        except FileNotFoundError:
            print("File not found.")
        except pd.errors.EmptyDataError:
            print("File is empty.")

        return True

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

    def count_work_id(self):
        print("CsvCoordinateRepositoryImpl: count_work_id()")

        work_id_file_path = "work_id.csv"

        work_id = 1
        temp_work_id = 1

        bind_data_for_saving = {
            'work_id': [work_id],
            'temp_work_id': [temp_work_id],
        }

        data_frame = pd.DataFrame(bind_data_for_saving)
        data_frame = data_frame[self.HEADER_WORK_ID]
        header = not os.path.exists(work_id_file_path)

        if header:
            data_frame.to_csv(work_id_file_path, mode='w', index=False, header=self.HEADER_WORK_ID)

            return 1

        else:
            existing_data_frame = pd.read_csv(work_id_file_path)
            existing_data_frame.loc[len(existing_data_frame)] = ''
            for i in range(len(existing_data_frame) - 1, 0, -1):
                existing_data_frame.loc[i] = existing_data_frame.loc[i - 1]
            existing_data_frame.loc[0] = existing_data_frame.loc[1] +1

            existing_data_frame.to_csv(work_id_file_path, mode='w', index=False, header=self.HEADER_WORK_ID)

            print("count_work_id", existing_data_frame.iloc[0]['work_id'])

            return existing_data_frame.iloc[0]['work_id']

    def read_work_id(self):
        print("CsvCoordinateRepositoryImpl: read_work_id()")

        work_id_file_path = "work_id.csv"

        existing_data_frame = pd.read_csv(work_id_file_path)
        current_work_id = existing_data_frame.iloc[0]['work_id']
        print("current_work_id", current_work_id)

        return current_work_id
