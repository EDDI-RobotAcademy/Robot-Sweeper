from sqlalchemy.orm import sessionmaker

from work_id_database.entity.WorkIdDatabase import WorkId
from work_id_database.repository.WorkIdDatabaseRepository import WorkIdDatabaseRepository
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

    def save(self, work_id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(work_id)
            session.commit()

            print(f"work_id: {work_id.get_id()}")
            return work_id

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def update(self, work_id: WorkId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        existingWorkId = session.query(WorkId).filter_by(_WorkId__workId=work_id.get_id()).first()
        if existingWorkId:
            existingWorkId.setTempdata(work_id.get_tempdata())
            session.commit()

    def findById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(WorkId).filter_by(_WorkId__id=id).first()

    def findByWorkId(self, work_id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        print(f"WorkIdRepositoryImpl: findByWorkId: {work_id}")
        print(f"WorkIdRepositoryImpl: {session.query(WorkId).filter_by(_WorkId__workId=work_id).all()}")
        print(f"WorkIdRepository: {str(session.query(WorkId).filter_by(_WorkId__workId=work_id).limit(1))}")

        return session.query(WorkId).filter_by(_WorkId__workId=work_id).first()

    def deleteByWorkId(self, work_id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        workId = session.query(WorkId).filter_by(_WorkId__workId=work_id).first()
        if workId:
            session.delete(workId)
            session.commit()

    def deleteById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        workId = session.query(WorkId).filter_by(_WorkId__workId=id).first()
        if workId:
            session.delete(workId)
            session.commit()
            return True
        return False

    def getBoolWithFindById(self, work_id):
        if self.findByWorkId(work_id) is not None:
            return True
        else:
            return False
