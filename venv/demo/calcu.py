import mgs,display
from calculator import add
from calculator import mul
import area

mgs.msg_method()
display.display_method()

add(10,20)
a=mul(10,20)
print(a)

areacircle=area.area_circle(5)
print(areacircle)

areaS=area.area_square(5)
print(areaS)