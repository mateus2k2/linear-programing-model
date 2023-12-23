# Sets
set N;  # Set of jobs

# Parameters
param lambda;  # Scale parameter of the system
param beta;    # Shape parameter of the system

# Additional Parameters
param M;            # A large positive value
param p {N};    # Processing time of job i
param d {N};    # Due date of job i
param TIPM;         # Duration time of an IPM
param TPPM;         # Duration time of a PPM
param TF;           # Penalty time of failure
param theta;        # Improvement factor
param delta;


# Displaying the loaded data
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
	
param TIPM := 2;
param TPPM := 5;
param TF := 10;
param theta := 0.4;
param delta := 0.78;
