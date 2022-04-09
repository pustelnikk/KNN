import random
import sys
import csv
import KNN


def csv_to_list(name):

    data = []

    with open(name) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

    
def get_vector_size(data_set):
    return len(data_set[0]) - 1


def main():
    train = csv_to_list("train-set.csv")
    test = csv_to_list("test-set.csv")
    vector_size = get_vector_size(train)
    k = 3
    print(vector_size)
    classifier = KNN.KNN(train,test,vector_size,k)
    classifier.classify()



if __name__ == '__main__' :
    main()
