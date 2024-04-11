from dataclasses import dataclass
from sqlalchemy import Column, Integer, DECIMAL, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Coordinate(Base):
    __tablename__ = "coordinate"

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __work_id: int = Column(Integer, name="work_id")
    __X_coordinate: DECIMAL = Column(DECIMAL(22, 15), name="X_coordinate")
    __Y_coordinate: DECIMAL = Column(DECIMAL(22, 15), name="Y_coordinate")
    __Z_coordinate: DECIMAL = Column(DECIMAL(22, 15), name="Z_coordinate")
    __Waypoint_ID: str = Column(String(255), name="Waypoint_ID")
    __Town_Number: str = Column(String(255), default='Town03', name="Town_Number")

    def __init__(self, work_id: int, X_coordinate: DECIMAL(22, 15),
                 Y_coordinate: DECIMAL(22, 15),
                 Z_coordinate: DECIMAL(22, 15),
                 Waypoint_ID: str, Town_Number: str):
        self.__work_id = work_id
        self.__X_coordinate = X_coordinate
        self.__Y_coordinate = Y_coordinate
        self.__Z_coordinate = Z_coordinate
        self.__Waypoint_ID = Waypoint_ID
        self.__Town_Number = Town_Number

    def get_id(self):
        return self.__id

    def get_workId(self):
        return self.__work_id

    def get_xCoordinate(self):
        return self.__X_coordinate

    def get_yCoordinate(self):
        return self.__Y_coordinate

    def get_zCoordinate(self):
        return self.__Z_coordinate

    def get_wayPointId(self):
        return self.__Waypoint_ID

    def get_townNumber(self):
        return self.__Town_Number
