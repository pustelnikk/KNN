import sys
import csv

def printList(list):
    for entry in list:
        print(entry)
def findFloats(list):
    size = 0
    
    for val in list:
        try:
            float(val)
            size +=1
        except:
            pass
    return size

def main():

    if(len(sys.argv) < 4):
        sys.exit("Brak argumentow")

    k = sys.argv[1]
    train = sys.argv[2]
    test = sys.argv[3]
    trainList = []
    vectorSize = 0;

    with open(train) as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            trainList.append(row)

    
    #printList(trainList)
    vectorSize = findFloats(trainList[0])
    #print(vectorSize)

    
if __name__ == '__main__' :
    main()
