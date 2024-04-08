from sqlalchemy.orm import sessionmaker

from database_work_id.entity.WorkIdDatabase import WorkId
from database_work_id.repository.WorkIdDatabaseRepository import WorkIdDatabaseRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

class WorkIdDatabaseRepositoryImpl(WorkIdDatabaseRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save(self, work_id: int):
        print("WorkIdDatabaseRepositoryImpl: save()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(work_id)
            session.commit()

            print(f"saved_work_id: {work_id.get_id()}")
            return work_id

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def findById(self, work_id: int):
        print("WorkIdDatabaseRepositoryImpl: findById()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(WorkId).filter_by(_WorkId__id=work_id).first()

    def deleteById(self, work_id: int):
        print("WorkIdDatabaseRepositoryImpl: deleteById()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        workId = session.query(WorkId).filter_by(_WorkId__id=work_id).first()
        if workId:
            session.delete(workId)
            session.commit()

    def getBoolWithFindById(self, work_id: int):
        print("WorkIdDatabaseRepositoryImpl: getBoolWithFindById()")
        if self.findById(work_id) is not None:
            return True
        else:
            return False
