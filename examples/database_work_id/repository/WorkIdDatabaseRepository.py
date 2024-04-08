import abc

from database_work_id.entity.WorkIdDatabase import WorkId

class WorkIdDatabaseRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, work_id: int):
        pass

    @abc.abstractmethod
    def getBoolWithFindById(self, work_id: int):
        pass

    @abc.abstractmethod
    def findById(self, work_id: int):
        pass

    @abc.abstractmethod
    def deleteById(self, work_id: int):
        pass
