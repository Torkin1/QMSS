"""
File name: QMSS_module.py
Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x

QMSS_module contiene le definizioni di:
    
    quickSelectSort(l, select)
    recursiveQuickSelectSort(l, left, right, select)
    sampleMedianSelect(l, left, right, k)
    sampleMedian(l, offset)

"""
from selection.__init__ import printSwitch
from random import randint
from math import ceil
from selection.Selection import partitionDet, recursiveQuickSelectRand, recursiveQuickSelectDet, trivialSelect, quickSelectRand

def quickSelectSort(l, select):
    """
    @param l: list of integers
    @param select: int, { 0 = sampleMedianSelect, 1 = quickSelectRand, 
                          2 = quickSelectDet }
    
    @return None, side effect: calls recursiveQuickSelectSort

    Esegue un quickSort sulla lista l chiamando recursiveQuickSelectSort,
    partizionando attorno a un pivot estrattotramite l'algoritmo di selezione
    indicato da select.

    """
    assert type(l) == list, "Error! Not a list"

    recursiveQuickSelectSort(l, 0, len(l) - 1, select)


def recursiveQuickSelectSort(l, left, right, select):
    """
    @param l: input list of integers
    @param left: int
    @param right: int
    @param select: int

    @return None, side effect: sorts list

    Nucleo ricorsivo di quickSelectSort.

    """
    k = int((left + right) / 2) + 1 
    
    if left >= right:
        return

    elif select == 0:
        pivot = sampleMedianSelect(l, left, right, k)
    
    elif select == 1:
        pivot = recursiveQuickSelectRand(l, left, right, k)
    
    elif select == 2:
        pivot = recursiveQuickSelectDet(l, left, right, k, 10, "QuickSelectDet")

    #print(pivot)
    #print("({},{})".format(left, right))

    pIndex = partitionDet(l, left, right, pivot)
    
    #print(l)

    recursiveQuickSelectSort(l, left, pIndex - 1, select)

    #print("({},{})".format(left, right))
    #print(l)
    
    recursiveQuickSelectSort(l, pIndex + 1, right, select)

    #print("({},{})".format(left, right))
    #print(l)


def sampleMedianSelect(l, left, right, k):
    """
    @param l: list
    @param left: int
    @param right: int
    @param k: int, elemento da estrarre
    @return int

    Estrae l'elemento k dalla lista l, partizionando attorno a un pivot calcolato
    chiamando sampleMedian.

    """
    if left == right:
        return l[left]
    
    lenTuple = ceil(len(l) / 100)
    #lenTuple = 500 if len(l) == 50k
    vperno = sampleMedian(l[left : right + 1] , lenTuple) # m = ceil(int((right - left + 1)/ 5))
    
    #print(f"vperno is {vperno}")
    
    perno = partitionDet(l, left, right, vperno)

    posperno = perno + 1
    if posperno == k:
        return l[perno]
    elif posperno > k:
        return sampleMedianSelect(l, left, perno - 1, k)
    else:
        return sampleMedianSelect(l, perno + 1, right, k)
    
def sampleMedian (l, offset):  
    """
    @param l: list
    @param offset: int, grandezza delle tuple
    
    @return int

    Costruisce un sottinsieme V di l partizionando quest'ultima
    in len(l) / offset tuple, estraendo un elemento a caso da ciascuna tupla e
    inserendolo in V. Se len(V) > 5, ripete ricorsivamente le suddette operazioni,
    altrimenti si calcola il mediano di V e lo restituisce.

    """
    if len(l) <= offset:
        
        return quickSelectRand(l, int(len(l) / 2) + 1)

    else:
        temp = []
        for i in range(0, len(l), offset):
            
            oneTuple = [l[j] for j in range(i, i + offset) if j < len(l)]
       #     print(f"tuple is {oneTuple}")
            temp.append(oneTuple[randint(0, len(oneTuple) - 1)])
       #     print (f"temp is {temp}")
        
        return sampleMedian(temp, offset)
