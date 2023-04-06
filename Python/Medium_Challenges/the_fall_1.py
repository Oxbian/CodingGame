import sys

DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

pieces = {
    0:[],
    1:{'TOP':DOWN, 'LEFT':DOWN, 'RIGHT':DOWN},
    2:{'LEFT':RIGHT,'RIGHT':LEFT},
    3:{'TOP':DOWN},
    4:{'TOP':LEFT,'RIGHT':DOWN},
    5:{'TOP':RIGHT,'LEFT':DOWN},
    6:{'LEFT':RIGHT,'RIGHT':LEFT},
    7:{'TOP':DOWN,'RIGHT':DOWN},
    8:{'LEFT':DOWN,'RIGHT':DOWN},
    9:{'LEFT':DOWN,'TOP':DOWN},
    10:{'TOP':LEFT},
    11:{'TOP':RIGHT},
    12:{'RIGHT':DOWN},
    13:{'LEFT':DOWN}
}
# w: number of columns.
# h: number of rows.
circuit = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    circuit.append([int(x) for x in input().split()])

print(circuit, file=sys.stderr, flush=True)  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]
    print(pieces[circuit[yi][xi]], file=sys.stderr, flush = True)
    print(pos, file=sys.stderr, flush = True)
    deltaX, deltaY = pieces[circuit[yi][xi]][pos]
    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(xi+deltaX, yi+deltaY)
