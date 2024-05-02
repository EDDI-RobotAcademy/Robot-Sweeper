class WorkId:
    __work_id = None
    __temp_work_id = None

    def __init__(self, work_id, temp_work_id):
        self.__work_id = work_id
        self.__temp_work_id = temp_work_id

    def get_work_id(self):
        return self.__work_id

    def get_temp_work_id(self):
        return self.__temp_work_id
