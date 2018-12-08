# QSS_module

```
NAME
    QSS_module

DESCRIPTION
    file name: QMSS_module.py
    Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
    Python version: 3.x
    
    QSS_module contiene le definizioni di:
       - quickSelectSort(l, select)
       - recursiveQuickSelectSort(l, left, right, select)
       - sampleMedianSelect(l, left, right, k)
       - sampleMedian(l, offset)

FUNCTIONS
    quickSelectSort(l, select)
        @param l: list of integers
        @param select: int, { 0 = sampleMedianSelect, 1 = quickSelectRand,
                              2 = quickSelectDet }
        @return None, side effect: calls recursiveQuickSelectSort
        Esegue un quickSort sulla lista l chiamando recursiveQuickSelectSort,
        partizionando attorno a un pivot estrattotramite l'algoritmo di selezione
        indicato da select.
    
    recursiveQuickSelectSort(l, left, right, select)
        @param l: input list of integers
        @param left: int
        @param right: int
        @param select: int
        @return None, side effect: sorts list
        Nucleo ricorsivo di quickSelectSort.
    
    sampleMedian(l, offset)
        @param l: list
        @param offset: int, grandezza delle tuple
        @return int
        Costruisce un sottinsieme V di l partizionando quest'ultima
        in len(l) / offset tuple, estraendo un elemento a caso da ciascuna tupla e
        inserendolo in V. Se len(V) > 5, ripete ricorsivamente le suddette operazioni,
        altrimenti si calcola il mediano di V e lo restituisce.
    
    sampleMedianSelect(l, left, right, k)
        @param l: list
        @param left: int
        @param right: int
        @param k: int, elemento da estrarre
        @return int
        Estrae l'elemento k dalla lista l, partizionando attorno a un pivot calcolato
        chiamando sampleMedian.
```
