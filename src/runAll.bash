#!/bin/bash

folder_path="C:\\Users\\mateu\\Downloads\\FACULDADE\\1-COMP\\6-Periodo\\OTIMIZACAO\\TP\\src\\inputs"
cd "$folder_path" || exit
files=($(ls -1v))

skip_first=true

for file in ${files[@]}; do
    if $skip_first; then
        skip_first=false
        continue
    fi

    echo "Processing: $file"
    cd C:\\Users\\mateu\\Downloads\\FACULDADE\\1-COMP\\6-Periodo\\OTIMIZACAO\\TP\\src\\
    touch out/"$file".terminal
    glpsol --cover --clique --gomory --mir -m modelo.mod -o out/"$file".out --data inputs/"$file" > out/"$file".terminal

done
