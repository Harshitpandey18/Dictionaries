def addToInventory(Inventory, addedItems): #a function is created
    count=0 
    for i in addedItems: #loop will run 
        if i in Inventory:
            Inventory[i] += 1
        else:
            Inventory[i] = 1
    print("New Inventory:")
    for key, value in Inventory.items(): #loop will run
        print(value, key)
        count+= value 
    print("Total number of Items: ", count)
Inventory={'arrow':8,'gold chain':26,'rope':2,'dagger':1} #a dictionary is created
count=0 
print("Inventory:")
for key, value in Inventory.items(): #loop will run 
        print(value, key)
        count= count+ value 
print("Total number of Items: ", count)
addedItems=[] #empty list is created
#input validation
while True:
    try:
        n=int(input("Enter the number of new items: "))
    except:
        print("Enter an Integer")
        continue
    break
for i in range(n):
    #input validation
    while True:
        try:
            a=str(input("Enter Item name: "))
            addedItems.append(a)
        except:
            print("Enter a string")
            continue
        break
addToInventory(Inventory, addedItems) #function call
