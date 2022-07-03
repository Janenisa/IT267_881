class Vehicle:
    def __init__(self,name,wheels,max_speed,vin) -> None: #wheelคือหมายเลขเครื่อง
        self.name = name
        self.wheels = wheels
        self._max_speed = max_speed
        self.__vin = vin
    
    def set_vin(self,vin):
        self.__vin = vin  #เพราะเป็น private เลยต้องใช้

    def v_detail(self): # detail ไว้กำหนดค่า print
        print("=====================")
        print (f'name: {self.name}')
        print("=====================")
        print (f'wheels : {self.wheels}')
        print (f'max_speed : {self._max_speed}') 
        print (f'vin: {self.__vin}')

