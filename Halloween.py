import random

class House:

    def __init__(self):
        self.rating = random.randint(1, 10)

    def getRating(self):
        return self.rating


def randPath(m, num):
    p = []

    while (len(p) < num): 
        p = []             
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        pVal = m[x][y] 
        p.append([x,y])

        for i in range(num - 1): 

            neighbors = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            bad = []

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

            nextHouse = random.choice(neighbors)
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y] 

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

    total = 0 
    for i in range(5):
        for j in range(5):
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
