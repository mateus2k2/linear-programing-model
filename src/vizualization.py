import matplotlib.pyplot as plt

# # Dados SM1
# recursoPorPeriodo    = 151
# tempoMaximoPeriodo   = 153
# numeroMaximoPeriodos = 9
# tempoTarefas         = [133, 84, 48, 29, 152, 93, 78, 7, 66, 52]
# recursoTarefas       = [39, 88, 32, 26, 122, 135, 87, 82, 151, 136]
# solucao              = [6,1,1,9,8,3,9,6,4,5] # SOLUCAO DO SM1 DO GUSEK

# Dados Exemplo
recursoPorPeriodo    = 5
tempoMaximoPeriodo   = 4
numeroMaximoPeriodos = 3
tempoTarefas         = [2,1,5,4,3]
recursoTarefas       = [3,3,4,1,1]
solucao              = [1,3,2,3,1] # SOLUCAO DO Exemplo DO GUSEK

# PLOT
fig, ax = plt.subplots()
solucaoClean = [ [] for _ in range(0, numeroMaximoPeriodos) ] 
for i in range(0, len(solucao)):
    for j in range(0, len(solucao)):
        if solucao[j] == i+1:
            solucaoClean[i].append(j)

ticks = []
for i in range(0, tempoMaximoPeriodo * numeroMaximoPeriodos, tempoMaximoPeriodo):
    ax.axvline(x=i, linestyle='dotted', color='gray', alpha=0.5)
    ticks.append(i)


for i, periodo in enumerate(solucaoClean):
    currantPoss = i * tempoMaximoPeriodo
    for tarefa in periodo:
        x = currantPoss
        y = 0
        bar_size = tempoTarefas[tarefa]
        
        ax.barh(y, width=bar_size, left=x, color='blue', alpha=1, edgecolor='black', linewidth=2)
        text_value = f"Tarefa = {tarefa+1} \n Recurso = {recursoTarefas[tarefa]} \n Tempo = {tempoTarefas[tarefa]}"
        text_x = x + bar_size / 2
        text_y = 0
        ax.text(text_x, text_y, text_value, ha='center', va='center', color='white', fontsize=8, fontweight='bold')

        currantPoss += tempoTarefas[tarefa]

ax.text(10, 1, f"Recurso Por Pediodo = {recursoPorPeriodo}", fontsize=12, ha='center', va='center', color='red')


ax.set_ylim(-2, 2)
ax.set_xticks(ticks)
ax.set_yticks([])
plt.gca().spines['top'].set_visible(False)
plt.show()

