# profiler.py
```
python3.5 -m profiler -h
```
```
usage: $ python3 -m profiler [-h] [-m] [-r] [-d] [-o] size range

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

written by Mihai Jianu, Daniele La Prova, Lorenzo Mei

```
