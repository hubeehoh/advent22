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
import pdb
acc = 0
with open("input2.txt","r") as f:
    for line in f:
        line=line.strip()
        try:
            acc += game[(line[0],line[2])] + element[line[2]]
        except:
            # pdb.set_trace()
            print("line:",line,":")
            print(line[0])
            print(line[2])
            break
        
print(acc)