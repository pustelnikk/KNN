import random
import sys
import csv


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

def findClosest(k, distances):

    names = {}
    
    for i in range(k):
        if distances[i][1] not in names:
            names[distances[i][1]] = 1
        else:
            names[distances[i][1]] += 1

    dict(sorted(names.items(), key=lambda item: item[1], reverse = True))
    
    print(names)

    return list(names.keys())[0]
    





    

def main():

    if(len(sys.argv) < 4):
        sys.exit("Brak argumentow")

    k = int(sys.argv[1])
    train = sys.argv[2]
    test = sys.argv[3]
    trainList = []
    testList = []
    accuracy = 0

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
    
    #randomowe rekordy
    
    trainList = random.sample(trainList, 15)

    testList = random.sample(testList, 15)

    print(trainList)
    print(testList)
    
    #
    #klasyfikacja
    #
    #
    for i in range(len(testList)):
        distances = [ (calcDistance(item, testList[i], size=vectorSize), item[vectorSize]) for item in trainList]
        #sortowanie krotki
        distances.sort(key= lambda tup : tup[0])
        #printList(distances)
        print('\n')
        klas = findClosest(k,distances)
        test = testList[i][vectorSize]
        print("Klasyfikacja: " + klas)
        print("Test: " + test)
        if( klas == test ):
            accuracy +=1

    print("\nAccuracy: " + str(100*float(accuracy)/float(len(testList)))+"%")


if __name__ == '__main__' :
    main()
