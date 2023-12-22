# coding=UTF-8

import sys
# import os
from random import uniform
from random import randint

def gera_header(n, nt, file, Prelease=0.02487845, Alp=0.72, Bet=0.00027):
    output = []
    output.append("data;\n\n")
    output.append("param n := " + str(n) + ";\n")
    output.append("param nt := " + str(nt) + ";\n")
    output.append("param Prelease := " + str(Prelease) + ";\n")
    output.append("param Alp := " + str(Alp) + ";\n")
    output.append("param Bet := " + str(Bet) + ";\n\n")
    
    file.writelines(output)

def gera_demandas(n_clientes, file):
    output = []
    output.append("param d :=")
    output.append("\n\t0\t0")
    for i in range(1,n_clientes+1):
        demanda_i = randint(50,100)
        output.append("\n\t"+str(i)+"\t"+str(demanda_i))
    output.append(";\n\n")

    file.writelines(output)

def gera_grafo(n_clientes, file):
    output = []
    output.append("param: A : al, c, PD, P :=")

    n_clientes += 1
    for i in range(0,n_clientes):
        for j in range(0,n_clientes):
            if i == j: continue
            output.append("\n\t"+str(i)+" "+str(j)+"\t\t")
            al = round(uniform(5,50),2)
            c = round(uniform(10,50),2)
            PD = randint(100,500)
            P =  round(uniform(0,1),3)
            out_aux='{:<6s} {:<6} {:<4} {:<5}'.format(str(al),str(c),str(PD), str(P))
            output.append(out_aux)
    output.append(";\n\n")

    file.writelines(output)

def gera_grafo1(n_clientes, file):
    output = []
    output.append("param: A : al, c, PD, P :=")

    n_clientes += 1
    for i in range(0,n_clientes):
        for j in range(0,n_clientes):
            if i == j or i > j: continue
            al = round(uniform(5,50),2)
            c = round(uniform(10,50),2)
            PD = randint(100,500)
            P =  round(uniform(0,1),3)
            out_aux='{:<6s} {:<6} {:<4} {:<5}'.format(str(al),str(c),str(PD), str(P))
            output.append("\n\t"+str(i)+" "+str(j)+"\t\t")
            output.append(out_aux)
            output.append("\n\t"+str(j)+" "+str(i)+"\t\t")
            output.append(out_aux)
    output.append(";\n\n")

    file.writelines(output)

def gera_info_caminhoes(n_tipos, file):
    output = []

    output.append("param Q :=")
    for i in range(1,n_tipos+1):
        Q = randint(100,500)
        output.append("\n\t"+str(i)+"\t"+str(Q))
    output.append(";\n\n")

    output.append("param TTAR :=")
    for i in range(1,n_tipos+1):
        TTAR = round(uniform(0,1),2)
        output.append("\n\t"+str(i)+"\t"+str(TTAR))
    output.append(";\n\n")

    output.append("param f :=")
    for i in range(1,n_tipos+1):
        f = randint(10,50)
        output.append("\n\t"+str(i)+"\t"+str(f))
    output.append(";\n\n")

    file.writelines(output)


nome_file = sys.argv[1]
output_file = open(nome_file, 'w')

n_clientes = int(sys.argv[2])
n_tipos = int(sys.argv[3])

gera_header(n_clientes,n_tipos,output_file)
gera_demandas(n_clientes, output_file)
gera_grafo1(n_clientes,output_file)
gera_info_caminhoes(n_tipos,output_file)

