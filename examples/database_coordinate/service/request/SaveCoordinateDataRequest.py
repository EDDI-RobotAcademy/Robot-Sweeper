from dataclasses import dataclass


@dataclass
class SaveCoordinateDataRequest:
    __coordinate_id: int
    __coordinate_data: dict

    def getCoordinateId(self):
        return self.__coordinate_id

    def getCoordinateData(self):
        return self.__coordinate_data
