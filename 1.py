

import urllib.request  # the lib that handles the url stuff


url = "https://adventofcode.com/2022/day/1/input.txt"
# data = urllib2.urlopen(url) 
# ct=0
acc =0
winner = -1
with open("input1.txt","r") as f:
    for line in f:
        # print(line.decode('utf-8')) #utf-8 or iso8859-1 or
        if len(line)<= 0 or line=='\n':
            winner = max(acc,winner)
            # ct+=1
            acc=0
        else:
            # print(line)
            acc += int(line)

print(winner)
