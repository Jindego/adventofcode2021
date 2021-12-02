file1 = open('/Users/connor/adventofcode/adventofcode2021-1/Day_2/Part2/input.txt', 'r')
Lines = file1.readlines()

# var defs
horizontalPos=0
depthPos=0
aimPos=0
count = 0


# Strips the newline character
for line in Lines:
    count += 1
    x = line.strip('\n')
    y = x.split(" ")

    if "up" in y:
        upint=int(y[1])
        aimPos=aimPos-upint

    if "down" in y:
        downint=int(y[1])
        aimPos=aimPos+downint
    
    if "forward" in y:
        forwardint=int(y[1])
        horizontalPos=horizontalPos+forwardint
        depthPos=depthPos+(forwardint*aimPos)
        
print ("Horizontal position: " + str(horizontalPos))
print ("Depth position: " + str(depthPos))
print ("Aim position: " + str(aimPos))

finalTotal=horizontalPos*depthPos

print ("Your final answer is: " + str(finalTotal))