import abc

from csv_coordinate.entity.CsvCoordinate import CsvCoordinate


class CsvCoordinateRepository(abc.ABC):
    @abc.abstractmethod
    def saveCoordinateInCsv(self, work_id, x_coordinate, y_coordinate, z_coordinate, wayPointId, townNumber):
        pass

    def readCoordinateInCsv(self, work_id) -> CsvCoordinate:
        pass
