class KNN:

    def __init__(self,train,test,vector_size, k):
        self.train = train
        self.test = test
        self.vector_size = vector_size
        self.k = k
        self.distances = []
        self.convert_to_floats()


    #converts string coordinates to floats
    def convert_to_floats(self):
        
        for i in range(len(self.train)):
            for j in range(self.vector_size):
                self.train[i][j] = float(self.train[i][j])

        for i in range(len(self.test)):
            for j in range(self.vector_size):
                self.test[i][j] = float(self.test[i][j])

    #calculates distances between one test vector and all train vectors
    #creates a list of (name, distance) tuples
    #sorts the list according to distance
    def calc_distances(self,test_vector):

        distances = []

        for i in range(len(self.train)):
            distance = 0.0
            for j in range(self.vector_size):
                distance += (self.train[i][j] - test_vector[j])**2

            distances.append( (self.train[i][self.vector_size],distance))

        distances.sort( key= lambda x : x[1])
        return distances
    
    #takes k nearest neighbors for each test case
    #puts all the names and number of their occurences into a dictiory
    #retrieves the first key 
    #compares the prediction to the answer
    def classify(self):
        
        acc = 0.0

        for i in range(len(self.test)):
            distances = self.calc_distances(self.test[i])
            distances = distances[0:self.k]

            neighbors = {}

            for (x,y) in distances:
                if x in neighbors:
                    neighbors[x] += 1
                else:
                    neighbors[x] = 1
            
            neighbors = dict(sorted(neighbors.items(), key=lambda item: item[1], reverse=True))
            pred = list(neighbors.keys())[0]
            print(f'Prediction: {pred}\nAnswer: {self.test[i][self.vector_size]}')

            if pred == self.test[i][self.vector_size]:
                acc += 1
        print(f'Acc: {100.0*acc/float(len(self.test))}%')