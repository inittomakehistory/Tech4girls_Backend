Number1=$2
Number2=$3
if [ $Number1 -gt 10 ] && [ $Number2 -gt 10 ];
then
 echo "Both numbers are greater than 10."
elif [ $Number1 -gt 10 ] || [ $Number2 -gt 10 ];
then
 echo "At least one number is greater than 10."
else 
 echo "Neither number is greater than 10."
fi 
