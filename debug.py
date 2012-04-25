from itertools import permutations


def trimPossibilities(poss, pegs, nails):
    print poss
    for poss_ans, poss_colors in poss.items():
        print poss
        nails_perm = permutations(nails)
        valid_perm = False
        for perm in nails_perm:
            poss_colors_left = poss_colors.copy()
            black_pegs = [i for i, x in enumerate(perm) if x == 1]
            white_pegs = [i for i, x in enumerate(perm) if x == 0]
            no_pegs = [i for i, x in enumerate(perm) if x == -1]
            poss_perm = True
            print black_pegs, white_pegs, no_pegs
            for b in black_pegs:
                poss_colors_left[pegs[b]] -= 1
                if poss_ans[b] != pegs[b]:
                    poss_perm = False
                    print "broke black_pegs"
                    break
                if not poss_perm: continue
            # 2 problems with white pegs
            # 1: this color not in this position
            for w in white_pegs:
                poss_colors_left[pegs[w]] -= 1
                if poss_ans[w] == pegs[w]:
                    poss_perm = False
                    print "broke white_pegs"
                    break
                if not poss_perm: continue
            # 2: elsewhere
            perm_colors = {x:0 for x in xrange(6)}
            for w in white_pegs:
                perm_colors[pegs[w]] += 1
            for color, num in perm_colors.items():
                if poss_colors[color] < num:
                    print "broke white_pegs"
                    poss_perm = False
            if not poss_perm: continue
            #nothing pegs
            for n in no_pegs:
                if poss_colors_left[pegs[n]] > 0:
                    poss_perm = False
                    print "broke no pegs"
                    break
            if not poss_perm: continue
            #SURVIVED!!
            valid_perm = True
            break
        if not valid_perm: del poss[poss_ans]
    for p in sorted(poss.keys()):
        print [num_to_color[x] for x in p]

poss = {(5, 5, 3, 0): {0:0, 1:0, 2:0, 3:1, 4:0, 5:2}}
pegs = [2, 1, 2, 3]
nails = [0, -1, -1, -1]

print poss, pegs, nails
trimPossibilities(poss, pegs, nails)