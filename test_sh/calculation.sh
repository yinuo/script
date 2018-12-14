#!/bin/bash

read -p "Please input on num:" num

sum=0

#${name:=default}使用指定值来代替空的或者没有赋值的变量name
echo ${num:=1}

for ((i=0; i<=num; i++))
do
	let sum+=i
done

echo "sum=$sum"
