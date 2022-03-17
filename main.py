from math import dist
import sys
import csv
from turtle import distance

def printList(list):
    for entry in list:
        print(entry)
def findVectorSize(list):
    size = 0
    
    for val in list:
        try:
            float(val)
            size +=1
        except:
            pass
    return size

def calcDistance(train, test, size):

    distance = 0.0
    for i in range(size):
        distance = distance + (float(test[i])-float(train[i]))**2
    
    
    return distance

def main():

    if(len(sys.argv) < 4):
        sys.exit("Brak argumentow")

    k = sys.argv[1]
    train = sys.argv[2]
    test = sys.argv[3]
    trainList = []
    testList = []
    

    #
    #czytanie CSV i przeliczanie wymiaru wektora
    #
    #


    with open(train) as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            trainList.append(row)

    with open(test) as file :
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            testList.append(row)
    
    vectorSize = findVectorSize(trainList[0])
    
    
    #
    #klasyfikacja
    #
    #
    distances = [ (calcDistance(item, testList[0], size=vectorSize), item[vectorSize]) for item in trainList]
    

    #sortowanie krotki
    distances.sort(key= lambda tup : tup[0])
    printList(distances)



if __name__ == '__main__' :
    main()
