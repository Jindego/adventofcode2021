input = open('input.txt').read().split(",")

totalDays=80
StartDate=0

while StartDate < totalDays:
    alpha =''
    for ec in input:
        ec=int(ec)
        if ec > 0:
            ec-=1
            alpha=alpha + str(ec)
        else:
            ec=6
            alpha=alpha + str(ec)
            alpha=alpha + '8'
    StartDate+=1
    input=alpha

print(len(input))