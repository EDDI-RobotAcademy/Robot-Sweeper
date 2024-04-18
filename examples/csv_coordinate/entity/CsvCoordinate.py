class CsvCoordinate:
    __x_coordinate = None
    __y_coordinate = None
    __z_coordinate = None
    __way_point_id = None
    __town_number = None

    def __init__(self, waypoint_data):
        self.__x_coordinate = waypoint_data[0]
        self.__y_coordinate = waypoint_data[1]
        self.__z_coordinate = waypoint_data[2]
        self.__way_point_id = waypoint_data[3]
        self.__town_number = waypoint_data[4]

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def get_z_coordinate(self):
        return self.__z_coordinate

    def get_way_point_id(self):
        return self.__way_point_id

    def get_town_number(self):
        return self.__town_number
