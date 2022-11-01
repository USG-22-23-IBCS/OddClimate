import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

    
def greedyPath(m, num):

    bestHouses = []
    houses = []
    coordinates = []

    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coordinates.append([i,j])

    for i in range(25):
        
        maxHouse = houses[0]

        for h in houses:
            if h > maxHouse:
                maxHouse = h

        pos = houses.index(maxHouse)
        bestHouses.append(coordinates.pop(pos))
        houses.pop(pos)

    print("These are the best houses in order of best to worst(refer to the last line):\n" + str(bestHouses))
    
    
    for i in range(25):
        p = []

        start = bestHouses[i] #best element
        x = start[0] #1st coordinate of best element. not 0, but the 1st thing
        y = start[1] #2nd (etc.)
        pVal = m[x][y]
        p.append(start)


        for i in range(num - 1):
            #---------
            neighbors = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            bad = []
            #---------
            
            for n in neighbors: 
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)
          
            for b in bad:
                neighbors.remove(b) 
                
            if len(neighbors) == 0:
                break

            
            bestNeighbor = neighbors[0]
            broken = False
            for b in bestHouses:
                if broken:
                    break
                for n in neighbors:
                    if n == b:
                        bestNeighbor = n
                        broken = True
                        break

            p.append(bestNeighbor)
            x = bestNeighbor[0]
            y = bestNeighbor[1]
            pVal = pVal + m[x][y]
            

        if len(p) == num:
            return pVal, p


    return 0, [[0,0]]



def randPath(m, num):
  
    p = []

      
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("What number of houses do you want to visit?\n "))
    
    pVal, p = greedyPath(m, num)

    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]
    average = total/25

    print(p)
    print("The Average Value of the neighborhood is " + str(average))
    print("The Average Value of the path is " + str(pVal/num))

    if (str(pVal/num) > (str(average))):
        print("Great! The path is better than the average neighborhood value.")
        

if __name__ == "__main__":
    main()
