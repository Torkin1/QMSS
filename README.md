La presente repository contiene i file relativi allo svolgimento della seconda traccia della prova pratica:

Profiler.py:
Il codice si presenta con lo script principale, Profiler.py, dove vengono passati in input, grazie al modulo 
argparse ed ai suoi metodi, il numero di elementi presenti all’interno della lista e, in maniera facoltativa,
quale algoritmo tra il QuickSort con sampleMedianSelect (-m), con select randomizzato (-r) o con select 
deterministico (-d) si vuole venga eseguito. Si è scelto di implementare il modulo argparse per facilitare 
l’inserimento dei dati con l’utilizzo del metodo add_argument.
In questo file vengono eseguiti anche tutti gli altri algoritmi di ordinamento che devono essere confrontati con 
le nuovi versione del QuickSort grazie al modulo cProfile, che scrive in un file in un formato proprio i tempi di 
esecuzione delle funzioni. Il modulo pStats, invece, consente di leggere ciò che è presente all’interno di questo 
file e stampa a schermo il suo contenuto.

QSS_module.py:
Lo scopo di questo modulo è quello di eseguire le varianti dell’algoritmo di ordinamento QuickSort in cui la scelta
del pivot avviene tramite algoritmi di selezione. Si è scelto di implementare una funzione quickSelectSort, che prende
in input una lista ed un parametro che indica quale tra gli algoritmi di selezione dovrà essere eseguito. Questa funzione
richiama a sua volta la funzione recursiveQuickSelectSort che, a differenza della prima, prende in più in input due 
parametriche indicano l’inizio e la fine della lista, estrae il pivot con l’algoritmo di selezione scelto, crea la 
partizione ed infine, ricorsivamente, risolve lo stesso problema nelle sottoliste. 

Nelle cartelle selection, sorting e strutture sono presenti i moduli d’appoggio richiamati all’interno di profiler.py
e di QSS_module.py. 
