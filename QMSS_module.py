from selection.__init__ import printSwitch
from random import *
from selection.Selection import partitionDet, recursiveQuickSelectRand, recursiveQuickSelectDet, condOutput

def quickSelectSort(l, select):
    assert type(l) == list, "Error! Not a list"

    recursiveQuickSelectSort(l, 0, len(l) - 1, select)


def recursiveQuickSelectSort(l, left, right, select):

    k = int((left + right) / 2) + 1

    if left >= right:
        return

    if select == 0:
        pivot = sampleMedianSelect(l, left, right, k)
    
    elif select == 1 and not (k <= 0 or k > len(l)):
        pivot = recursiveQuickSelectRand(l, left, right, k)
    
    elif select == 2 and not (k <= 0 or k > len(l)):
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
    #@param l: list 
    #@return pivot: int
    #Si assuma che m sia uguale a 5
    #Costruisco l'insieme V di 5 elementi scelti a caso da l
    
    """
    if left == right:
        return l[left]
    
    vlen = 5        # vlen (o m) va scelto secondo un criterio ancora da definire
    vperno = sampleMedian(l[left : right + 1] , vlen)
    
    # Il resto del codice è analogo a quello del quickSelectRand
    
    perno = partitionDet(l, left, right, vperno)

    posperno = perno + 1
    if posperno == k:
        return l[perno]
    elif posperno > k:
        return sampleMedianSelect(l, left, perno - 1, k)
    else:
        return sampleMedianSelect(l, perno + 1, right, k)
    
def sampleMedian (l, m):  
   
    i = 0
    V = []
    temp = l.copy()

    while i < m and len(temp) != 0:
        lenTemp = len(temp) 
        index = randint(0, lenTemp - 1)
        V.append(temp.pop(index))
        i += 1

    #Effettuo un selection sort sui primi len(V)/2 elementi.
    #L'elemento alla posizione len(V) / 2 elemento sarà il mediano di V
    
    for k in range(0, int(len(V) / 2)):

        min_pos = k
        for j in range(k + 1, len(V)):
            if V[j] < V[min_pos]:
                min_pos = j

        V[min_pos], V[k] = V[k], V[min_pos]  # mette m al posto giusto

    return V[int(len(V) / 2)]

 
