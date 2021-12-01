#set -x
for el in `cat input.txt`
do
if [[ $elp == '' ]]
then
    elp=$el
    echo "0" > increase.log
else
    if [[ $el -gt $elp ]]
    then
        curCounter=$(cat increase.log)
        count=$(($curCounter+1)) 
        echo $count > increase.log
        elp=$el
    else
        elp=$el
    fi
fi
done
echo "your answer is $(cat increase.log)"