import random
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__' :
    mylist =   lst =  [*range(1, 101)]
    random.shuffle(mylist)
    liste1 = mylist
    print(liste1)
    liste2 = []
    plt.ion()
    def tester() :
        for i in range(0,99) :
            if liste1[i] < liste1[i + 1] :
                y = liste1[i]
                liste1[i] = liste1[i + 1]
                liste1[i + 1] = y

        else :
                pass


    for j in range(0, 99) :
        liste2.append(liste1[:])
        tester()
    print(liste1)
    print(liste2)


    x = np.array(liste1)
    while liste1 != liste2 :

        for t in liste2 :
            plt.clf()
            c = np.array(t)
            plt.plot(x, c)
            plt.pause(0.11)
            plt.show()
