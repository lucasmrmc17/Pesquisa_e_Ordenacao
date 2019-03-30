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
          


def geraListaAleatoria(tam):
    lista = []
    while tam > len(lista):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

x = [10000, 20000, 30000, 40000, 50000]

y = []

for i in x:
  
  lista = geraListaAleatoria(i)
  y.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))

desenhaGrafico(x, y, 'Grafico bubbleSort', 'Gráfico bubbleSort.png')


