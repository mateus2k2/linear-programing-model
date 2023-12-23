set N;  # Set of jobs

# Parameters
param lambda; # Scale parameter of the system
param beta;   # Shape parameter of the system

param M;     # A large positive value
param p {N}; # Processing time of job i
param d {N}; # Due date of job i
param TIPM;  # Duration time of an IPM
param TPPM;  # Duration time of a PPM
param TF;    # Penalty time of failure
param theta; # Improvement factor
param delta; # Reliability threshold

# param T = 0.1
# param R = 0.5

# ----------------------------------------------------------------------------------------------------------------


# Print Paarameters
printf "\nLoaded Data:\n";
printf "lambda: %.2f\n", lambda;
printf "beta: %.2f\n", beta;
printf "theta: %.2f\n", theta;
printf "M: %d\n", M;
printf "p: %s\n", p[1];
printf "d: %s\n", d[1];
printf "TIPM: %.2f\n", TIPM;
printf "TPPM: %.2f\n", TPPM;
printf "TF: %.2f\n", TF;
printf "delta: %.2f\n", delta;


# ----------------------------------------------------------------------------------------------------------------


# Variables
var x{i in N, j in N} binary;         # 1 if job i is processed in position j; 0 otherwise
var y{j in N}         binary;         # 1 if an IPM is inserted at the beginning of position j; 0 otherwise
var z{j in N}         binary;         # 1 if a PPM is inserted at the beginning of position j; 0 otherwise
var s{j in N}         >= 0;           # Start time of the machine in position j
var c{i in N}         >= 0;           # Completion time of job i

var R{j in N}         >= 0, integer;  # Machine reliability after the job in position j is processed
var F{j in N}         >= 0, integer;  # Expected cumulative number of failures at position j

var ub{j in N}        >= 0, integer;  # Example machines dummy age before the job in each position
var uf{j in N}        >= 0, integer;  # Example machines dummy age after the job in each position

var t{i in N}         >= 0, integer; # Auxiliary variable for tardiness


# ----------------------------------------------------------------------------------------------------------------


# Objective
minimize Total_Tardiness:
    sum{i in N} t[i];

# Tardiness constraints
subject to TardinessConstraint{i in N}:
    t[i] >= c[i] - d[i];


# ----------------------------------------------------------------------------------------------------------------


# Constraints
subject to ExpectedFailuresConstraint{j in N}:
    # F[j] = lambda * (uf[j]^beta - ub[1]^beta);
    F[j] = lambda * (uf[j] - ub[1]);

subject to OneJobPerPosition{j in N}:
    sum{i in N} x[i, j] = 1;

subject to OnePositionPerJob{i in N}:
    sum{j in N} x[i, j] = 1;

subject to StartTimeConstraint{i in N, j in N}:
    s[j + 1] >= x[i, j] * c[i];

subject to CompletionTimeConstraint{i in N, j in N}:
    c[i] + M * (1 - x[i, j]) >= s[j] + p[i] + TIPM * y[j] + TPPM * z[j] + TF * (lambda * (uf[j]^beta - ub[j]^beta));

subject to MachineAgeConstraint{j in N}:
    ub[j] = uf[j - 1] * (1 - theta * y[j] - z[j]);

subject to ProcessingTimeConstraint{i in N, j in N}:
    uf[j] >= ub[j] + x[i, j] * p[i];

subject to ReliabilityConstraint{j in N}:
    R[j] = exp(-lambda * (uf[j]^beta - ub[j]^beta));
    R[j] >= delta;

subject to MaintenanceConstraint{j in N}:
    y[j] + z[j] <= 1;


# ----------------------------------------------------------------------------------------------------------------


# Binary Constraints
subject to BinaryConstraints{i in N, j in N}:
    x[i, j] binary;
    y[j] binary;
    z[j] binary;


# ----------------------------------------------------------------------------------------------------------------


data;

# Sets
set N := 1 2 3;

# Parameters
param lambda := 0.000001;
param beta := 3;

# Additional Parameters
param M := 1000;
param p :=
	1 1
	2 2
	3 2;

param d :=
	1 4
	2 5
	3 6;
	
param TIPM   := 2;
param TPPM   := 5;
param TF     := 10;
param theta  := 0.4;
param delta  := 0.78;

# param T = 0.1
# param R = 0.5

# ----------------------------------------------------------------------------------------------------------------
