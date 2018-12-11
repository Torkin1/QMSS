import matplotlib.pyplot as plt

def printGraph():
    #numero di elementi da 500 a 5000 nei vari cambiamenti
    NumbTime = [500,2500,5000]
    QMSS = [0.028,0.112,0.232]
    QSSR = [0.009,0.049,0.106]
    QSSD = [0.025,0.138,0.302]
    Selection = [0.019,0.444,1.832]
    Insertion = [0.013,0.338,1.475]
    Bubble = [0.056,1.483,6.023]
    Merge = [0.006,0.027,0.059]
    Quick = [0.004,0.018,0.038]
    Heap = [0.010,0.057,0.125]
    Radix = [0.008,0.300,0.058]
    Sort = [0.000,0.001,0.001]

    plt.grid()
    plt.plot(NumbTime, QMSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Selection, label="SelectionSort")
    plt.plot(NumbTime, Insertion, label="InsertionSort")
    plt.plot(NumbTime, Bubble, label="BubbleSort")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento")
    plt.legend()
    plt.show()

def printGraph1():
    #grafi per numeri alti
    NumbTime = [7500, 10000, 50000, 75000, 100000]
    QMSS = [0.342, 0.454, 2.454,4.145, 6.13]
    QSSR = [0.164, 0.220, 1.216,2.727 , 3.002]
    QSSD = [0.496, 0.680, 4.079,8.107 , 10.580]
    Selection = [3.967, 7.350, 212.297,519.311 , 923.77]
    Insertion = [3.354, 5.619, 174.234,434.142 , 791.319]
    Bubble = [16.386, 27.983, 781.234,1905.262 , 3681.031]
    Merge = [0.102, 0.139, 0.855,1.298 , 2.602]
    Quick = [0.071, 0.098, 0.526,0.786 , 1.409]
    Heap = [0.234, 0.318, 1.923,3.064 , 5.449]
    Radix = [0.103, 0.136, 0.700,1.077 , 1.837]
    Sort = [0.002, 0.002, 0.022,0.035 , 0.078]

    plt.grid()
    plt.plot(NumbTime, QMSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Selection, label="SelectionSort")
    plt.plot(NumbTime, Insertion, label="InsertionSort")
    plt.plot(NumbTime, Bubble, label="BubbleSort")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento")
    plt.legend()
    plt.show()


