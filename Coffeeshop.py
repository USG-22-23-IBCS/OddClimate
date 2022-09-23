#- Your class has a working constructor method (__init__)
#- Your class has values for the drinks it offers and their prices
#- Your class has at least 2 actions (methods/functions) in addition to the
#constructor method (getPrice(drink), or getInfo() could be good options)
#- Your module also contains a working main method
#- Your main method creates one instance of your shop.
#- Your main method has inputs that prompt the user to order.
#- Your main method correctly prints out what the order is and how much it costs
#based on the user input (correct use of conditional statements).

#Dutch Bros
    #Black Coffee
    #Americano
    #Bagel

class Cafe:
    def __init__(self, name, o1, o2, blackcoffee):
        self.name = name
        self.order1 = o1
        self.order2 = o2
        self.order3 = o3
        self.blackcoffee = blackcoffee
        
def main():
    Cafe = Cafe("Dutch Bros", "Black Coffee", "Americano", "Okay, one Black Coffee. Would you like a bagel with that?")

print("Welcome to. Our options are on the menu.")
print("- Black Coffee, $2")
print("- Americano, $2")
print("- Bagel, $1")
drink = input("Which drink would you like?")

if drink == "Black Coffee":
    bagel = input("Okay, one Black Coffee. Would you like a bagel with that?")
    
elif drink == " Black Coffee":
    print("Okay, one Black Coffee. Would you like a bagel with that?")
elif drink == "black coffee":
    print("Okay, one Black Coffee. Would you like a bagel with that?")
elif drink == " black coffee":
    print("Okay, one Black Coffee. Would you like a bagel with that?")
    user_in=input(" ")
    
else:
    print("Okay, one Americano. Would you like a bagel with that?")
    user_in=input(" ")
if bagel == "Yes":
    print("Wonderful. Your order will be three dollars.")
elif user_in == "yes":
    print("Wonderful. Your order will be three dollars.")
elif user_in == " Yes":
    print("Wonderful. Your order will be three dollars.")
elif user_in == " yes":
    print("Wonderful. Your order will be three dollars.")
    user_in=input(" ")
else:
    print("Okay. Your order will be two dollars.")
