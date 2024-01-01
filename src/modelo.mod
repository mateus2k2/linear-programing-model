set I;               # Set of periods
set J;               # Set of jobs


# ----------------------------------------------------------------------------------------------------------------


param p{J};          # Processing time of job j
param r{J};          # Required resource amount for job j
param T;             # Maximum duration of the periods
param R;             # Maximum amount of resource for each period
param M;             # A large positive number


# ----------------------------------------------------------------------------------------------------------------


printf "p[1] = %i /n", p[1];
printf "r[1] = %i /n", r[1];
printf "T = %i /n", T;
printf "R = %i /n", R;
printf "M = %i /n", M;


# ----------------------------------------------------------------------------------------------------------------


var X{I, J} binary;  # 1 if job j is processed in period i, 0 otherwise
var y{I}    binary;  # 1 if period i is used in a given solution, 0 otherwise
var w{I}    binary;  # 1 if it is the period with the longest idle time, 0 otherwise
var z       >= 0  ;  # Computes the longest idle time (maximum slack) in the last period


# ----------------------------------------------------------------------------------------------------------------


minimize obj:
    T * sum{i in I} y[i] - z;


# ----------------------------------------------------------------------------------------------------------------


subject to job_assignment{j in J}:
    sum{i in I} X[i, j] = 1;

subject to time_limit{i in I}:
    sum{j in J} p[j] * X[i, j] <= T;

subject to resource_limit{i in I}:
    sum{j in J} r[j] * X[i, j] <= R;

subject to job_assignment_limit{i in I, j in J}: # VERIFICAR
    X[i, j] <= y[i];

subject to longest_idle_time:
    sum{i in I} w[i] = 1;

subject to longest_idle_time_limit{i in I}:
    w[i] <= y[i];

subject to slack_constraint{i in I}:
    z <= M * (1 - w[i]) + T * (y[i]) - sum{j in J} p[j] * X[i, j];


# ----------------------------------------------------------------------------------------------------------------


# subject to non_negativity_y{i in I}:
#     y[i] >= 0;

# subject to binary_constraints{i in I, j in J}:
#     X[i, j] binary;

# subject to binary_constraints_w{i in I}:
#     w[i] binary;

# subject to non_negativity_z:
#     z >= 0;


# ----------------------------------------------------------------------------------------------------------------

# Data exemplo do Artigo

data;

set J := 1 2 3 4 5;
set I := 1 2 3;

param p := 
    1 2
    2 1
    3 5
    4 4
    5 3;

param r := 
    1 3
    2 3
    3 4
    4 1
    5 1;

param T := 5;
param R := 4;
param M := 1000000;

end;