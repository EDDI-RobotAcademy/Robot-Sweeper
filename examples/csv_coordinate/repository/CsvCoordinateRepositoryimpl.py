import csv
import os
import pandas as pd

from database_work_id.repository.DatabaseWorkIdRepositoryImpl import DatabaseWorkIdRepositoryImpl
from csv_coordinate.repository.CsvCoordinateRepository import CsvCoordinateRepository
from csv_coordinate.entity.CsvCoordinate import CsvCoordinate


class CsvCoordinateRepositoryImpl(CsvCoordinateRepository):
    __instance = None
    __csvNumberDictionary = []
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

    def saveCoordinateInCsv(self, work_id, x_coordinate, y_coordinate, z_coordinate, wayPointId, townNumber) -> bool:
        print("CsvCoordinateRepositoryImpl: saveCoordinateInCsv()")
        print("work_id: ", work_id)
        print("x_coordinate: ", x_coordinate)
        print("y_coordinate: ", y_coordinate)
        print("z_coordinate: ", z_coordinate)
        print("wayPointId: ", wayPointId)
        print("townNumber: ", townNumber)

        bind_data_for_saving = {
            'work_id': [work_id],
            'x_coordinate': [x_coordinate],
            'y_coordinate': [y_coordinate],
            'z_coordinate': [z_coordinate],
            'wayPointId': [wayPointId],
            'townNumber': [townNumber],
        }

        data_frame = pd.DataFrame(bind_data_for_saving)
        file_path = 'waypoint_data.csv'
        header = not os.path.exists(file_path)
        data_frame.to_csv(file_path, mode='a', index=False, header=header)

        return True