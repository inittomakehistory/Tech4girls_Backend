read -p "enter Number1:" input1
read -p "enter Number2:" input2
if [ $input1 -gt $input2 ]; then 
 echo "$input1 is greater than $input2"
elif [ $input1 -lt $input2 ]; then
 echo "$input1 is less than $input2"
else
 echo "$input1 and $input2 are equal 
fi
