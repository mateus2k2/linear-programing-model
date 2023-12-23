import os

# J = numberJobs           10
# I = numberPeriods        9
# T = timeDuration         153
# R = resourceConstraint   151
# p = processingTime       133 84 48 29 152 93 78 7 66 52
# r = resourceConsumption  39 88 32 26 122 135 87 82 151 136
# M = bigM                 1000000



# data;

# set I := 1 2 3;   # Example: Three periods
# set J := 1 2;     # Example: Two jobs

# param p :=        # Example: Processing time for each job
#   1 2
#   2 3;  

# param r :=        # Example: Required resource amount for each job
#   1 5
#   2 8;

# param T := 6;     # Example: Maximum duration of periods
# param R := 15;    # Example: Maximum amount of resource for each period
# param M := 1000;  # Example: A large positive number

# end;



inputFolder  = r"C:\Users\mateu\Downloads\FACULDADE\1-COMP\6-Periodo\OTIMIZACAO\TP\src\data\Original"
outputFolder = r"C:\Users\mateu\Downloads\FACULDADE\1-COMP\6-Periodo\OTIMIZACAO\TP\src\inputs"


files = os.listdir(inputFolder)
files = [file for file in files if file.endswith(".txt")]
# files = [r"sm1.txt"]
files = [file[:-4] for file in files]

parametres = {}

for file in files:
    inputFile = open(inputFolder + "\\" + file + ".txt", "r")
    lines = inputFile.readlines()
    
    parametres["numberJobs"] = int(lines[0])
    parametres["numberPeriods"] = int(lines[1])
    parametres["timeDuration"] = int(lines[2])
    parametres["resourceConstraint"] = int(lines[3])
    parametres["processingTime"] = [int(x) for x in lines[4].split(" ")]
    parametres["resourceConsumption"] = [int(x) for x in lines[5].split(" ")]
    
    inputFile = open(outputFolder + "\\" + file + ".dat", "w+")
    
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
    
    inputFile.write("data;\n\n")
    inputFile.write("set J := "   + tmpJobsSet                            + ";\n")
    inputFile.write("set I := "   + tmpPeriodsSet                         + ";\n")
    
    inputFile.write("\n")
    
    inputFile.write("param p := \n")
    inputFile.write(tmpParamP)

    inputFile.write("\n\n")

    inputFile.write("param r := \n")
    inputFile.write(tmpParamR)
    
    inputFile.write("\n\n")
    
    inputFile.write("param T := "       + str(parametres["timeDuration"])       + ";\n")
    inputFile.write("param R := "       + str(parametres["resourceConstraint"]) + ";\n")
    inputFile.write("param M := 1000000;")
    
    inputFile.write("\n\n")
    
    inputFile.write("end;")