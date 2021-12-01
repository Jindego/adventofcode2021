echo "0" > increase.log

IFS=$'\r\n' GLOBIGNORE='*' command eval  'array=($(cat input.txt))'
totalCount=$(cat input.txt | wc -l)
RunningCount=0
arrayPos2=0

while [[ $RunningCount -le $totalCount ]]
do
    if [[ $RunningCount -ge "3" ]]
    then
        arrayPos1=$(($RunningCount))
        arrayPos2=$(($arrayPos1+1))
        
        i=$(($RunningCount-3))
        while [[ $i != $arrayPos1 ]]
        do
            part1total=$(($part1total+${array[$i]}))
            i=$(($i+1))
        done

        j=$(($arrayPos1-2))
        while [[ $j != $arrayPos2 ]] && [[ $j -le $totalCount ]]
        do
            part2total=$(($part2total+${array[$j]}))
            j=$(($j+1))
        done

        if [[ $part2total -gt $part1total ]]
        then
            curCounter=$(cat increase.log)
            count=$(($curCounter+1)) 
            echo $count > increase.log
        fi

        part1total=0
        part2total=0
        RunningCount=$(($RunningCount+1))
    else
        RunningCount=$(($RunningCount+1))
    fi
done
echo "your answer is $(cat increase.log)"