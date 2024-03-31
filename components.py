
import tkinter as tk
from tkinter import messagebox
import validationAndVerification as vANDv
import read
import write


inventory_list = read.read_file()

inventory_list.sort()
# print(inventory_list)


'''Components of table frame'''
def fillDataInTable(tableFrame):
    # listHeader = tk.Label(tableFrame,text="Available Items",font=("Arial", 25))
    # listHeader.grid(row=0,column=1,padx=(120,0), pady=(40, 20), sticky="n")
    header = ["Item","Price","Quantity"]
    rows = len(inventory_list)
    columns = len(inventory_list[0])
    # Find the maximum length of content in each column
    max_lengths = len(header[2])
    # Create Header label
   

    listHeadingLabel = tk.Label(tableFrame,text="Available Items",font=("Arial",18,'bold'),bg="aquamarine1")
    listHeadingLabel.grid(row=0,column=0,pady=(20,0),columnspan=len(header),ipadx=2,ipady=2)

    for y, header_text in enumerate(header):
        label = tk.Label(tableFrame, text=header_text, width=max_lengths + 7, fg='black', font=('Times New Roman', 14, 'italic'), relief='solid', borderwidth=1, bg='slategray3')
        if(header_text=="Item"):
            label.grid(row=3,column=y,padx=(100,0),pady=(30,0))
        elif(header_text=="Quantity"):
            label.grid(row=3,column=y,padx=(0,100),pady=(30,0))
        else:
            label.grid(row=3,column=y,pady=(30,0))
        # label.grid(row=3,column=y,pady=(100,0))

    # Fill in inventory_list data in table
    
    for x, row in enumerate(inventory_list, start=1):

        for y, data in enumerate(row):
            
            label = tk.Label(tableFrame, text=data, width=max_lengths +7, fg='black', font=('Times New Roman', 14, 'italic'), relief='solid', borderwidth=1, bg='snow2')
            
            if(y==0):
                label.grid(row=3+x,column=y, padx=(100,0))
            elif(y==(len(row)-1)):
                label.grid(row=3+x,column=y, padx=(0,100))
            else:
                label.grid(row=3 + x, column=y)

            if(x==len(inventory_list)):
                label.grid(row=3+x,column=y,pady=(0,30))


# ----------------------------------------------------------------------------------------------

# Declare Global variables for input values for adding items to the list
name = None
price = None
quantity = None

# Global variabels for input values to update existing items from the list
nameOfItem = None
quantityOfItem = None

# Global variabels for input values to removing items from the list
removeItemName = None

# Background color for entry labels
pink = 'pink'
'''Components of button frame'''
def buttonFrameComponents(buttonsFrame):
    # Buttons and InputBox for adding items to the list.
    global name
    global price
    global quantity

    # Heading
    addItemHeading = tk.Label(buttonsFrame,text="Add items to the list",font=('Arial', 15, 'bold'),bg=pink)
    addItemHeading.grid(row=0,column=3,columnspan=1,padx=0,pady=(40,10),ipadx=2,ipady=1)
    

    # Take Item name from owner
    iName = tk.Label(buttonsFrame, text='Name:', font=('Arial', 14, 'italic'),bg=pink)
    iName.grid(row=1, column=2,padx=(10,0),pady=(10,5))
    nameInput = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    nameInput.grid(row=1, column=3,padx=10,pady=(10,5),ipadx=5,ipady=5)

    # Take Price from owner.
    iPrice = tk.Label(buttonsFrame, text='Price:', font=('Arial', 14, 'italic'),bg=pink)
    iPrice.grid(row=2, column=2,padx=(10,0),pady=(10,5))
    priceInput = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    priceInput.grid(row=2, column=3,padx=10,pady=(10,5),ipadx=5,ipady=5)

    # Take Quantity from owner
    iQuantity =tk.Label(buttonsFrame, text='Quantity:', font=('Arial', 14, 'italic'),bg=pink)
    iQuantity.grid(row=3, column=2,padx=(10,0),pady=(10,10))
    quantityInput = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    quantityInput .grid(row=3, column=3,padx=10,pady=(10,10),ipadx=5,ipady=5)


    # Naming instruction information
    
    # nameInput.bind("<FocusIn>", namingInstructions)

    # Initializing local variables to global variables
    name = nameInput
    price = priceInput
    quantity = quantityInput


