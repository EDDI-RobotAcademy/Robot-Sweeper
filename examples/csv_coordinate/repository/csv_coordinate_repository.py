import abc

from csv_coordinate.entity.csv_coordinate import CsvCoordinate


class CsvCoordinateRepository(abc.ABC):
    @abc.abstractmethod
    def saveToCsv(self, work_id, x_coordinate, y_coordinate, z_coordinate, wayPointId, townNumber):
        pass
