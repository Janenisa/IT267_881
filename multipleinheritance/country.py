from geographic import Geographic
from temperature import Temperature

#คือ import 2 ตัว Class เลยต้องมี ,คั่น เพราะเอามาสองอัน
class Country(Geographic,Temperature): 
    def __init__(self,name,area,pop) -> None: #pop คือ population
        super().__init__() #ใช้super
        Geographic. __init__(self) #เราใช้ init
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density(self):
        return self.population / self.area

    def show_detail(self): 
        #ชื่อประเทศ
        print(f'County: {self.name}')
        #สถานที่ตััง latitude และ longgitude
        print(self.getcordinate())
        #แสดงขนาดพื้นที่ จำนวนประชากร ความหนาแน่น
        print(f'Area: {self.area}')
        print(f'Population : {self.population} Million')
        print(f'Density : {self.getpopulation_density()}')
        #Time Zone, Climate, Temperature, weather
        print(f'Time: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperature(C): {self.setcelsius}')
        print(f'Temperature(F): {self.getfahrenheit}')
        print(f'Weater: {self.getweather()}')
        print()
