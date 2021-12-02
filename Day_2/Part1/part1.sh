function getValuesThenAdd() {
export $1=$(grep -i $1 input.txt | awk -F ' ' '{print $2}' | xargs | tr -s ' ' '+')
export $1=$(($1))
}

function depth() {
export depthTotal=$(($1-$2))
}

function HorizonTimesDepth() {
export finalTotal="$(echo "$1 * $2" | bc -l )"
}

getValuesThenAdd forward
getValuesThenAdd down
getValuesThenAdd up

depth $down $up

HorizonTimesDepth $depthTotal $forward

echo "Your answer is $finalTotal"