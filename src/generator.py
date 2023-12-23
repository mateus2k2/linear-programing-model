import os


""" 
ARQUIVO .txt ORIGINAL

J = numberJobs           10
I = numberPeriods        9
T = timeDuration         153
R = resourceConstraint   151
p = processingTime       133 84 48 29 152 93 78 7 66 52
r = resourceConsumption  39 88 32 26 122 135 87 82 151 136
M = bigM                 1000000

"""



""" 
ARQUIVO .dat GERADO

data;

set I := 1 2 3;   # Example: Three periods
set J := 1 2;     # Example: Two jobs

param p :=        # Example: Processing time for each job
  1 2
  2 3;  

param r :=        # Example: Required resource amount for each job
  1 5
  2 8;

param T := 6;     # Example: Maximum duration of periods
param R := 15;    # Example: Maximum amount of resource for each period
param M := 1000;  # Example: A large positive number

end; 

"""

srcFolder = "C:/Users/mateu/Downloads/FACULDADE/1-COMP/6-Periodo/OTIMIZACAO/TP/src"
inputFolder  = srcFolder + "/data/Original"
outputFolder = srcFolder + "/inputs"


files = os.listdir(inputFolder)
files = [file for file in files if file.endswith(".txt")]
files = [file[:-4] for file in files]

parametres = {}

for file in files:
    
    # Load txt
    
    inputFile = open(inputFolder + "/" + file + ".txt", "r")
    lines = inputFile.readlines()
    
    parametres["numberJobs"] = int(lines[0])
    parametres["numberPeriods"] = int(lines[1])
    parametres["timeDuration"] = int(lines[2])
    parametres["resourceConstraint"] = int(lines[3])
    parametres["processingTime"] = [int(x) for x in lines[4].split(" ")]
    parametres["resourceConsumption"] = [int(x) for x in lines[5].split(" ")]
    
    outputFile = open(outputFolder + "/" + file + ".dat", "w+")
    
    # Make dat
    
    tmpJobsSet = [str(x) for x in range(1, parametres["numberJobs"] + 1)]
    tmpJobsSet = ' '.join(tmpJobsSet)
    
    tmpPeriodsSet = [str(x) for x in range(1, parametres["numberPeriods"] + 1)]
    tmpPeriodsSet = ' '.join(tmpPeriodsSet)
     
    tmpParamP = [f'    {x} {parametres["processingTime"][x-1]}'  for x in range(1, parametres["numberJobs"] + 1)]
    tmpParamP[len(tmpParamP)-1] = tmpParamP[len(tmpParamP)-1] + ';'
    tmpParamP = '\n'.join(tmpParamP)
    
    tmpParamR = [f'    {x} {parametres["resourceConsumption"][x-1]}'  for x in range(1, parametres["numberJobs"] + 1)]
    tmpParamR[len(tmpParamR)-1] = tmpParamR[len(tmpParamR)-1] + ';'
    tmpParamR = '\n'.join(tmpParamR)
    
    outputFile.write("data;\n\n")
    outputFile.write("set J := "   + tmpJobsSet                            + ";\n")
    outputFile.write("set I := "   + tmpPeriodsSet                         + ";\n")
    
    outputFile.write("\n")
    
    outputFile.write("param p := \n")
    outputFile.write(tmpParamP)

    outputFile.write("\n\n")

    outputFile.write("param r := \n")
    outputFile.write(tmpParamR)
    
    outputFile.write("\n\n")
    
    outputFile.write("param T := "       + str(parametres["timeDuration"])       + ";\n")
    outputFile.write("param R := "       + str(parametres["resourceConstraint"]) + ";\n")
    outputFile.write("param M := 1000000;")
    
    outputFile.write("\n\n")
    
    outputFile.write("end;")