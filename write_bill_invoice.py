import tkinter as tk
import asyncio
from datetime import datetime
import write

import os

# Get the directory of the current Python script
current_directory = os.path.dirname(os.path.abspath(__file__))

# If the main file is located in a subfolder, you can navigate up one level
# by using os.path.dirname twice
main_folder = os.path.dirname(current_directory)

# Define the name of the subfolder
program_folder_name = "My-project"
subfolder_name = "Bills"
# Create the path to the subfolder
subfolder_path = os.path.join(main_folder, program_folder_name, subfolder_name)

# Check if the subfolder exists, if not, create it
if not os.path.exists(subfolder_path):
    os.makedirs(subfolder_path)



async def generateInvoice(listbox, customer_name, customer_contact,window):
    list_data = []
    for index in range(listbox.size()):
        item = listbox.get(index).split(" ")
        print(item)
        list_data.append(item)

    file_contents = "=============================================================\n"
    file_contents += "ELECTRONIC STORE\t\t\t\tINVOICE\n"
    file_contents += "\nInvoice: bill\t\tDate: " + datetime.now().strftime("%d/%m/%Y") + "\n"
    file_contents += "Time: " + datetime.now().strftime("%H:%M:%S") + "\n"
    file_contents += "Name of Customer: " + str(customer_name).title() + "\n"
    file_contents += "Contact No: " + str(customer_contact) + "\n"
    file_contents += "=============================================================\n"
    file_contents += "Item\t\tQUANTITY\t\tUNIT PRICE\t\tTOTAL\n"
    file_contents += "-------------------------------------------------------------\n"

    total = 0
    for item in list_data:
        itemName = item[0]
        price = int(item[1])
        quantity = int(item[2])
        s_total = price * quantity
        file_contents += f"{itemName}\t\t  {quantity}\t\t  {price}\t\t  {s_total}\n"
        total += s_total
        
    file_contents += "-------------------------------------------------------------\n"
    file_contents += "\t\t\tTotal: " + str(total) + "\n"
    file_contents += "\nYour discount amount is: " + str(total/10) + "\n"
    file_contents += "Your payable amount is: " + str(total - total/10) + "\n"
    file_contents += "-------------------------------------------------------------\n"
    file_contents += "\nThank You " + customer_name.title() + " for your shopping.\nSee you again!\n"
    file_contents += "============================================================="

    # Modify the contents of the list
    write.modifyList(list_data)

    # Create bill text file with customer name
    # Define the name of the new text file
    file_name = customer_name+".txt"

    # Create the path to the new text file inside the subfolder
    file_name_path = os.path.join(subfolder_path, file_name)                           

    with open(file_name_path, "w") as file:
        file.write(file_contents)

    await display_text_file(customer_name,window)

async def display_text_file(customer_name,window):
    file_name = customer_name+".txt"
    # Create the path to the new text file inside the subfolder
    file_name_path = os.path.join(subfolder_path, file_name)
    with open(file_name_path, "r") as file:
        file_contents = file.read()
        print("file contents are" + file_contents)

    billWindow = tk.Tk()
    billWindow.title("Text File Viewer")

    # Create a Text widget
    text_widget = tk.Text(billWindow, wrap="word")
    text_widget.pack(expand=True, fill="both")

    # Add scrollbar
    scrollbar = tk.Scrollbar(billWindow, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)

    # Insert file contents into the Text widget
    text_widget.insert("1.0", file_contents)
    
    window.destroy()
    billWindow.mainloop()


