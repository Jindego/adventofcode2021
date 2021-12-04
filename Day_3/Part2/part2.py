input = open('input.txt').read().splitlines()
input1 = input
input2 = input

def OTWOsearcher(position):
    a="1"
    posCount = 0
    alpha = ''
    negCount = 0
    global input1

    for lines in input1:
        b=list(lines)
        if b[position] == a:
            posCount += 1
        else:
            negCount +=1

    if posCount > negCount or posCount == negCount:
        for lines in input1:
            b=list(lines)
            if b[position] == '1':
                str1=''.join(b)
                if alpha == '':
                    alpha = str1
                else:
                    alpha = alpha + "\n" + str1

    elif negCount > posCount:
        for lines in input1:
            b=list(lines)
            if b[position] == '0':
                str1=''.join(b)
                if alpha == '':
                    alpha = str1
                else:
                    alpha = alpha + "\n" + str1
    
    return alpha

def ScrubberSearcher(position):
    a="1"
    posCount = 0
    beta = ''
    negCount = 0
    global input2

    for lines in input2:
        b=list(lines)
        if b[position] == a:
            posCount += 1
        else:
            negCount +=1

    if posCount > negCount or posCount == negCount:
        for lines in input2:
            b=list(lines)
            if b[position] == '0':
                str1=''.join(b)
                if beta == '':
                    beta = str1
                else:
                    beta = beta + "\n" + str1

    elif negCount > posCount:
        for lines in input2:
            b=list(lines)
            if b[position] == '1':
                str1=''.join(b)
                if beta == '':
                    beta = str1
                else:
                    beta = beta + "\n" + str1
    
    return beta

count1=0
input1clean=""
while len(input1) > 1:
    input1clean=OTWOsearcher(count1)
    input1=OTWOsearcher(count1).splitlines()
    count1+=1
    
print ("Oxygen generator reading = " + input1clean)

count2=0
input2clean=""
while len(input2) > 1:
    input2clean=ScrubberSearcher(count2)
    input2=ScrubberSearcher(count2).splitlines()
    count2+=1

print ("Scrubber generator reading = " + input2clean)

alphaInt=(int(input1clean, 2))
betaInt=(int(input2clean, 2))

print ("The life support rating of the submarine = " + str((alphaInt * betaInt)))