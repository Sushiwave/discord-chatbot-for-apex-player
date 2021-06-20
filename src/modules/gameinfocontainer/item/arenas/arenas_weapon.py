class arenas_weapon:
    def __init__(self, name, base_cost, first_upgrade_cost, second_upgrade_cost, third_upgrade_cost, reserve_ammo):
        self.__name                = name
        self.__base_cost           = base_cost
        self.__first_upgrade_cost  = first_upgrade_cost
        self.__second_upgrade_cost = second_upgrade_cost
        self.__third_upgrade_cost  = third_upgrade_cost
        self.__reserve_ammo        = reserve_ammo

    @property
    def name(self):
        return self.__name

    @property
    def base_cost(self):
        return self.__base_cost

    @property
    def first_upgrade_cost(self):
        return self.__first_upgrade_cost

    @property
    def second_upgrade_cost(self):
        return self.__second_upgrade_cost

    @property
    def third_upgrade_cost(self):
        return self.__third_upgrade_cost

    @property
    def reserve_ammo(self):
        return self.__reserve_ammo