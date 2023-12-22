# quantidade de clientes
param n, integer, > 0;
# quantidade de tipos de caminhao
param nt, integer, > 0;

param Prelease, > 0;
param Bet, > 0;
param Alp, > 0;

/* PROPRIEDADES DO GRAFO QUE DESCREVE A REDE  DOS CLIENTES */

#  conjunto dos clientes
set C := {1..n};

# conjunto dos vertices do grafo que representam os clientes e o vertice 0 é o deposito
set N := {0..n};

# demanda de cada cliente
param d{i in N};            

# conjunto dos arcos entre os vertices que representam rotas entre dois clientes
set A, within N cross N;

# verifica se nao tem nenhum arco com origem e destino iguais
check{(i,j) in A}: i != j;

# comprimento do arco (distancia entre os clientes i j)
param al{(i,j) in A};

# custo para se transportar no arco
param c{(i,j) in A};

# numero de pessoas expostas como consequencia de um acidente com liberação de HazMat em cada rota i j
param PD{(i,j) in A};

# ADICIONADO: probabilidade de acontecer um acidente no trajeto i j
param P{(i,j) in A};

/* PROPRIEDADES DE TIPOS DE CAMINHAO */

# conjunto dos nt tipos caminhao
set K := {1..nt};

# capacidade maxima de cada tipo caminhao
param Q{k in K};

# custo fixo de cada tipo de caminhao
param f{k in K};

# taxa de acidentes com cada tipo de caminhao
param TTAR{k in K};

/* VARIAVEIS DE DECISAO */

# fluxo de bens no trecho i j transportados por veiculos do tipo k 
var y{i in N, j in N, k in K} >=0;

# 1 se um veiculo do tipo k passa por i j. 0 caso contrario
var x{i in N, j in N, k in K} binary;

/* FUNCAO OBJETIVO */
minimize z : sum{k in K} sum{(i,j) in A} (al[i,j] * (TTAR[k] * P[i,j]) * y[i,j,k] + PD[i,j]);

/* RESTRICOES */
subject to

# garante que cada cliente seja visitado exatamente uma vez
r1 {j in C}: sum{k in K} sum{i in N} x[i,j,k] = 1; 

# conservacao de fluxo
r2 {k in K, j in C}: sum{i in N} x[i,j,k] - 
                     sum{i in N} x[j,i,k] = 0; 

# satisfacao de demanda
r3 {j in C}: sum{k in K} sum{i in N} y[i,j,k] - 
             sum{k in K} sum{i in N} y[j,i,k] = d[j]; 

# nao deve ser tranportado nenhum bem entre i j se nao existe nenhum tipo de caminhao operando nesse arco
r4 {(i,j) in A}: sum{k in K} x[i,j,k]*d[j] <= 
                 sum{k in K} y[i,j,k]; 

# garante o limite de carga de cada tipo de caminhao
r5 {(i,j) in A, k in K}: y[i,j,k] <= x[i,j,k]*(Q[k]-d[i]);

solve;
