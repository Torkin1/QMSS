# profiler.py

```
>>> import profiler
>>> help(profiler)
```
```
NAME
    profiler

DESCRIPTION
    File name: profiler.py
    Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
    Python version: 3.x
    
    Script di profiling per gli algoritmi di ordinamento
    
    $ python[3.x] -m profiler -h
    
    usage: python -m main [-h] [-m] [-r] [-d] [-o] size range
    
    profiles quickSelectionSort execution time with major sorting algorithms
    
    positional arguments:
      size                 size of the list
      range                maximum range of values generated
    
    optional arguments:
      -h, --help           show this help message and exit
      -m, --median         includes quickSelectSort with sampleMedianSelect
      -r, --random         inlcudes quickSelectSort with quickSelectRand
      -d, --deterministic  includes quickSelectSort with quickSelectDet
      -o, --others         inlcudes major sorting algorithms


```
