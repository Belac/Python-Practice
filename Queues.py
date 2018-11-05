try:
    Queue = []
    while True:
            option = input("(Store/Complete Order/Quit): ")
            option = option.lower()
            if option == "store":
                Order = input("Order: ")
                Queue.append(Order)
                print(Queue)
            elif option == "complete order":
                Queue.remove(Queue[0])
                print("Order has left the kitchen.")
                print(Queue)
            elif option == "quit":
                exit()
            else:
                print("Invalid Option.")
except:
    print("Oh poops, there's been an error ¯\_(ツ)_/¯")
    