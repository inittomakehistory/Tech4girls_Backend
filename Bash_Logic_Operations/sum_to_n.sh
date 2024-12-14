read - p "enter the number:" number sum=0
for i in $( seq 1 $number);
do ((sum +=i))
done
 echo " The sum of numbers from 1 to $number is: $sum"
