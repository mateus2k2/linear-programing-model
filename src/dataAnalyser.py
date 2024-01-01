import os
import GLPKParser as parser
import re

srcFolder = "C:/Users/mateu/Downloads/FACULDADE/1-COMP/6-Periodo/OTIMIZACAO/TP/src"
inputFolder  = srcFolder + "/out"


files = os.listdir(inputFolder)
files = [file for file in files if file.endswith(".dat.out") or file.endswith(".dat.terminal")]
files = [(files[i], files[i+1]) for i in range(files.__len__()-1) if i%2 == 0]
# files = [("modelo.out", "modeloTerminal.out")]

data = []

for outFile, terminalFile in files:
    print(outFile)
    print(terminalFile)
    print()
    
    # Parse nao funciona 
    # Fazer outro?
    # https://stackoverflow.com/questions/54570442/glpk-output-formats
    # out = parser.GLPKOutput(inputFolder + "/" + outFile)
    
    outFileText = open(inputFolder + "/" + outFile, "r").read()
    terminalFileText = open(inputFolder + "/" + terminalFile, "r").read()
    
    time_used_match = re.search(r"Time used:\s+([\d.]+)\s+secs", terminalFileText)
    memory_used_match = re.search(r"Memory used:\s+([\d.]+)\s+Mb", terminalFileText)
    objective_match = re.search(r"Objective:\s+obj = (\d+)", outFileText)
    
    print("time_used_match", time_used_match.group(1))
    print("memory_used_match", memory_used_match.group(1))
    print("objective_match", objective_match.group(1))
    
    print("------------------------------------------------------------")