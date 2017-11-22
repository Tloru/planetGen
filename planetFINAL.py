paLat = 0 # from 0 to 360
paLong = 90 # from 0 to 180

pl1 = [] # 48x*12x plane of heights
pl2 = [] # ^ each one covers 4/6 of the world
pl3 = [] # ^ they're generated with pseudo-random seeded noise

a = [] # top    | pl1[1]+pl2[2]
b = [] # front  | pl1[2]+pl3[4]
c = [] # left   | pl2[3]+pl3[3]
d = [] # back   | pl1[4]+pl3[2]
e = [] # right  | pl2[1]+pl3[1]
f = [] # bottom | pl1[3]+pl2[3]
