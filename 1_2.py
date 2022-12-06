acc =0
ordered = [0,0,0,0]


with open("input1.txt","r") as f:
    for line in f:
        if len(line)<= 0 or line=='\n':
            ordered[0] = acc
            ordered = sorted(ordered)
            acc=0
        else:
            acc += int(line)

print(sum(ordered[1:]))
