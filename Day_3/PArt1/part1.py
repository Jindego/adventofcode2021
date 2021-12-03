file1 = open('input.txt', 'r')
Lines = file1.readlines()
alpha=""
beta=""

def columnpos(number):
    coltotal=-500
    count=0
    global alpha
    global beta

    for line in Lines:
        count += 1
        x = line.strip('\n')
        y = list(x)
        coltotal=(int(y[number])+coltotal)

    if coltotal > 0:
        alpha = alpha + "1"
        beta = beta + "0"
    else:
        alpha = alpha + "0"
        beta = beta + "1"

i=0
while i < 12:
    columnpos(i)
    i += 1

alphaInt=(int(alpha, 2))
betaInt=(int(beta, 2))

print ("Your Final answer is: " + str((alphaInt * betaInt)))