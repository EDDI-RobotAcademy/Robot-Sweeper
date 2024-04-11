import abc
from database_coordinate.entity.CoordinateDatabase import Coordinate


class DatabaseCoordinateRepository(abc.ABC):

    @abc.abstractmethod
    def saveWorkId(self) -> int:
        pass

    @abc.abstractmethod
    def saveCoordinate(self, work_id: int, coordinate_data: Coordinate):
        pass

    @abc.abstractmethod
    def findCoordinate(self, work_id: int):
        pass

    @abc.abstractmethod
    def findCoordinateById(self, work_id: int):
        pass
