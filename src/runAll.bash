# #!/bin/bash

# # Requires glpsol 
# # Mudar caso necessario 
# # Python script para gerar os arquivos .dat
# folder="C:/Users/mateu/Downloads/FACULDADE/1-COMP/6-Periodo/OTIMIZACAO/TP/src"

# cd "$folder"/inputs || exit
# files=($(ls -1v *.dat))

# for file in ${files[@]}; do
#     echo "Processing: $file"
#     cd "$folder"
#     touch out/"$file".terminal
#     glpsol --cover --clique --gomory --mir -m modelo.mod -o out/"$file".out --data inputs/"$file" > out/"$file".terminal
# done



#!/bin/bash

# Requires glpsol 
# Mudar caso necessario 
# Python script para gerar os arquivos .dat
folder="C:/Users/mateu/Downloads/FACULDADE/1-COMP/6-Periodo/OTIMIZACAO/TP/src"

cd "$folder"/inputs || exit
files=($(ls -1v *.dat))

run_process() {
    local file="$1"
    echo "Processing: $file"
    cd "$folder"
    touch out/"$file".terminal
    glpsol --cover --clique --gomory --mir -m modelo.mod -o out/"$file".out --data inputs/"$file" > out/"$file".terminal &
    echo "Fineshed: $file"
}

max_processes=5
current_processes=0

for file in ${files[@]}; do
    if [ "$current_processes" -ge "$max_processes" ]; then
        wait -n
        ((current_processes--))
    fi

    run_process "$file"
    ((current_processes++))
done

wait
