import pandas as pd
file1 = open('input.txt', 'r')
Lines = file1.readlines()


def columnpos(number):
    coltotal=-500
    count=0

    for line in Lines:
        count += 1
        x = line.strip('\n')
        y = list(x)
        coltotal=(int(y[number])+coltotal)

    if coltotal > 0:
        print("Column " + str(number) + ": Most Common - 1, Least Common - 0")
    else:
        print("Column " + str(number) + ": Most Common - 0, Least Common - 1")

columnpos(0)
columnpos(1)
columnpos(2)
columnpos(3)
columnpos(4)
columnpos(5)
columnpos(6)
columnpos(7)
columnpos(8)
columnpos(9)
columnpos(10)
columnpos(11)
