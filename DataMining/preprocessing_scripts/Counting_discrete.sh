#!/bin/bash

headers=$(head -1 Subset_Columns_Mollusca.tsv)

for i in $(seq 5)
do
	hi=$(echo $headers | cut -d" " -f${i})
	echo $hi
	tail -n +2 Subset_Columns_Mollusca.tsv | cut -d"	" -f${i} | sort -g | uniq > Counting/Col${hi}.list
	paste Counting/Col${hi}.list Counting/Count${hi}.list
done
