import sys
from itertools import permutations, product

# Input
# colors = BWRYGB
# number = 012345
#
# Output
# black peg = 1
# white peg = 0
# nothing   = -1

# build dict of possiblities

#poss = {}

# for i in xrange(6):
#    for j in xrange(6):
#         for l in xrange(6):
#             for k in xrange(6):
#                 poss[(i, j, k, l)] = {x:0 for x in xrange(6)}
#                 poss[(i, j, k, l)][i] += 1
#                 poss[(i, j, k, l)][j] += 1
#                 poss[(i, j, k, l)][k] += 1
#                 poss[(i, j, k, l)][l] += 1


#color_to_num = {"b": 0, "w": 1, "r": 2, "y": 3, "g": 4, "bu": 5}
#num_to_color = {0: "b", 1: "w", 2: "r", 3: "y", 4: "g", 5: "bu"}

def constructInitialPossibilities(num_colors, num_pegs):
    # generate tuples, see Art of Computer Programming Vol 4
    color_tuples = product(*[range(b) for b in [num_colors]*num_pegs])
    possibilities = {}
    for possibility in color_tuples:
        possibilities[possibility] = {x:0 for x in xrange(num_colors)}
        for color in possibility:
            possibilities[possibility][color] += 1
    return possibilities

def readPegs(color_to_num):
    line_in = sys.stdin.readline()
    line_split = line_in.split()
    pegs = [color_to_num[x] for x in line_split]
    return pegs

def readNails(num_pegs):
    # line = B W
    # B = number of black pegs
    # W = number of white pegs
    line = sys.stdin.readline()
    line_split = [int(x) for x in line.split()]
    num_nail_types = len(line_split)
    if num_nail_types > 0: b = line_split[0]
    else: b = 0
    if num_nail_types > 1: w = line_split[1]
    else: w = 0
    n = num_pegs - b - w
    nails = [1] * b
    nails.extend([0] * w)
    nails.extend([-1] * n)
    print "black:", b, "white:", w, "none", n
    print nails
    return nails

def trimPossibilities(poss, pegs, nails):
    for poss_ans, poss_colors in poss.items():
        nails_perm = permutations(nails)
        valid_perm = False
        for perm in nails_perm:
            poss_colors_left = poss_colors.copy()
            black_pegs = [i for i, x in enumerate(perm) if x == 1]
            white_pegs = [i for i, x in enumerate(perm) if x == 0]
            no_pegs = [i for i, x in enumerate(perm) if x == -1]
            poss_perm = True
            for b in black_pegs:
                poss_colors_left[pegs[b]] -= 1
                if poss_ans[b] != pegs[b]:
                    poss_perm = False
                    break
                if not poss_perm: continue
            # 2 problems with white pegs
            # 1: this color not in this position
            for w in white_pegs:
                poss_colors_left[pegs[w]] -= 1
                if poss_ans[w] == pegs[w]:
                    poss_perm = False
                    break
            if not poss_perm: continue
            # 2: elsewhere
            perm_colors = {x:0 for x in xrange(6)}
            for w in white_pegs:
                perm_colors[pegs[w]] += 1
            for color, num in perm_colors.items():
                if poss_colors[color] < num: poss_perm = False
            if not poss_perm: continue
            #nothing pegs
            for n in no_pegs:
                if poss_colors_left[pegs[n]] > 0:
                    poss_perm = False
                    break
            if not poss_perm: continue
            #SURVIVED!!
            valid_perm = True
            break
        if not valid_perm: del poss[poss_ans]
    for p in sorted(poss.keys()): print [num_to_color[x] for x in p]
                   

sys.stdout.write("Default colors? ")
default_colors = sys.stdin.readline()
colors = []
if default_colors.strip() == "y":
    colors.extend(["black", "white", "red", "yellow", "green", "blue"])
else:
    sys.stdout.write("Tell me the colors (separated by spaces): ")
    colors_line = sys.stdin.readline()
    colors.extend(colors_line.split())

color_to_num = {c:n for n,c in enumerate(colors)}
num_to_color = {n:c for n,c in enumerate(colors)}

sys.stdout.write("Input: ")
pegs = readPegs(color_to_num)
num_colors = len(colors)
num_pegs = len(pegs)
poss = constructInitialPossibilities(num_colors, num_pegs)
sys.stdout.write("Output: ")
nails = readNails(num_pegs)
trimPossibilities(poss, pegs, nails)
print "Number of possibilities: ", len(poss)

while len(poss) > 1:
    sys.stdout.write("Input: ")
    pegs = readPegs(color_to_num)
    sys.stdout.write("Output: ")
    nails = readNails(num_pegs)
    trimPossibilities(poss, pegs, nails)
    print "Number of possibilities: ", len(poss)
            







    
                



                    
                    
                    
        
    
    
    
