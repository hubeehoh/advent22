game = {("A","X"):3,
    ("B","Y"):3,
    ("C","Z"):3,
    # ("A",""):3,
    ("B","X"):0,
    ("C","X"):6,
    ("A","Y"):6,
    # ("B","Y"):0,
    ("C","Y"):0,
    ("A","Z"):0,
    ("B","Z"):6,
    # ("C","Z"):6,
    }
element = {"X":1,"Y":2,"Z":3}

win = {"X":0,"Y":3,"Z":6}

find_strat = lambda a,x: [i for i in win.keys() if game[(a,i)]==win[x]][0]

import pdb
acc = 0
with open("input2.txt","r") as f:
    for line in f:
        line=line.strip()
        try:
            acc += element[find_strat(line[0],line[2])] + win[line[2]]
            
        except:
            pdb.set_trace()
            break
        
print(acc)