import tkinter as tk
from tkinter import messagebox



def validate(name,price,quantity,list):
    try:
        for item in list:
            if name.lower() == item[0]:
                messagebox.showerror("Error","Item already exist!")
                return False
            
        if name != '':
            Name = name.split("-")[1]
        if name == '' or price == '' or quantity == '':
            messagebox.showerror("Empty input", "Please enter details properly!")
            return False
        elif Name != price:
            messagebox.showerror("Price Error","Price must be same as mentioned in the name")
            return False
        elif float(quantity) < 0:
            messagebox.showerror("Error", "Please enter a vaild quantity.")
            quantity.delete(0,tk.END) 
            return False
        elif float(price) < 0:
            messagebox.showerror("Error", "Please enter a vaild quantity.")
            price.delete(0,tk.END)
            return False
        return True
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return False
        name.delete(0,tk.END)

def listLimitCheck(list):
    if len(list) >=15:
        messagebox.showerror("Limit Exceed","List is full")
        return False
    else:
        return True




def findItem(name,list):
    if name == '':
        messagebox.showerror("Error","Please enter name of item")
        return False
    for item in list:
        if item[0].lower() == name.lower():
            return True
    messagebox.showerror("Not Found","Item not found! Please check the item name")
    return False


def quantityValidation(quantity):
    if int(quantity) <0:
        messagebox.showerror("Invalid Input","Please Enter valid quantity!")
        return False
    return True


# Item validation for bill generation
def itemValidation(selectedItem,quantity, limit, zero,window):
    if selectedItem == 'Select Item':
        messagebox.showerror("Input missing", "Please Select Item", parent=window)
        return False
    elif quantity == '':
        messagebox.showerror("Invalid Quantity", "Please Enter Valid Quantity", parent=window)
        return False
    elif limit:
        messagebox.showerror("Item Limit", "Not enough quantity of item!", parent=window)
        return False
    elif zero:
        messagebox.showerror("Out of stock", "Item is out of stock!", parent=window)
        return False
    return True


def customerDetailsValidator(name,contact,window,listbox):
    if name == '':
        messagebox.showerror("Input required","Please Enter details properly!",parent=window)
        return False
    elif len(str(contact)) <10 or len(str(contact)) == '' or len(str(contact))>10 or not contact.isdigit():
        messagebox.showerror("Invalid Contact","Please Valid Contact Number!",parent=window)
        return False
    elif listbox.size() == 0:
        messagebox.showerror("Missing Details","Please enter product details!",parent=window)
        return False
    return True





    

        
           
    