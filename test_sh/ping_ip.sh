#!/bin/bash

net=192.168.1
max=100
Log=~/zl/script/test_sh/log

# seq 用于产生某个数到另外一个数之间的所有整数
for i in $(seq 1 $max)
do
  #echo $i
  ping -c 2 -i 0.2 -w 0.2 $net.$i &> $Log

  if [ $? -eq 0 ];then
  	echo "This host $net.$i , ping success!"
  else
  	echo "This host $net.$i , ping failed!"
  fi
done
