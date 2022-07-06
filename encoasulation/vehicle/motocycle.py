from vehicle import Vehicle

class Motocycle(Vehicle):
    def __init__(self,name,wheels,max,vin) -> None:
        #super().__init__()
        Vehicle.__init__(self,name,wheels,max,vin)

    def set_cc(self,cc):
        self.cc = cc
    def v_detail(self):
        Vehicle.v_detail(self)
        print(f': {self.cc}')
