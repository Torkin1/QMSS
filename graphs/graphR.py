def printGraphr2():
    #grafo al variare di r su 100'000 elementi
    NumbTime = [1, 0.75, 0.5, 0.25]

    QMSS = [5.271, 6.010, 7.330, 8.532]


    plt.plot(NumbTime, QMSS, label= "100'000 elementi")
    plt.ylabel("Tempo (s)")
    plt.title("Prestazione QMSS in base al variare di r")
    plt.legend()
    plt.show()