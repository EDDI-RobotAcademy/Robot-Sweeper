import abc

class DatabaseWorkIdRepository(abc.ABC):

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
