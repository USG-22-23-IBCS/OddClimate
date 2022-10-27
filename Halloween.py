import random

class House:

    def __init__(self):
        self.rating = random.randint(1, 10)

    def getRating(self):
        return self.rating


def randPath(m, num):
    p = [] #the list that is the path

    while (len(p) < num): 
        p = []             
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        pVal = m[x][y] #house and ratings
        p.append([x,y]) #added house to list.
                        #[x][y] is to access a position of a list (outer,inner) 
                        #[x,y] is a list with 2 elements
        for i in range(num - 1): #this is within the while loop

    #lists:--------------------------------------------------
            neighbors = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            bad = []
    #--------------------------------------------------------

            for n in neighbors: #literally looks at the neighbors list up there
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)
            #basically add things to 'bad' trashcan THEN delete

            for b in bad: #b is each of the neighbors in 'bad'
                neighbors.remove(b) #"remove the neighbors that are 'b' from neighbors"
                
            if len(neighbors) == 0: #if there are no good neighbors left, break loop ↑
                break               #                                       and try again

            nextHouse = random.choice(neighbors)
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y] #pVal is the total of all houses currently in the path

        print("Path:")
        return pVal, p
                           
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int(input("What number of houses do you want to visit?\n "))

    total = 0 #this is the total of
    for i in range(5):
        for j in range(5): #can't use i twice, so j
            total = total + m[i][j]

    average = total/25

    pVal, p = randPath(m, num)
    
    while (average > pVal/num):
        pVal, p = randPath(m, num)

    print(p)

    print("The Average Value of the neighborhood is " + str(average))
    print("The Average Value of the path is " + str(pVal/num))

    if (str(pVal/num) > (str(average))):
        print("Great! The path is better than the average neighborhood value.")

if __name__ == "__main__":
    main()


#GREEDY PATH-------------------------------------------
#! 1. Create a list of the best houses in a sorted order. (different to ^)
#2. Keep track of pVal (same as ^)
#3. Pick next house from bestHouses list (different to ^)
#4. Check to see bad neighbors and if we are stuck. (same as ^)
#! 5. Pick the best neighbor from the good ones. (different to ^)
#6. Add neighbor to pack and update x, y and pVal. (same as ^)
#7. if len(p) == num
   #return pVal, p

#def greedyPath(m, num):
    #bestHouses = []

    #for i in range(len(bestHouses)):
    #p = []

    #start = bestHouses[i]
    #x = start[0]
    #y = start[1]

    #for i in range(num - 1):
    
