class grenade:
    def __init__(self, name, ignition_time, info):
        self.__name          = name
        self.__ignition_time = ignition_time
        self.__info          = info

    @property
    def name(self):
        return self.__name

    @property
    def ignition_time(self):
        return self.__ignition_time

    @property
    def info(self):
        return self.__info

    @property
    def attrib_list(self):
        return [self.__name, self.__ignition_time, self.__info]