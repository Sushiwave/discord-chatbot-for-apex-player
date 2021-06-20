class weapon:
    def __init__(self, name, body_damage, head_damage, leg_damage, mag_size, RPM, body_dps, UPS):
        self.__name        = name
        self.__body_damage = body_damage
        self.__head_damage = head_damage
        self.__leg_damage  = leg_damage
        self.__mag_size    = mag_size
        self.__RPM         = RPM
        self.__body_dps    = body_dps
        self.__UPS         = UPS

    @property
    def name(self):
        return self.__name

    @property
    def body_damage(self):
        return self.__body_damage

    @property
    def head_damage(self):
        return self.__head_damage

    @property
    def leg_damage(self):
        return self.__leg_damage

    @property
    def mag_size(self):
        return self.__mag_size

    @property
    def RPM(self):
        return self.__RPM

    @property
    def body_dps(self):
        return self.__body_dps
    
    @property
    def UPS(self):
        return self.__UPS

    @property
    def attrib_list(self):
        return [self.__name, self.__body_damage, self.__head_damage, self.__leg_damage, self.__mag_size, self.__RPM, self.__body_dps, self.__UPS]
    
    