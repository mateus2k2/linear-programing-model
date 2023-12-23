# linear-programing-model

## Comandos

--cover --clique --gomory --mir -m test.mod -o out/test.out
glpsol --check --cover --clique --gomory --mir -m implementacao.mod --data implementacao.dat --wlp implementacao.lp; subl implementacao.lp
glpsol --cover --clique --gomory --mir -m implementacao.mod --data implementacao.dat -o out/implementacao.out; subl out/implementacao.out
python gerador


Sets
i: index for periods {1, 2,..., t}.
j: index for jobs {1, n}.

Params
pj: processing time of job j.
r j: required resource amount for job j.
T: Maximum duration of the periods.
R: Maximum amount of resource for each period.
M: a large positive number.


Variables
Xij
1, if job j is processed in period i,
0, otherwise,

yi
1, if period i is used in a given solution
0, otherwise

wi
1, if it is the period with the longest idle time (maximum slack occurs in period i)
0, Otherwise

z: computes the longest idle time (maximum slack) in the last period.

Minimize
T * Sum{i=1, t}(yi - z)

Subject to
Sum{i=1, t} (xij = 1), ∀j
Sum{i=1, t} (pjxij <= T), ∀i
Sum{i=1, t} (rjxij <= R), ∀i
xij <= yi ∀i, j
Sum{i=1, t} (wi = 1)
wi <= yi ∀i


z <= M(1 − wi) + Tyi − Sum{i=1, t}(pjxij), ∀i

yi >= 0 ∀i
xij ∈ {0, 1}, ∀i, j
wi ∈ {0, 1} ∀i
z >= 0