import tkinter as tk
import components as cmp
import validationAndVerification as vANDv
from tkinter import messagebox
from datetime import datetime
import write_bill_invoice as wbi
import asyncio


items = [item[0] for item in cmp.inventory_list]


def billWindow():
    global window
    window = tk.Toplevel()
    window.title("Generate Bill")
    window.attributes("-fullscreen", True)

    # root.transient(window)
    window.grab_set_global()

    # declare global variables.
    global customerNameEntry
    global customerContactEntry
    global item_var
    global quantity_entry
    global listbox


    # colors
    bgColor = 'azure3'
    # Calculate the center of the window
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    frame_width = 300  # Adjust the frame width as needed
    frame_height = 200  # Adjust the frame height as needed
    x_center = (window_width - frame_width) / 2
    y_center = (window_height - frame_height) / 2

    # Create a frame to contain all elements
    frame = tk.Frame(window,bg=bgColor)
    frame.place(relx=0.5, rely=0.5, anchor="center",)  # Place the frame at the center

    # Create the label
    billHeading = tk.Label(frame, text="Enter details", font=('Arial', 20, 'bold'),bg=bgColor)
    billHeading.grid(row=0, column=0,columnspan=2, pady=(20, 10), sticky="ew")  # Center horizontally

    # Take customer name
    customerNameLabel = tk.Label(frame,text="Enter Customer Name :",font=('Arial', 14, 'normal'),bg=bgColor)
    customerNameLabel.grid(row=1,column=0,pady=5,padx=(0,200),sticky='nsew')
    customerNameEntry = tk.Entry(frame,width=20,font=('Arial',14),)
    customerNameEntry.grid(row=1,column=0,columnspan=2,padx=(300,10),pady=5,ipadx=2,ipady=1,sticky='nsew')


    # Take customer mobile number
    customerContact = tk.Label(frame,text="Enter Contact No. :",font=('Arial', 14, 'normal'),bg=bgColor)
    customerContact.grid(row=2,column=0,pady=5,padx=(0,160))

    customerContactEntry = tk.Entry(frame,width=20,font=('Arial',14),)
    customerContactEntry.grid(row=2,column=0,columnspan=2,padx=(300,10),pady=5,ipadx=2,ipady=1)
    
    # select item
    selectLabel = tk.Label(frame,text="Select Item :",font=('Arial',14),bg=bgColor)
    selectLabel.grid(row=3,column=0,padx=(0,110),pady=5)
    
    # StringVar to hold the selected item
    item_var = tk.StringVar(frame)
    item_var.set("Select Item")  # Set initial value

    # Dropdown list for selecting items
    item_dropdown = tk.OptionMenu(frame, item_var, *items,)
    item_dropdown.grid(row=3,column=0,columnspan=2,padx=(172,0),pady=5)


    # Take quantity of item
    quantityLabel = tk.Label(frame,text="Enter Quantity :",font=('Arial', 14, 'normal'),bg=bgColor)
    quantityLabel.grid(row=4,column=0,pady=5,padx=(0,130))

    quantity_entry = tk.Entry(frame,width=10,font=('Arial',14),bg=bgColor)
    quantity_entry.grid(row=4,column=0,padx=(240,20),pady=5,ipadx=2,ipady=1)

    # Create ListBox
    listbox = tk.Listbox(frame, width=50, height=10,bg=bgColor)
    listbox.grid(row=5,column=0,columnspan=2,pady=10,padx=(100,0))

    # Add button for confirming item for purchase
    addButton = tk.Button(frame,text='Add',width=5,command=add_item_to_listbox)
    addButton.grid(row=4,column=0,padx=(420,0),pady=5)

    # Create the cancel button
    cancelButton = tk.Button(frame, text="Cancel", bg='red', width=8, command=window.destroy, cursor='hand2',font=('Arial',12,'bold'))
    cancelButton.grid(row=20, column=0,columnspan=2,padx=(0,50), pady=10,)  # Center horizontally

    # Create Generate button
    generateButton = tk.Button(frame, text="Generate", bg='green1', width=10, command=generateBill, cursor='hand2',font=('Arial',12,'bold'))
    generateButton.grid(row=20, column=0,columnspan=2,padx=(200,0), pady=10,) # Center horizontally

    # Run the Tkinter event loop
    window.mainloop()


# Working of add button
def add_item_to_listbox():
    # Get selected item and quantity from the dropdown and entry widgets
    try:
        selected_item = item_var.get()
        quantity = int(quantity_entry.get())
        quantityLimitExceed = False
        quantityLimitZero = False
        if type(quantity) == int:
            for item in cmp.inventory_list:
                if selected_item == item[0]:
                    price = item[1]
                    if int(item[2]) < quantity:
                        print(int(item[2]))
                        quantityLimitExceed = True
                    elif int(item[2]) == 0:
                        print(int(item[2]))
                        quantityLimitZero = True
                    break
    
    
        # Add item and quantity to the listbox
        if vANDv.itemValidation(selected_item,quantity,quantityLimitExceed,quantityLimitZero,window):
            if selected_item and quantity:  # Check if both item and quantity are provided
                listbox.insert(tk.END, f"{selected_item} {price} {quantity}")
                # Clear entry widgets for next input
                item_var.set("Select Item")  # Clear the dropdown selection
                quantity_entry.delete(0, tk.END)  # Clear the quantity entry
    except:
        messagebox.showerror("Invalid Quantity","Please Enter valid quantity!",parent=window)
        quantity_entry.delete(0,tk.END)
    


# Generating the bill
def generateBill():
    customer_name = customerNameEntry.get()
    customer_contact = customerContactEntry.get()
    if vANDv.customerDetailsValidator(customer_name,customer_contact,window,listbox):
        asyncio.run(wbi.generateInvoice(listbox, customer_name, customer_contact,window))



