from database_coordinate.entity.CoordinateDatabase import Coordinate
from database_coordinate.repository.DatabaseCoordinateRepositoryImpl import DatabaseCoordinateRepositoryImpl
from database_coordinate.service.DatabaseCoordinateService import DatabaseCoordinateService
from database_coordinate.service.response.SaveCoordinateDataResponse import SaveCoordinateDataResponse


class DatabaseCoordinateServiceImpl(DatabaseCoordinateService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
            cls.__instance.__databaseCoordinateRepository = DatabaseCoordinateRepositoryImpl.getInstance()

        return cls.__instance


    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def saveCoordinateData(self, *args, **kwargs):
        print("DatabaseCoordinateServiceImpl: saveCoordinateData()")
        print("args: ", args)

        saveCoordinateDataRequest = args[0]
        print("saveCoordinateDataRequest: ", saveCoordinateDataRequest)
        work_id = self.__databaseCoordinateRepository.saveWorkId()
        # print(f"work_id: {work_id}")

        coordinateData = saveCoordinateDataRequest
        # coordinateData.reverse()
        print("coordinateData: ", coordinateData)

        for coordinate in coordinateData:
            print("coordinateData: ", coordinateData)
            coordinateData = {
                'work_id': None,
                'X_coordinate': coordinate["X_coordinate"],
                'Y_coordinate': coordinate["Y_coordinate"],
                'Z_coordinate': coordinate["Z_coordinate"],
                'Waypoint_ID': coordinate["Waypoint_ID"],
                'Town_Number': coordinate["Town_Number"],
            }
            self.__databaseCoordinateRepository.saveCoordinate(work_id, coordinateData)

        print("saveCoordinateData completed")

        return SaveCoordinateDataResponse(True)
