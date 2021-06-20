class season:
    def __init__(self, name, season_number, duration, new_legend, new_weapon, featured_map):
            self.__name          = name
            self.__season_number = season_number
            self.__duration      = duration
            self.__new_legend    = new_legend
            self.__new_weapon    = new_weapon
            self.__featured_map  = featured_map

    @property
    def name(self):
        return self.__name

    @property
    def season_number(self):
        return self.__season_number

    @property
    def duration(self):
        return self.__duration
    
    @property
    def new_legend(self):
        return self.__new_legend
    
    @property
    def new_weapon(self):
        return self.__new_weapon
    
    @property
    def featured_map(self):
        return self.__featured_map
