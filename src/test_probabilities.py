from aspects.store import board
from aspects.board import Board
from aspects.player import Player
import time

start = time.time()
b = Board(log=False)
p = Player(b)
position_store = {}
iterations = 1000000
for _ in range(iterations):
    p.play()
    pos = str(p.position)
    if len(pos) == 1:
        pos = "0" + pos
    pos = pos + ". " + board[p.position]
    if pos in position_store.keys():
        position_store[pos] += 1
    else:
        position_store[pos] = 1

for key in sorted(position_store):
    print("%s: %s%%" % (key, position_store[key] * 100/iterations))

print("\nCompleted in %s s" % str(round(time.time() - start, 2)))