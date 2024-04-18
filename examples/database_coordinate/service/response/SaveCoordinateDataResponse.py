from dataclasses import dataclass


@dataclass
class SaveCoordinateDataResponse:
    __isSuccess: bool
    __message: str

    def __init__(self,  isSuccess: bool, message: str = "save success"):
        self.__isSuccess = isSuccess
        self.__message = message

    def __iter__(self):
        yield "__success", self.__isSuccess
        yield "__message", self.__message
