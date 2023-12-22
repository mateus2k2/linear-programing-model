# Sets
set N;  # Set of jobs

# Parameters
param M;       # A large positive value
param lambda;  # Scale parameter of the system
param beta;    # Shape parameter of the system
param TIPM;    # Duration time of an IPM
param TPPM;    # Duration time of a PPM
param TF;      # Penalty time of failure
param delta;   # Reliability threshold

# Variables
var x{i in N, j in N} binary;  # 1 if job i is processed in position j; 0 otherwise
var y{j in N} binary;          # 1 if an IPM is inserted at the beginning of position j; 0 otherwise
var z{j in N} binary;          # 1 if a PPM is inserted at the beginning of position j; 0 otherwise
var s{j in N} >= 0;            # Start time of the machine in position j
var c{i in N} >= 0;            # Completion time of job i

# Objective
minimize Total_Tardiness:
    sum{i in N} max(c[i] - di, 0);

# Constraints
subject to OneJobPerPosition{j in N}:
    sum{i in N} x[i, j] = 1;

subject to OnePositionPerJob{i in N}:
    sum{j in N} x[i, j] = 1;

subject to StartTimeConstraint{i in N, j in N}:
    s[j + 1] >= x[i, j] * c[i];

subject to CompletionTimeConstraint{i in N, j in N}:
    c[i] + M * (1 - x[i, j]) >= s[j] + pi + TIPM * y[j] + TPPM * z[j] + TF * (lambda * (uf[j]^beta - ub[j]^beta));

subject to MachineAgeConstraint{j in N}:
    ub[j] = uf[j - 1] * (1 - theta * y[j] - z[j]);

subject to ProcessingTimeConstraint{i in N, j in N}:
    uf[j] >= ub[j] + x[i, j] * pi;

subject to ReliabilityConstraint{j in N}:
    R[j] = exp(-lambda * (uf[j]^beta - ub[j]^beta));
    R[j] >= delta;

subject to MaintenanceConstraint{j in N}:
    y[j] + z[j] <= 1;

# Binary Constraints
subject to BinaryConstraints{i in N, j in N}:
    x[i, j] binary;
    y[j] binary;
    z[j] binary;




data;

# Test Data for Single-Machine Scheduling with Maintenance

# Set of jobs
set N := 1 2 3;

# Parameters
param M := 1000;
param lambda := 0.1;
param beta := 2;
param TIPM := 5;
param TPPM := 10;
param TF := 2;
param delta := 0.9;

# Job-specific parameters
param pi :=
    1 20
    2 15
    3 25;

param di :=
    1 50
    2 70
    3 90;

param theta := 0.5;

# Dummy age parameters
param ub :=
    1 0
    2 0
    3 0;

# Execute the AMPL model with the test data
include your_ampl_model_file.mod;  # Replace with the actual filename of your AMPL model
include test_data.dat;

# Solve the model
solve;

# Display the results
display Total_Tardiness;
display x;
display y;
display z;
display s;
display c;
