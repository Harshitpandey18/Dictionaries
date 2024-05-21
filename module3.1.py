def displayInventory():
    inventory={} #empty dictionary is created
    count=0
    #input validation
    while True:
        try: #checks if the input is of correct data type or not
            n=int(input("Enter the number of input you want to give: "))
        except:
            print("Enter a integer")
            continue 
        break 
    for i in range(n):
        #input validation
        while True:
            try:
                key=str(input("Enter the name of item: "))
            except:
                print("Enter a string")
                continue
            try:
                value=int(input("Enter the value: "))
            except:
                print("Enter an integer")
                continue
            break
        inventory[key]=value #add items in the dictionary
    print("Inventory:")
    for key , value in inventory.items(): #loop will run
        print(value, key) 
        count+= value 
    print("Total number of items:",count)
displayInventory() #cfunction call
        
    
    
        