# ----------------------------------------------------------------------------------------------
    # Buttons and InputBox for updating existing item in list

    # Global variables
    global nameOfItem
    global quantityOfItem

    updateQuantityHeading = tk.Label(buttonsFrame,text="Update Quantity",font=('Arial', 15, 'bold'),bg=pink)
    updateQuantityHeading.grid(row=0,column=5,padx=5,pady=(40,10),ipadx=2,ipady=1)

    # Take Item name from owner
    uName = tk.Label(buttonsFrame, text='Name:', font=('Arial', 14, 'italic'),bg=pink)
    uName.grid(row=1, column=4,padx=(10,0),pady=(10,5))
    updateName = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    updateName.grid(row=1, column=5,padx=10,pady=(10,5),ipadx=5,ipady=5)


    # Take Quantity from owner
    uQuantity =tk.Label(buttonsFrame, text='Quantity:', font=('Arial', 14, 'italic'),bg=pink)
    uQuantity.grid(row=2, column=4,padx=(10,0),pady=(5,10))
    updateQuantity = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    updateQuantity .grid(row=2, column=5,padx=10,pady=(5,10),ipadx=5,ipady=5)

    # Initializing local variables to global variables
    nameOfItem = updateName
    quantityOfItem = updateQuantity

# ----------------------------------------------------------------------------------------------
    global removeItemName
    removeItemHeading = tk.Label(buttonsFrame,text="Remove Item",font=('Arial', 15, 'bold'),bg=pink)
    removeItemHeading.grid(row=5,column=3,columnspan=3,padx=(0,80),pady=(40,10),ipadx=2,ipady=1)

    # Take Item name from owner
    rName = tk.Label(buttonsFrame, text='Name:', font=('Arial', 14, 'italic'),bg=pink)
    rName.grid(row=6, column=2,columnspan=3,padx=(0,80),pady=(10,5))
    removeName = tk.Entry(buttonsFrame,width=15,font=('Arial',14),)
    removeName.grid(row=6, column=3,columnspan=3,padx=(0,80),pady=(10,5),ipadx=5,ipady=5)


    # Initializing local variables to global variables
    removeItemName = removeName



# ----------------------------------------------------------------------------------------------

# Callback function for adding the item to the list
def addItem():
    # Verify the input from the user and check if the space in the list is free.
    Name = name.get()
    Price = price.get()
    Quantity = quantity.get()
    if vANDv.validate(Name,Price,Quantity,inventory_list) and vANDv.listLimitCheck(inventory_list):
        messagebox.showinfo("info",f"items added!\n{name.get()}\n{price.get()}\n{quantity.get()}")
        print(name.get(),int(price.get()),int(quantity.get()))
        # Update the list
        print("Names from additem()")
        print(name.get(),int(price.get()),int(quantity.get()))
        write.addToList(name.get(),int(price.get()),int(quantity.get()))
    
    name.delete(0,tk.END)
    price.delete(0,tk.END)
    quantity.delete(0,tk.END) 

# ----------------------------------------------------------------------------------------------

# Callback function for updating the quantity of an item
def updateQuantity():
    name = nameOfItem.get().lower()
    quantity = quantityOfItem.get()
    if vANDv.findItem(name,inventory_list) and vANDv.quantityValidation(quantity):
        write.updateToItem([name,quantity])

    nameOfItem.delete(0,tk.END)
    quantityOfItem.delete(0,tk.END)

def removeItem():
    name = removeItemName.get()
    
    if vANDv.findItem(name,inventory_list):
        write.removeItem(name)


    removeItemName.delete(0,tk.END)



# Validating name
# def namingInstructions(event = None):
#     messagebox.showinfo("Naming Process","The name should be combination of Item Name and Item Price separated by '-'\nE.g:- Name - shirt\nPrice - 300\nName - 'shirt-300'")
#     name.unbind("<FocusIn>")