def printGraph1p2():
    #grafi per numeri alti "zoomato"
    NumbTime = [7500, 10000, 50000, 75000, 100000]
    QMSS = [0.342, 0.454, 2.454, 4.145, 6.13]
    QSSR = [0.164, 0.220, 1.216, 2.727 , 3.002]
    QSSD = [0.496, 0.680, 4.079, 8.107 , 10.580]
    Selection = [3.967, 7.350, 212.297,519.311 , 923.77]
    Insertion = [3.354, 5.619, 174.234,434.142 , 791.319]
    Bubble = [16.386, 27.983, 781.234,1905.262 , 3681.031]
    Merge = [0.102, 0.139, 0.855,1.298 , 2.602]
    Quick = [0.071, 0.098, 0.526,0.786 , 1.409]
    Heap = [0.234, 0.318, 1.923,3.064 , 5.449]
    Radix = [0.103, 0.136, 0.700,1.077 , 1.837]
    Sort = [0.002, 0.002, 0.022,0.035 , 0.078]

    plt.grid()
    plt.plot(NumbTime, QMSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento")
    plt.legend()
    plt.show()



def printGraph2():
    #grafo che mostra i cambiamenti nel piccolo
    NumbTime = [500,600, 750, 800, 1000]
    QMSS = [0.028, 0.039, 0.041, 0.049, 0.052]
    QSSR = [0.009, 0.011, 0.014, 0.018, 0.020]
    QSSD = [0.025, 0.031, 0.039, 0.048, 0.053]
    Selection = [0.019, 0.033, 0.043, 0.061, 0.075]
    Insertion = [0.013, 0.020, 0.032, 0.044, 0.055]
    Bubble = [0.056, 0.086, 0.132, 0.190, 0.240]
    Merge = [0.006, 0.006, 0.008, 0.010, 0.013]
    Quick = [0.004, 0.006, 0.006, 0.010, 0.007]
    Heap = [0.010, 0.013, 0.016, 0.019, 0.021]
    Radix = [0.008, 0.008, 0.011, 0.012, 0.013]
    Sort = [0.000, 0.000, 0.000, 0.000, 0.000]

    plt.plot(NumbTime, QMSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Selection, label="SelectionSort")
    plt.plot(NumbTime, Insertion, label="InsertionSort")
    plt.plot(NumbTime, Bubble, label="BubbleSort")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento")
    plt.legend()
    plt.show()


def printGraphT():
    #grafo che mostra i cambiamenti nel piccolo con lenTuple = classico, 3, 5,7, 9. len / 50,500,1000
    NumbTime = [500, 1000, 2500, 5000, 7500, 10000, 50000, 75000, 100000]

    QMSSA = [0.025, 0.045, 0.112, 0.231, 0.371, 0.534, 2.970, 4.601, 6.320]
    QMSS =  [0.032,  0.052, 0.239, 0.232, 0.365, 0.504, 2.862, 4.502, 6.295]
    QMSSB = [0.081, 0.182, 0.216, 0.305, 0.453, 0.633, 2.978, 4.577, 6.369]
    QMSSC = [0.090, 0.184, 0.346, 0.527, 0.522, 0.775, 3.139, 4.859, 6.300]
    QMSS3 = [0.050, 0.116, 0.306, 0.736, 1.074, 1.566, 11.314, 17.643, 24.363]
    QMSS5 = [0.035, 0.067, 0.200, 0.424, 0.699, 0.925, 6.027, 10.499, 13.681]
    QMSS7 = [0.029, 0.062, 0.167, 0.352, 0.591, 0.789, 5.407, 8.078, 11.490]
    QMSS9 = [0.026, 0.055, 0.170, 0.312, 0.567, 0.677, 4.518, 7.030, 10.097]

    plt.plot(NumbTime, QMSSA, label="lenTuple = ceil(len(l) / 50)")
    plt.plot(NumbTime, QMSS, label="lenTuple = ceil(len(l) / 100)")
    plt.plot(NumbTime, QMSSB, label="lenTuple = ceil(len(l) / 500)")
    plt.plot(NumbTime, QMSSC, label="lenTuple = ceil(len(l) / 1000)")
    plt.plot(NumbTime, QMSS3, label="lenTuple = 3")
    plt.plot(NumbTime, QMSS5, label="lenTuple = 5")
    plt.plot(NumbTime, QMSS7, label="lenTuple = 7")
    plt.plot(NumbTime, QMSS9, label="lenTuple = 9")

    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple")
    plt.legend()
    plt.show()

def printGraphT2():
    # grafo T zoomato sui len(l)/x
    NumbTime = [500, 1000, 2500, 5000, 7500, 10000, 50000, 75000, 100000]

    QMSSA = [0.025, 0.045, 0.112, 0.231, 0.371, 0.534, 2.970, 4.601, 6.320]
    QMSS = [0.032, 0.052, 0.116, 0.232, 0.365, 0.504, 2.862, 4.502, 6.295]
    QMSSB = [0.081, 0.182, 0.216, 0.305, 0.453, 0.633, 2.978, 4.577, 6.369]
    QMSSC = [0.090, 0.184, 0.346, 0.527, 0.522, 0.775, 3.139, 4.859, 6.300]


    plt.plot(NumbTime, QMSSA, label="lenTuple = ceil(len(l) / 50)")
    plt.plot(NumbTime, QMSS, label="lenTuple = ceil(len(l) / 100)")
    plt.plot(NumbTime, QMSSB, label="lenTuple = ceil(len(l) / 500)")
    plt.plot(NumbTime, QMSSC, label="lenTuple = ceil(len(l) / 1000)")


    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple")
    plt.legend()
    plt.show()

def printGraphr():
    # grafo di QMSS al variare di r, 0,25,
    NumbTime = [500, 1000, 2500, 5000, 7500, 10000, 50000, 75000, 100000]

    QMSS = [0.032, 0.052, 0.116, 0.232, 0.365, 0.442, 2.462, 3.846, 5.071]
    QMSSA = [0.034, 0.058, 0.121, 0.253, 0.369, 0.494, 3.396, 4.668, 6.410]
    QMSSB = [0.034, 0.061, 0.134, 0.259, 0.404, 0.528, 3.568, 5.785, 7.630]
    QMSSC = [0.047, 0.073, 0.180, 0.386, 0.503, 0.689, 3.615, 5.979, 8.532]
    QMSSD = [1.172, 2.462, 4.425, 17.088, 50.469, 54.185, 435.555, 599.401, 902.713]

    plt.plot(NumbTime, QMSS, label="r = 1")
    plt.plot(NumbTime, QMSSA, label="r = 0,75")
    plt.plot(NumbTime, QMSSB, label="r = 0,5")
    plt.plot(NumbTime, QMSSC, label="r = 0,25")
    plt.plot(NumbTime, QMSSD, label="r = 0,01")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QMSS in base al variare di r")
    plt.legend()
    plt.show()

def printGraphrZ():
    # grafo di QMSS al variare di r, 0.75,0.5,0.25,0.01
    NumbTime = [500, 1000, 2500, 5000, 7500, 10000, 50000, 75000, 100000]


    QMSS = [0.032, 0.052, 0.116, 0.232, 0.365, 0.442, 2.462, 3.846, 5.071]
    QMSSA = [0.034, 0.058, 0.121, 0.253, 0.369, 0.494, 3.396, 4.668, 6.410]
    QMSSB = [0.034, 0.061, 0.134, 0.259, 0.404, 0.528, 3.568, 5.785, 7.630]
    QMSSC = [0.047, 0.073, 0.180, 0.386, 0.503, 0.689, 3.615, 5.979, 8.532]


    plt.plot(NumbTime, QMSS, label="r = 1")
    plt.plot(NumbTime, QMSSA, label="r = 0,75")
    plt.plot(NumbTime, QMSSB, label="r = 0,5")
    plt.plot(NumbTime, QMSSC, label="r = 0,25")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QMSS in base al variare di r")
    plt.legend()
    plt.show()

def printGraphr2():
    #grafo al variare di r su 100'000 elementi

    NumbTime = [1.000, 0.500, 0.400, 0.375, 0.350, 0.325, 0.300, 0.275, 0.250, 0.225, 0.200, 0.175, 0.150, 0.125, 0.100]

    QMSS = [5.126, 5.626, 6.016, 6.164, 6.341, 6.547, 6.804, 7.188, 7.404, 7.690, 8.404, 9.225, 10.262, 11.785, 14.893]


    plt.plot(NumbTime, QMSS, label= "100'000 elementi")
    plt.ylabel("Tempo (s)")
    plt.xlabel("range/size")
    plt.grid()
    plt.title("Prestazione QSS in base a range/size")
    plt.legend()
    plt.show()


def printGraphTuple():
    #grafo con lunghezza di 100k
    NumbTime = [1, 3, 5, 7, 9, 17, 25, 50, 100, 200, 500, 1000, 2000, 3500, 3750, 4000, 5000, 7500, 10000, 50000, 100000]

    lenT = [43.472, 19.696, 11.434, 9.348, 8.401, 6.663, 5.906, 5.595, 5.296, 5.205, 5.040, 5.038, 5.019, 4.988, 5.082, 5.363, 5.352, 5.415, 5.298, 4.951, 5.490]

    plt.plot(NumbTime, lenT, label = "100'000 elementi")
    plt.grid()
    plt.xlabel("Valori lenTuple")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple")
    plt.legend()
    plt.show()

def printGraphTuple2():
    # grafo con lunghezza di 100k
    NumbTime = [1, 3, 5, 7, 9, 17]
    lenT = [43.472, 19.696, 11.434, 9.348, 8.401, 6.663]

    plt.plot(NumbTime, lenT, label="100'000 elementi")
    plt.grid()
    plt.xlabel("Valori lenTuple")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple (zoom1)")
    plt.legend()
    plt.show()



def printGraphTuple3():
    # grafo con lunghezza di 100k
    NumbTime = [25, 50, 100, 200, 500]
    lenT = [5.906, 5.595, 5.296, 5.205, 5.040]

    plt.plot(NumbTime, lenT, label="100'000 elementi")
    plt.grid()
    plt.xlabel("Valori lenTuple")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple (zoom2)")
    plt.legend()
    plt.show()

def printGraphTuple4():
    # grafo con lunghezza di 100k
    NumbTime = [1000, 2000, 3500, 3750, 4000, 5000, 7500]
    lenT = [5.038, 5.019, 4.988, 5.082, 5.363, 5.352, 5.415]

    plt.plot(NumbTime, lenT, label = "100'000 elementi")
    plt.grid()
    plt.xlabel("Valori lenTuple")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple (zoom3)")
    plt.legend()
    plt.show()

def printGraphTuple5():
    # grafo con lunghezza di 100k
    NumbTime = [10000, 25000, 50000, 75000, 100000]
    lenT = [5.298, 5.070,4.951, 5.023, 5.490,]

    plt.plot(NumbTime, lenT, label = "100'000 elementi")
    plt.grid()
    plt.xlabel("Valori lenTuple")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QSS in base a lenTuple (zoom4)")
    plt.legend()
    plt.show()




def printGraphReve():
    #numero di elementi da 500 a 5000 nei vari cambiamenti
    NumbTime = [500, 1250, 2500, 3125, 5000]
    QSS = [0.032,0.060, 0.143, 0.155, 0.218]
    QSSR = [0.009, 0.024, 0.061, 0.058, 0.097]
    QSSD = [0.023,0.059, 0.140, 0.170, 0.272]
    Selection = [0.019, 0.116, 0.565, 0.718, 1.878]
    Insertion = [0.015,0.099, 0.419, 0.640, 1.655]
    Bubble = [0.0770, 0.497, 2.114, 3.436, 8.142]
    Merge = [0.004, 0.011, 0.022, 0.028, 0.047]
    Quick = [0.003, 0.008, 0.017, 0.044, 0.035]
    Heap = [0.009, 0.027, 0.056, 0.072, 0.120]
    Radix = [0.007, 0.015, 0.030, 0.037, 0.057]
    Sort = [0.000, 0.000, 0.000, 0.000, 0.000, 0.000]

    plt.grid()
    plt.plot(NumbTime, QSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Selection, label="SelectionSort")
    plt.plot(NumbTime, Insertion, label="InsertionSort")
    plt.plot(NumbTime, Bubble, label="BubbleSort")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento con lista ordinata al contrario")
    plt.legend()
    plt.show()

def printGraphReve2():
    #numero di elementi da 500 a 5000 nei vari cambiamenti
    NumbTime = [10000, 25000, 50000, 75000, 100000]
    QSS = [0.429, 1.147, 2.513, 4.007, 5.132]
    QSSR = [0.212, 0.533, 1.134, 1.839, 2.534]
    QSSD = [0.583, 1.739, 3.653, 6.250, 8.231]
    Selection = [7.468, 46.339, 183.702, 451.490, 823.890]
    Insertion = [6.621,42.828, 176.954, 486.439, 799.289]
    Bubble = [32.992, 214.760, 848.697, 2385.772, ]
    Merge = [0.095, 0.260, 0.609, 0.928, ]
    Quick = [0.072, 0.182, 1.018, 0.626, ]
    Heap = [0.254, 0.696, 1.807, 2.573, ]
    Radix = [0.114, 0.288, 0.978, 0.936, ]
    Sort = [0.001, 0.001, 0.013, 0.010, ]

    plt.grid()
    plt.plot(NumbTime, QSS, label="QSS(SampleMedianSelect)")
    plt.plot(NumbTime, QSSR, label="QSSR")
    plt.plot(NumbTime, QSSD, label="QSSD")
    plt.plot(NumbTime, Selection, label="SelectionSort")
    plt.plot(NumbTime, Insertion, label="InsertionSort")
    plt.plot(NumbTime, Bubble, label="BubbleSort")
    plt.plot(NumbTime, Merge, label="MergeSort")
    plt.plot(NumbTime, Quick, label="QuickSort")
    plt.plot(NumbTime, Heap, label="HeapSort")
    plt.plot(NumbTime, Radix, label="RadixSort")
    plt.plot(NumbTime, Sort, label="Python's Sort")
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Algoritmi di ordinamento con lista ordinata al contrario")
    plt.legend()
    plt.show()