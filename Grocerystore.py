


#When running this program, if you want to make the choice of 'View Bag' or 'No' please stick
#  with one of them. If you choose 'View Bag', there won't be any code for 'No', and vice versa.
#     It is taking me a very long time to complete. I will submit the finished version later.


class Witchstuffs:

    def __init__(self):
        self.witch = "Hoy hoy... You can't have the great Hohoyin! Get outta here!!\nJust kidding..."
        self.cash = "Hoy... here's your change! Have a great death! Hoyhoyhoyhoyhoyyyy!!! >:3"
        self.credit = "Byebye! Have a great death! Hoyhoyhoyhoyhoyyyy!!! >:3"

    def getWitch(self):
        return self.witch

    def getCash(self):
        return self.cash

    def getCredit(self):
        return self.credit

def main():
    store = Witchstuffs()

    products = {"Pumpkin" : 5,
             "M&Murders" : 2,
             "Cauldron" : 30,
             "Full-Size Candy Bar" : 70,
             "Candles" : 5,
             "Mystic Potion" : 430,
             "Poison" : 3,
             "Cucumber" : 1,
             "Ghost Bites" : 2,
             "Bloody Icing" : 3,
                "You 🤩" : 1000}

    productsList = list(products.keys())

    cart = []
    
    totPrice = []

    print("")
    print("★ Witch: Hoy hoy! Welcome to Witchstuffs. Which three stuff do you want?\nPlease pick one at a time, hoy!\nUSE CAPS LOCK\n")
    print(productsList)
    
    stuff = input()
            
    if stuff == "PUMPKIN":
        cart.append("Pumpkin: $5")
        productsList.remove("Pumpkin")
        totPrice.append(int(5))
        #print(productsList)
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "M&MURDERS":
        cart.append("M&Murders: $2")
        productsList.remove("M&Murders")
        totPrice.append(int(2))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "CAULDRON":
        cart.append("Cauldron: $30")
        productsList.remove("Cauldron")
        totPrice.append(int(30))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "FULL-SIZE CANDY BAR":
        cart.append("Full-Size Candy Bar: $70")
        productsList.remove("Full-Size Candy Bar")
        totPrice.append(int(70))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "CANDLES":
        cart.append("Candles: $5")
        productsList.remove("Candles")
        totPrice.append(int(5))
        print("Hoy hoy! I put it in your bag ;P")

    elif stuff == "MYSTIC POTION":
        cart.append("Mystic Potion: $430")
        productsList.remove("Mystic Potion")
        totPrice.append(int(430))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "POISON":
        cart.append("Poison: $3")
        productsList.remove("Poison")
        totPrice.append(int(3))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "CUCUMBER":
        cart.append("Cucumber: $1")
        productsList.remove("Cucumber")
        totPrice.append(int(1))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "GHOST BITES":
        cart.append("Ghost Bites: $2")
        productsList.remove("Ghost Bites")
        totPrice.append(int(2))
        print("Hoy hoy! I put it in your bag ;P")
        
    elif stuff == "BLOODY ICING":
        cart.append("Bloody Icing: $3")
        productsList.remove("Bloody Icing")
        totPrice.append(int(3))
        print("Hoy hoy! I put it in your bag ;P")

    elif stuff == "YOU":
        cart.append("Hohoyin: $1000")
        productsList.remove("You 🤩")
        totPrice.append(int(1000))
        print("Hoy hoy! I am in your bag ;P")

    
    done = input("Are you done, hoy?\n(USE CAPS LOCK)\n'Yes' 'No' 'View Bag'\n")

    if done == "VIEW BAG":
        print(cart)
        donedone = input("Well?...\n'Done' 'Not done'\n")
        
        if donedone == "NOT DONE":
            print("Hoy hoy! What else, then? You have two more picks!")
            print(productsList)
            stuff = input()
                    
            if stuff == "PUMPKIN":
                cart.append("Pumpkin: $5")
                productsList.remove("Pumpkin")
                totPrice.append(int(5))
                #print(productsList)
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "M&MURDERS":
                cart.append("M&Murders: $2")
                productsList.remove("M&Murders")
                totPrice.append(int(2))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CAULDRON":
                cart.append("Cauldron: $30")
                productsList.remove("Cauldron")
                totPrice.append(int(30))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "FULL-SIZE CANDY BAR":
                cart.append("Full-Size Candy Bar: $70")
                productsList.remove("Full-Size Candy Bar")
                totPrice.append(int(70))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CANDLES":
                cart.append("Candles: $5")
                productsList.remove("Candles")
                totPrice.append(int(5))
                print("Hoy hoy! I put it in your bag ;P")

            elif stuff == "MYSTIC POTION":
                cart.append("Mystic Potion: $430")
                productsList.remove("Mystic Potion")
                totPrice.append(int(430))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "POISON":
                cart.append("Poison: $3")
                productsList.remove("Poison")
                totPrice.append(int(3))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CUCUMBER":
                cart.append("Cucumber: $1")
                productsList.remove("Cucumber")
                totPrice.append(int(1))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "GHOST BITES":
                cart.append("Ghost Bites: $2")
                productsList.remove("Ghost Bites")
                totPrice.append(int(2))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "BLOODY ICING":
                cart.append("Bloody Icing: $3")
                productsList.remove("Bloody Icing")
                totPrice.append(int(3))
                print("Hoy hoy! I put it in your bag ;P")

            elif stuff == "YOU":
                cart.append("Hohoyin: $1000")
                productsList.remove("You 🤩")
                totPrice.append(int(1000))
                print("Hoy hoy! I am in your bag ;P")


            done = input("Are you done, hoy?\n(USE CAPS LOCK)\n'Yes' 'No' 'View Bag'\n")

            if done == "VIEW BAG":
                print(cart)
                donedone = input("Well?...\n'Done' 'Not done'\n")
                
                if donedone == "NOT DONE":
                    print("Hoy hoy! What else, then? You have one more pick!")
                    print(productsList)
                    stuff = input()
                            
                    if stuff == "PUMPKIN":
                        cart.append("Pumpkin: $5")
                        productsList.remove("Pumpkin")
                        totPrice.append(int(5))
                        #print(productsList)
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "M&MURDERS":
                        cart.append("M&Murders: $2")
                        productsList.remove("M&Murders")
                        totPrice.append(int(2))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "CAULDRON":
                        cart.append("Cauldron: $30")
                        productsList.remove("Cauldron")
                        totPrice.append(int(30))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "FULL-SIZE CANDY BAR":
                        cart.append("Full-Size Candy Bar: $70")
                        productsList.remove("Full-Size Candy Bar")
                        totPrice.append(int(70))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "CANDLES":
                        cart.append("Candles: $5")
                        productsList.remove("Candles")
                        totPrice.append(int(5))
                        print("Hoy hoy! I put it in your bag ;P")

                    elif stuff == "MYSTIC POTION":
                        cart.append("Mystic Potion: $430")
                        productsList.remove("Mystic Potion")
                        totPrice.append(int(430))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "POISON":
                        cart.append("Poison: $3")
                        productsList.remove("Poison")
                        totPrice.append(int(3))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "CUCUMBER":
                        cart.append("Cucumber: $1")
                        productsList.remove("Cucumber")
                        totPrice.append(int(1))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "GHOST BITES":
                        cart.append("Ghost Bites: $2")
                        productsList.remove("Ghost Bites")
                        totPrice.append(int(2))
                        print("Hoy hoy! I put it in your bag ;P")
                        
                    elif stuff == "BLOODY ICING":
                        cart.append("Bloody Icing: $3")
                        productsList.remove("Bloody Icing")
                        totPrice.append(int(3))
                        print("Hoy hoy! I put it in your bag ;P")

                    elif stuff == "YOU":
                        cart.append("Hohoyin: $1000")
                        productsList.remove("You 🤩")
                        totPrice.append(int(1000))
                        print("Hoy hoy! I am in your bag ;P")

                    print(cart)
                    print("Now! Your total for that is $" + str(sum(totPrice)))
                    pay = input("Cash or credit, hoy? (USE CAPS LOCK)\n")
                    if pay == "CASH":
                        print(store.getCash())

                    elif pay == "CREDIT":
                            print("Hoy... swipe here.")
                            credit = input("Good, now enter your pin...\n")
                            print(store.getCredit())
                            

                    elif donedone == "DONE":
                        print("Great!")
                        pay = input("Cash or credit, hoy? (USE CAPS LOCK)\n")
                        if pay == "CASH":
                            print(store.getCash())
    
    elif done == "NO":
        print("Hoy hoy! What else, then? You have two more picks!")
        print(productsList)
        stuff = input()
                
        if stuff == "PUMPKIN":
            cart.append("Pumpkin: $5")
            productsList.remove("Pumpkin")
            totPrice.append(int(5))
            #print(productsList)
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "M&MURDERS":
            cart.append("M&Murders: $2")
            productsList.remove("M&Murders")
            totPrice.append(int(2))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "CAULDRON":
            cart.append("Cauldron: $30")
            productsList.remove("Cauldron")
            totPrice.append(int(30))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "FULL-SIZE CANDY BAR":
            cart.append("Full-Size Candy Bar: $70")
            productsList.remove("Full-Size Candy Bar")
            totPrice.append(int(70))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "CANDLES":
            cart.append("Candles: $5")
            productsList.remove("Candles")
            totPrice.append(int(5))
            print("Hoy hoy! I put it in your bag ;P")

        elif stuff == "MYSTIC POTION":
            cart.append("Mystic Potion: $430")
            productsList.remove("Mystic Potion")
            totPrice.append(int(430))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "POISON":
            cart.append("Poison: $3")
            productsList.remove("Poison")
            totPrice.append(int(3))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "CUCUMBER":
            cart.append("Cucumber: $1")
            productsList.remove("Cucumber")
            totPrice.append(int(1))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "GHOST BITES":
            cart.append("Ghost Bites: $2")
            productsList.remove("Ghost Bites")
            totPrice.append(int(2))
            print("Hoy hoy! I put it in your bag ;P")
            
        elif stuff == "BLOODY ICING":
            cart.append("Bloody Icing: $3")
            productsList.remove("Bloody Icing")
            totPrice.append(int(3))
            print("Hoy hoy! I put it in your bag ;P")

        elif stuff == "YOU":
            cart.append("Hohoyin: $1000")
            productsList.remove("You 🤩")
            totPrice.append(int(1000))
            print("Hoy hoy! I am in your bag ;P")


        done = input("Are you done, hoy?\n(USE CAPS LOCK)\n'Yes' 'No' 'View Bag'\n")

        if done == "NO":
            print("Hoy hoy! What else, then? You have one more pick!")
            print(productsList)
            stuff = input()
                    
            if stuff == "PUMPKIN":
                cart.append("Pumpkin: $5")
                productsList.remove("Pumpkin")
                totPrice.append(int(5))
                #print(productsList)
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "M&MURDERS":
                cart.append("M&Murders: $2")
                productsList.remove("M&Murders")
                totPrice.append(int(2))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CAULDRON":
                cart.append("Cauldron: $30")
                productsList.remove("Cauldron")
                totPrice.append(int(30))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "FULL-SIZE CANDY BAR":
                cart.append("Full-Size Candy Bar: $70")
                productsList.remove("Full-Size Candy Bar")
                totPrice.append(int(70))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CANDLES":
                cart.append("Candles: $5")
                productsList.remove("Candles")
                totPrice.append(int(5))
                print("Hoy hoy! I put it in your bag ;P")

            elif stuff == "MYSTIC POTION":
                cart.append("Mystic Potion: $430")
                productsList.remove("Mystic Potion")
                totPrice.append(int(430))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "POISON":
                cart.append("Poison: $3")
                productsList.remove("Poison")
                totPrice.append(int(3))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "CUCUMBER":
                cart.append("Cucumber: $1")
                productsList.remove("Cucumber")
                totPrice.append(int(1))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "GHOST BITES":
                cart.append("Ghost Bites: $2")
                productsList.remove("Ghost Bites")
                totPrice.append(int(2))
                print("Hoy hoy! I put it in your bag ;P")
                
            elif stuff == "BLOODY ICING":
                cart.append("Bloody Icing: $3")
                productsList.remove("Bloody Icing")
                totPrice.append(int(3))
                print("Hoy hoy! I put it in your bag ;P")

            elif stuff == "YOU":
                cart.append("Hohoyin: $1000")
                productsList.remove("You 🤩")
                totPrice.append(int(1000))
                print("Hoy hoy! I am in your bag ;P")

            print(cart)
            print("Now! Your total for that is $" + str(sum(totPrice)))
            pay = input("Cash or credit, hoy? (USE CAPS LOCK)\n")
            if pay == "CASH":
                print(store.getCash())

            elif pay == "CREDIT":
                    print("Hoy... swipe here.")
                    credit = input("Good, now enter your pin...\n")
                    print(store.getCredit())
        
                
    elif done == "YES":
        print("Great!")
        print("Now! Your total for that is $" + str(sum(totPrice)))
        pay = input("Cash or credit, hoy? (USE CAPS LOCK)\n")
        
        if pay == "CASH":
            print(store.getCash())

        elif pay == "CREDIT":
                print("Hoy... swipe here.")
                credit = input("Good, now enter your pin...\n")
                print(store.getCredit())
                    

if __name__ == "__main__":
    main()
