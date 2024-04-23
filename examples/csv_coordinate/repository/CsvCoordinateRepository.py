import abc

from csv_coordinate.entity.CsvCoordinate import CsvCoordinate


class CsvCoordinateRepository(abc.ABC):
    @abc.abstractmethod
    def save_coordinate_in_csv(self, work_id, x_coordinate, y_coordinate, z_coordinate, way_point_id, town_number):
        pass

    def read_waypoint_data_from_csv(self, work_id):
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
