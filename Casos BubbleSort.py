import timeit
from random import randint
import matplotlib as mpl


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x, y, graphLabel, fileName,xl = "Quantidade de numeros", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = graphLabel)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)

def bubbleSort(arr):
  lenght = len(arr)
  swapped = True
  while swapped:
    swapped = False
    for i in range(lenght):
      for j in range(lenght-i-1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
          swapped = True
          
def GeraListaCrescente(tam):
    lista = []
    i = 0
    while i <= tam:
        lista.append(i)
        i += 1
        
    return lista
    
def GeraListaDecrescente(tam):
    lista = []
    while tam >= 0:
        lista.append(tam)
        tam -= 1
        
    return lista

def GeraListaAleatoria(tam):
    lista = []
    while tam >= len(lista):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)

    return lista

x = [100, 200, 300, 400, 500]

yMelhorCaso = []
yMedioCaso = []
yPiorCaso = []

for i in x:
  lista = GeraListaCrescente(i)
  yMelhorCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))

  lista = GeraListaAleatoria(i)
  yMedioCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))

  lista = GeraListaDecrescente(i)
  yPiorCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))

#desenhaGrafico(x, yMelhorCaso, 'Grafico Melhor Caso', 'Gráfico MelhorCaso.png')
#desenhaGrafico(x, yMedioCaso, 'Grafico Medio Caso', 'Gráfico MedioCaso.png')
#desenhaGrafico(x, yPiorCaso, 'Grafico Pior Caso', 'Gráfico PiorCaso.png')

Nomenclatura = ['Pior caso', 'Medio caso', 'Melhor caso']
casos = [yPiorCaso, yMedioCaso, yMelhorCaso]

desenhaGrafico(x, casos, Nomenclatura, 'Casos.png')


