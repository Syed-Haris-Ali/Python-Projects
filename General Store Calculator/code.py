sum = 0
while(True):
    userInput = input("Enter the Item Price or Press Q to Exit: \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Order Total so far: {sum}")
    else:
        print(f"Your Bill Total is {sum}. Thanks for shopping with us")
        break
