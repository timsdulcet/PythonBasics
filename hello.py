print('Hello, World!')
print(2*2)

name = "Keena1n"

if name == "Keenan":  
    print ("Hello,", name)
else:  
    print ("Oh, well, what is your name then?")


def checkName(name):  
    answer = input("Is your name " + name + "? ") 


    if answer.lower() == "yes": # lower() turns the answer into lowercase
        print("Hello,", name)  
    else:    
        print("We're sorry about that.")

checkName("Keenan")