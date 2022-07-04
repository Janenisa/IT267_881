from country import Country

class Europe(Country):
    def __init__(self, name, pop) -> None:
        super().__init__(name, pop)
        self.__location = ''
        self.__capital = 0

    @property #getter ของ base
    def location(self):
        return self.__location
    
    #setter ของ base
    @location.setter
    def location(self,value):
        self.__location = value

    @property #getter ของ base
    def capital(self):
        return self.__capital
    
    #setter ของ base
    @capital.setter
    def capital(self,value):
        self.__capital = value
    
    def show_detail(self):
        print('==== Europe ====')
        print(f'country : {self.name}')
        print(f'capital : {self.capital}')
        print(f'population : {self.population}')
        print(f'location : {self.location}')

class Asia(Country):
    def __init__(self, name, population) -> None:
        super().__init__(name, population)
        self.__gdp = 0
        
    @property #getter ของ base
    def gdp(self):
        return self.__gdp
    
    #setter ของ base
    @gdp.setter
    def gdp(self,value):
        self.__gdp = value

    def show_detail(self):
        print('==== Asia ====')
        print(f'country : {self.name}')
        print(f'population : {self.population}')
        print(f'gdp : {self.gdp}')