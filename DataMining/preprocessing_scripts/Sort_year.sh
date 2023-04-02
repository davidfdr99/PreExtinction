#!/bin/bash $1

# Last processing step before the model.
# First argument is path to folder containing 1 file with meteo data

find . -type f -empty -print -delete

mkdir ../parsed_output

for file in $(ls $1)
do

echo $file
tr -d '\r' < $file > temp
mv temp $file

awk -F"	" '{print $10, $1, $2, $3, $4, $5, $6, $7, $8, $9, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30}' OFS="	" $file | sort -g > temp
sed -e "s/\r//g" temp > ../parsed_output/${file}_parsed.tsv # To be tested
cat temp >> ../parsed_output/01-All_Mollusca_parsed.tsv
rm temp

done
