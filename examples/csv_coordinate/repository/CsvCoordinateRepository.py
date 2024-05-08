class CsvCoordinateRepository:
    def saveCoordinateInCsv(self, work_id, x_coordinate, y_coordinate, z_coordinate, wayPointId, townNumber):
        raise NotImplementedError("saveCoordinateInCsv method must be implemented")

    def read_waypoint_data_from_csv(self):
        pass

    def build_dictionaries(self, csv_data):
        pass

    def get_csv_number(self):
        pass

    def get_work_id(self, csv_number):
        pass

    def get_x_coordinate(self, csv_number):
        pass

    def get_y_coordinate(self, csv_number):
        pass

    def get_z_coordinate(self, csv_number):
        pass

    def get_way_point_id(self, csv_number):
        pass

    def get_town_number(self, csv_number):
        pass

    def count_work_id(self):
        pass

    def read_work_id(self):
        pass
