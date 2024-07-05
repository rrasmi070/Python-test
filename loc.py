import haversine as hs
from haversine import Unit
loc1=(28.7129818,77.2156933)
loc2=(28.712842, 77.215831)

calculat_mtr = hs.haversine(loc1,loc2,unit=Unit.METERS)
if int(calculat_mtr) > 100:
    print(int(calculat_mtr),'=======')
else:
    print(int(calculat_mtr),'--------kk',calculat_mtr)