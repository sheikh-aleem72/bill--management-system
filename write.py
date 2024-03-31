from tkinter import messagebox


# Update the inventory on adding new Item
def addToList(name,price,quantity):
    with open("products.txt","a") as file:
        print("Names from write()")
        print(name,price,quantity)
        file.write(f"{name},{price},{quantity}\n")


def updateToItem(details):
    # Read the contents of the file
    with open("products.txt", "r") as file:
        lines = file.readlines()

    # List to store data based on the first word
    data = []   

    # Iterate over the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split(",") # Split the line by comma
        data.append(parts)

    # Modify the existing data based on the first word
    for index,item in enumerate(data):
        if item[0] == details[0]:
            data[index][0] = details[0]
            data[index][2] = details[1]

    with open("products.txt","w") as file:
        for i,item in enumerate(data):
            file.write(f"{item[0]},{item[1]},{item[2]}\n")

    messagebox.showinfo("Success","Details of item updated successfully!")

def removeItem(name):
    # Read the contents of the file
    with open("products.txt", "r") as file:
        lines = file.readlines()

    # Dictionary to store data based on the first word
    data = []   

    # Iterate over the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split(",") # Split the line by comma
        data.append(parts)

    # Modify the existing data based on the first word
    for index,item in enumerate(data):
        if item[0] == name:
            data.remove(item)

    with open("products.txt","w") as file:
        for i,item in enumerate(data):
            file.write(f"{item[0]},{item[1]},{item[2]}\n")

    messagebox.showinfo("Success","Item has been removed successfully!")

def modifyList(list_data):
    # Read the contents of the file
    with open("products.txt", "r") as file:
        lines = file.readlines()

    # Dictionary to store data based on the first word
    data = []   

    # Iterate over the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split(",") # Split the line by comma
        data.append(parts)

    # Modify the existing data based on the first word
    for index,item in enumerate(data):
        for element in list_data:
            if item[0] == element[0]:
                data[index][0] = element[0]
                data[index][1] = element[1]
                data[index][2] = int(data[index][2]) - int(element[2])

    with open("products.txt","w") as file:
        for i,item in enumerate(data):
            file.write(f"{item[0]},{item[1]},{item[2]}\n")