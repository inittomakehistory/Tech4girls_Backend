read -p "enter your age:" age
if [ $age -le 18 ]; then
 echo "You are a minor."
elif [ $age -ge 18 ] && [ $ age - lt 64 ];then
 echo "You are an adult."
else
 echo " You are a senior"
fi
