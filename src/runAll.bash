#!/bin/bash

# Requires glpsol 
# Mudar caso necessario 
# Python script para gerar os arquivos .dat
folder="C:/Users/mateu/Downloads/FACULDADE/1-COMP/6-Periodo/OTIMIZACAO/TP/src"

cd "$folder"/inputs || exit
files=($(ls -1v *.dat))

for file in ${files[@]}; do
    echo "Processing: $file"
    cd "$folder"
    touch out/"$file".terminal
    glpsol --cover --clique --gomory --mir -m modelo.mod -o out/"$file".out --data inputs/"$file" > out/"$file".terminal
done
