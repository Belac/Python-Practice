try:
    CardStack = []
    CardStackSize = 5
    while True:
            option = input("(Store/Retrieve/Quit): ")
            option = option.lower()
            if option == "store":
                if len(CardStack) > (CardStackSize-1):
                    print ("Stack is full.")
                    print(CardStack)
                else:
                    card = input("Card: ")
                    CardStack.append(card)
                    print(CardStack)
            elif option == "retrieve":
                TopCard = CardStack.pop()
                print(TopCard)
            elif option == "quit":
                exit()
            else:
                print("Invalid Option.")
except:
    print("Oh poops, there's been an error ¯\_(ツ)_/¯")
    