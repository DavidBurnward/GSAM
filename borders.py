import tile
from units import chunk_size
from pics import rock

wall1 = []
wall2 = []
wall3 = []
wall4 = []

Len_wall = chunk_size-1

for i in xrange(Len_wall):
    wall1.append(tile.tile(i,0,rock,True))

for i in xrange(Len_wall):
    wall2.append(tile.tile(0,i+1,rock,True))

for i in xrange(Len_wall):
    wall3.append(tile.tile(i+1, Len_wall, rock, True))

for i in xrange(Len_wall):
    wall4.append(tile.tile(Len_wall, i, rock, True))
