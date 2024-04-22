from sqlalchemy.orm import sessionmaker
# pip install sqlalchemy

from database_coordinate.entity.CoordinateDatabase import Coordinate
from database_coordinate.repository.DatabaseCoordinateRepository import DatabaseCoordinateRepository
from database_work_id.entity.DatabaseWorkId import WorkId
from database_work_id.repository.DatabaseWorkIdRepositoryImpl import DatabaseWorkIdRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

class DatabaseCoordinateRepositoryImpl(DatabaseCoordinateRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.databaseWorkIdRepository = DatabaseWorkIdRepositoryImpl().getInstance()
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def saveWorkId(self):
        print("DatabaseCoordinateRepositoryImpl: saveWorkId()")
        work_id_data = {
        }
        work_id = WorkId(**work_id_data)
        id = self.databaseWorkIdRepository.save(work_id)
        return id

    def saveCoordinate(self, work_id: int, coordinate_data: Coordinate):
        print("DatabaseCoordinateRepositoryImpl: saveCoordinate()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            coordinateData: Coordinate = {
                'work_id': work_id,
                'X_coordinate': coordinate_data["X_coordinate"],
                'Y_coordinate': coordinate_data["Y_coordinate"],
                'Z_coordinate': coordinate_data["Z_coordinate"],
                'Waypoint_ID': coordinate_data["Waypoint_ID"],
                'Town_Number': coordinate_data["Town_Number"],
            }

            print("coordinateData: ", coordinateData)
            add_coordinate = Coordinate(**coordinateData)
            session.add(add_coordinate)
            session.commit()

            return coordinateData

        except SQLAlchemyError as exception:
            session.rollback()
            print("DB 저장 중 에러 발생: ", exception)
            return None

    def findCoordinate(self, work_id: int):
        print("DatabaseCoordinateRepositoryImpl: findCoordinate()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            find_coordinates = session.query(CoordinateData).filter_by(_WorkId__id=work_id).all()
            result_list: list = []
            for find_coordinate in find_coordinates:
                print("find_coordinate: ", find_coordinate)
                result_list.append(find_coordinate)

            print("result_list: ", result_list)
            return result_list

            # query = f"SELECT * FROM coordinate WHERE work_id = {work_id}"
            # session.execute(query)
            # results = session.fetchall()
            # result_list: list = []
            # for result in results:
            #     print("result: ", result)
            #     result_list.append(result)
            #
            # print("result_list: ", result_list)
            # return result_list

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 호출 중 에러 발생: {exception}")
            return None

    def findCoordinateById(self, work_id: int):
        print("DatabaseWorkIdRepositoryImpl: findById()")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(WorkId).filter_by(_WorkId__id=work_id).first()


