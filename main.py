import os


def option_sys(options):
    index = 0
    ch = "---"
    while ch != "p": # looping the option for choosing if use has not pressed 'p' for pick

        for i, opt in enumerate(options):
            
            if i != index: 
                print("  ",opt) #print two empty spaces before option chosen 
            else:
                print("> ",opt) #print arrow before option chosen 
            
        ch = input("") #collect input to proceed choosing
        print(ch)

        if ch == "": #in enter is pressed point to next option 
            index += 1
            if index == len(options):
                index = 0

    
    return index


data = ["Chicken", "Port", "Beef", "Fish"]
option_sys(data)

