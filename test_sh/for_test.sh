#!/bin/bash

max=10

for i in a b c
do
	echo $i
done

for j in $(seq 1 3 $max)
do
	echo $j
done

for ((k=0; k<10; k++))
do
	echo $k
done
