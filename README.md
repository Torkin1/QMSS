# QSS - QuickSelectionSort

La repository contiene i file relativi allo svolgimento della seconda traccia della prova pratica.

Maggiori informazioni su scelte implementative, raccolta dati e in generale del lavoro svolto sono disponibili nel file ``documentazione.pdf``.

**Profiler.py:**

Il codice si presenta con lo script principale, ``profiler.py``, dove vengono passati in input, grazie al modulo 
``argparse`` ed ai suoi metodi, il numero di elementi presenti all’interno della lista, il range di rappresentazione e gli algoritmi di cui si vuole effetuare il profiling. Si è scelto di implementare il modulo argparse per facilitare l’inserimento dei dati con l’utilizzo del metodo add_argument.
Tale lavoro di profiling è reso disponibile grazie all'implementazione del modulo ``cProfile``, che scrive in un file in un formato proprio i tempi di esecuzione delle funzioni. Il modulo ``pStats``, invece, consente di leggere ciò che è presente all’interno di questo 
file e stampa a schermo il suo contenuto.

Per maggiori informazioni, consultare ``README_profiler.txt``.

**QSS_module.py:**

Tale modulo contiene le definizioni delle varianti dell’algoritmo di ordinamento ``QuickSort`` in cui la scelta
del pivot avviene tramite algoritmi di selezione. Si è scelto di implementare una funzione ``quickSelectSort``, che prende
in input una lista ed un parametro che indica quale tra gli algoritmi di selezione dovrà essere eseguito. Questa funzione
richiama a sua volta la funzione ``recursiveQuickSelectSort`` che, a differenza della prima, prende in più in input due 
parametriche indicano l’inizio e la fine della lista, estrae il pivot con l’algoritmo di selezione scelto, crea la 
partizione ed infine, ricorsivamente, risolve lo stesso problema nelle sottoliste.

Per maggiori informazioni, consultare ``README_QSS_module.md``.

**sorting, selection, strutture:**

Nelle cartelle selection, sorting e strutture sono presenti i moduli d’appoggio richiamati all’interno di ``profiler.py``
e di ``QSS_module.py``, contenenti rispettivamente le definizioni degli algoritmi di selezione, di ordinamento e delle strutture dati. 

**Autori:**

- Mihai Jianu        0255043
- Daniele La Prova   0253508
- Lorenzo Mei       *matricola*
