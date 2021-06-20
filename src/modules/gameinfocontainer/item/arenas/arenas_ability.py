class arenas_ability:
    def __init__(self, name, cost, free_charges, maximum_charges):
        self.__name            = name
        self.__cost            = cost
        self.__free_charges    = free_charges
        self.__maximum_charges = maximum_charges

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost
    
    @property
    def free_charges(self):
        return self.__free_charges

    @property
    def maximum_charges(self):
        return self.__maximum_charges

    @property
    def attribute_list(self):
        return [self.__name, self.__cost, self.__free_charges, self.maximum_charges]