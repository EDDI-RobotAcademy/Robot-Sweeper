import csv
import os

from database_work_id.repository.DatabaseWorkIdRepositoryImpl import DatabaseWorkIdRepositoryImpl
from csv_coordinate.repository.csv_coordinate_repository import CsvCoordinateRepository


class CsvCoordinateRepositoryImpl(CsvCoordinateRepository):
    __instance = None
    # __xCoordinateDictionary = []
    # __yCoordinateDictionary = []
    # __zCoordinateDictionary = []
    # __wayPointIdDictionary = []
    # __townNumberDictionary = []

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
        print("work_id: ", work_id)
        print("x_coordinate: ", x_coordinate)
        print("y_coordinate: ", y_coordinate)
        print("z_coordinate: ", z_coordinate)
        print("wayPointId: ", wayPointId)
        print("townNumber: ", townNumber)

        bind_data_for_saving = []
        bind_data_for_saving = {
            'work_id': work_id,
            'x_coordinate': x_coordinate,
            'y_coordinate': y_coordinate,
            'z_coordinate': z_coordinate,
            'wayPointId': wayPointId,
            'townNumber': townNumber,
        }

        file_path = 'waypoint_data.csv'
        if os.path.isfile(file_path):
            mode = 'a'
            print("mode: a")
        else:
            mode = 'w'
            print("mode: w")

        field_names = list(bind_data_for_saving.keys())
        try:
            with open(file_path, mode, newline='') as csvfile:
                if mode == 'a':
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writerow(bind_data_for_saving)
                elif mode == 'w':
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()  # Write header only if it's a new file
                    writer.writerow(bind_data_for_saving)

        except Exception as e:
            print("Error while saving: ", e)

        return True
