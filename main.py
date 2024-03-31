import tkinter as tk
# from inventoryList import inventory_list
import components as cmp
from bill_window import billWindow


def mainWindow():
    # Create the main root
    root = tk.Tk()
    root.title("Billing System")
    root.config(bg="lavender")

    # Maximize the window
    root.attributes('-fullscreen', True)

    # Create a label for the shop name
    shop_name_label = tk.Label(root, text="ALSA DRESSES", font=("Arial", 38), fg='green',)
    shop_name_label.grid(row=0, column=1, columnspan=2,pady=20, sticky="n",)

    # Create frame for displaying list of items
    tableFrame = tk.Frame(root,bg='lavender',height=500,width=700)
    tableFrame.grid(row=1,column=1,sticky="nsew",padx=(20,10),pady=(50,20))

    # Filling the list data into the table 
    cmp.fillDataInTable(tableFrame)


    # Create frame for adding or updating items from the list
    buttonsFrame = tk.Frame(root,bg="pink",width=500,height=500,border=2)
    buttonsFrame.grid(row=1,column=2,sticky="nsew",padx=10,pady=20)

    # Adding widgets inside the frame
    cmp.buttonFrameComponents(buttonsFrame)

    # Add Button
    addItemButton = tk.Button(buttonsFrame,text="Add Items", command=cmp.addItem,height=1,width=7,font=('Times New Roman',16,'normal'),bg='#007BFF',cursor='hand2',fg='black')
    addItemButton.grid(row=4,column=3,padx=20,pady=20,ipadx=2,ipady=1)

    # Update Quantity Button
    updateItemButton = tk.Button(buttonsFrame,text="Update Quantity", command=cmp.updateQuantity,height=1,width=12,font=('Times New Roman',16,'normal'),bg='#007BFF',cursor='hand2',fg='black')
    updateItemButton.grid(row=4,column=5,padx=20,pady=20,ipadx=2,ipady=1)

    # Remove Item Button
    removeItemButton = tk.Button(buttonsFrame,text="Remove Item", command=cmp.removeItem,height=1,width=10,font=('Times New Roman',16,'normal'),bg='#007BFF',cursor='hand2',fg='black')
    removeItemButton.grid(row=7,column=3,columnspan=3,padx=(0,80),pady=20,ipadx=2,ipady=1)

    # Generate Bill Button
    GenerateBill = tk.Button(root,text="Generate Bill",width=12,bg='gold',font=('Times New Roman',18,'normal'),command=billWindow,cursor='hand2')
    GenerateBill.grid(row=20,column=2,columnspan=3,padx=5,pady=(5,20),ipadx=1,ipady=1)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=root.destroy,height=1,width=7,font=('Times New Roman',16,'normal'),bg='tomato1',cursor='hand2',)
    exit_button.grid(row=20, column=0,columnspan=2,pady=(5,20))

    # Run the main loop
    root.mainloop()


# Create bill Window

if __name__ == "__main__":
    mainWindow()