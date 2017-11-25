from random import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pandas import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ds = SupervisedDataSet(4, 2)

ds.addSample((0.9, 0.8, 0.7, 0.9),(0.5 , 0.4))
ds.addSample((0.29, 0.1, 0.2, 0.9),(0.32 , 0.1))
ds.addSample((0.4, 0.2, 0.98, 0.2),(0.45 , 0.7))



nn = buildNetwork(4, 4, 2, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in xrange(2000):
	treinamento = trainer.train()

erro = treinamento*100

print "Erro associado ao treinamento: " + str(erro)

def mutacao(individuo, taxa_mutacao):
  novoIndividuo = []
  decisao = randint(1,10)
  taxa = taxa_mutacao * 10
  # Aqui vai ocorrer a mutacao
  if taxa <= decisao:
    tamanho = len(individuo)
    indiceSorteado = randint(0, tamanho)
    direcao = randint (0, 1)
    for i in range(tamanho):
      if i != indiceSorteado:
        novoIndividuo.append(individuo[i])
      else:
        if direcao == 0:
          novoIndividuo.append(individuo[i] + 0.05)
        else:
          novoIndividuo.append(individuo[i] - 0.05)
          
    return novoIndividuo
  else:
    return individuo

def fitting(individuo):
  fit = 0
  for i in range(len(individuo)):
    temp = individuo[i] * 0.025 * i 
    fit = fit + temp
  return fit
  
  
def neural_fitting(individuo):
  fit = nn.activate(individuo)
  return sum(fit)

def gera_individuo(dimensao):
  individuo = []
  for i in range(dimensao):    
    atributo = uniform(0, 1)
    individuo.append(atributo)
  return individuo

def gera_populacao(tamanho, dimensao):
    populacao = []
    for i in range(tamanho):
        individuo = gera_individuo(dimensao)
        populacao.append(individuo)

    return populacao

fitting_populacao = []
populacao = gera_populacao(2, 4)
melhor_fitness = 0
melhor_individuo = []
contador = 0

while True:
    
    # Aplica o fitness a todos da populacao
    for i in range(len(populacao)):
        temp = neural_fitting(populacao[i])
        # Captura o melhor fitness
        if (temp > melhor_fitness):
            melhor_fitness = temp
            melhor_individuo = populacao[i]
        fitting_populacao.append(temp)

    #aplica mutacao na populacao
    for i in range(len(populacao)):
        temp = mutacao(populacao[i], 0.2)
        populacao[i] = temp
        
    contador = contador + 1

    if (melhor_fitness > 2):
        print "Quantidade de geracoes: " + str(contador)
        print "Melhor individuo: " + str(melhor_individuo)
        print "Melhor fitness: " + str(melhor_fitness)
        break


#fig, ax = plt.subplots(1, 1)
#ax.hist(np.random.randn(10))
#fig.savefig('display.svg') # Any filename will do


plt.rcdefaults()
fig, ax = plt.subplots()

people = ('#1', '#2', '#3', '#4', 'Fitness')
y_pos = np.arange(len(people))
performance = melhor_individuo
performance.append(melhor_fitness)

print performance
error = np.random.rand(len(people))

p1 = ax.barh(y_pos, performance, align='center',
        color='#60A0D0', ecolor='black')
        
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Valores dos Atributos')
ax.set_title('Otimizador Genetico')

fig.savefig('display.svg') # Any filename will do