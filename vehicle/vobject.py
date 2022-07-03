#objec bus
from bus import Bus

b1 = Bus("Volvo",4,120,"v123")
b1.set_color("Blue")
b1.set_capacity(34)
b1.v_detail()

#object motocycle
from motocycle import Motocycle

m1 = Motocycle("Honda",2,100,"V345")
m1.set_cc(1200)
m1.v_detail()
m1.set_vin("V256")
m1.v_detail