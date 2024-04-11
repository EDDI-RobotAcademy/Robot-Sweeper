from sqlalchemy.orm import sessionmaker

from database_work_id.entity.DatabaseWorkId import WorkId
from database_work_id.repository.DatabaseWorkIdRepository import DatabaseWorkIdRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

class DatabaseWorkIdRepositoryImpl(DatabaseWorkIdRepository):
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
        print("DatabaseWorkIdRepositoryImpl: save()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            print("work_id?? ", work_id)
            session.add(work_id)
            session.commit()
            result_id = work_id.get_id()
            print(f"saved_work_id: {result_id}")
            return result_id

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def     findById(self, work_id: int):
        print("DatabaseWorkIdRepositoryImpl: findById()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(WorkId).filter_by(_WorkId__id=work_id).first()

    def deleteById(self, work_id: int):
        print("DatabaseWorkIdRepositoryImpl: deleteById()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        workId = session.query(WorkId).filter_by(_WorkId__id=work_id).first()
        if workId:
            session.delete(workId)
            session.commit()

    def getBoolWithFindById(self, work_id: int):
        print("DatabaseWorkIdRepositoryImpl: getBoolWithFindById()")
        if self.findById(work_id) is not None:
            return True
        else:
            return False
