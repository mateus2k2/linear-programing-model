import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------

# exemplo
# i
numeroMaximoPeriodos = 3
# p
tempoTarefas         = [2,1,5,4,3]
# r 
recursoTarefas       = [3,3,4,1,1]
# T
tempoMaximoPeriodo   = 5 
# R
recursoPorPeriodo    = 4
# solucao
solucao              = [1,3,2,3,1]

# ---------------------------------------------------------------------------

# exemplo Modificado
# i
numeroMaximoPeriodos = 3
# p
tempoTarefas         = [2,1,5,4,3]
# r 
recursoTarefas       = [3,3,4,1,1]
# T
tempoMaximoPeriodo   = 6
# R
recursoPorPeriodo    = 4
# solucao
solucao              = [3,1,2,3,1]

# ---------------------------------------------------------------------------

# sm3
# # i
# numeroMaximoPeriodos = 8
# # p
# tempoTarefas         = [140, 45, 132, 145, 150, 30, 136, 80, 3, 144]   
# # r 
# recursoTarefas       = [91, 95, 60, 60, 170, 102, 36, 33, 160, 165] 
# # T
# tempoMaximoPeriodo   = 188 
# # R
# recursoPorPeriodo    = 170
# # solucao
# solucao              = [3, 4, 6, 7, 8, 7, 1, 4, 5, 2]      

# ---------------------------------------------------------------------------

# # sm14
# # i
# numeroMaximoPeriodos = 17
# # p
# tempoTarefas         = [48, 168, 64, 20, 74, 126, 90, 23, 158, 58, 7, 49, 94, 126, 41, 144, 57, 152, 36, 38]   
# # r 
# recursoTarefas       = [118, 85, 116, 17, 42, 124, 3, 83, 95, 120, 98, 15, 116, 87, 95, 77, 149, 15, 68, 138] 
# # T
# tempoMaximoPeriodo   = 175 
# # R
# recursoPorPeriodo    = 150
# # solucao
# solucao              = []     

# ---------------------------------------------------------------------------

# # sm30
# # i
# numeroMaximoPeriodos = 27
# # p
# tempoTarefas         = [70, 52, 4, 94, 129, 162, 135, 15, 47, 7, 147, 28, 36, 91, 85, 44, 103, 112, 139, 144, 110, 38, 141, 34, 116, 77, 112, 141, 62, 14]   
# # r 
# recursoTarefas       = [37, 166, 48, 4, 53, 5, 125, 181, 154, 93, 107, 78, 156, 71, 19, 26, 158, 79, 114, 5, 180, 34, 83, 3, 80, 175, 41, 7, 167, 165] 
# # T
# tempoMaximoPeriodo   = 165
# # R
# recursoPorPeriodo    = 181
# # solucao
# solucao              = []                        

# ---------------------------------------------------------------------------

# PLOT
fig, ax = plt.subplots()
solucaoClean = [ [] for _ in range(0, numeroMaximoPeriodos) ] 
for i in range(0, len(solucao)):
    for j in range(0, len(solucao)):
        if solucao[j] == i+1:
            solucaoClean[i].append(j)

# ---------------------------------------------------------------------------

#sort periods by the sum of the tasks inside of it
solucaoClean.sort(key=lambda x: sum([tempoTarefas[i] for i in x]), reverse=True)

# ---------------------------------------------------------------------------

ticks = []
for i in range(0, tempoMaximoPeriodo * (numeroMaximoPeriodos+1), tempoMaximoPeriodo):
    ax.axvline(x=i, linestyle='dotted', color='gray', alpha=0.5)
    ticks.append(i)


for i, periodo in enumerate(solucaoClean):
    currantPoss = i * tempoMaximoPeriodo
    
    text_x = currantPoss + tempoMaximoPeriodo / 2
    # ax.text(text_x, 0.5, f"p={i+1}", fontsize=12, ha='center', va='center', color='red')
    
    for j, tarefa in enumerate(periodo):
        x = currantPoss
        y = 0
        bar_size = tempoTarefas[tarefa]
        
        ax.barh(y, width=bar_size, left=x, color='green', alpha=1, edgecolor='black', linewidth=1)
        text_value = f"Tarefa = {tarefa+1} \n Recurso = {recursoTarefas[tarefa]} \n Tempo = {tempoTarefas[tarefa]}"
        text_x = x + bar_size / 2
        text_y = 0
        # ax.text(text_x, text_y, text_value, ha='center', va='center', color='black', fontsize=8, fontweight='bold')

        currantPoss += tempoTarefas[tarefa]
        
        if (j == len(periodo) - 1) and (i == len(solucaoClean) - 1):
            ax.axvline(x=currantPoss, linestyle='dotted', color='red', alpha=0.5)
            ticks.append(currantPoss)
        

x = (numeroMaximoPeriodos * tempoMaximoPeriodo) / 2
ax.text(x, 1, f"Recurso Por Pediodo = {recursoPorPeriodo}", fontsize=12, ha='center', va='center', color='red')

ax.set_ylim(-2, 2)
ax.set_xticks(ticks)
ax.set_yticks([])
plt.gca().spines['top'].set_visible(False)
plt.savefig("img.png", transparent=True, dpi=300)
plt.show()