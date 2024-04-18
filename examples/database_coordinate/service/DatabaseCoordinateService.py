import abc


class DatabaseCoordinateService(abc.ABC):
    @abc.abstractmethod
    def saveCoordinateData(self, *args, **kwargs):
        pass
