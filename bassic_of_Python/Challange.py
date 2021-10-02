
## need a lot improuvement but happy with the little time i put on it 


print("1. Place an order\n2. Process an order")
#check the input for the Place or process order 


## improuvement check if the imput is correct
checkIn = input("What wouldtou like to do?")


    


#gipe asking you item to order or blank for stop
if int(checkIn) == 1:
    #asking inputer
    nameOrder = input("What would you like to call this order? ")
    print("Please place your order below. To stop placing your orde, leace the item empty ")
    f = open(nameOrder, "a")
    while True:
        I = input("Item: ")
        if I == "":
            print(f"Order saved to file {nameOrder}  Exiting Application...")
            break
        P = input("Price: ")
        Q = input("Quantity: ")
        print("---------------------------------------------------------")
        f.write(I +"|"+ P +'|'+ Q)
        f.close()






#gipe asking for the order file.txt you want a process
if int(checkIn) == 2:
    mylist = []
    ordrename  = input("What order would tou like to process? ")
    print("----------------------------------------------------------")
    print("Going to the shops and buying everythin for you .... Pleas hold.")
    with open(f"{ordrename}", "r") as f:
        for line in f:
            mylist.append(line.split("|"))
        
        for i in mylist:
            total = int(i[0]) * int(i[1])
            nameitem = str(i[2])
            print(f"Spending {total} on {nameitem} .... ")
        print("Shopping complete.")
else:
    print("something when wrong ") 

