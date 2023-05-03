import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *
from tkinter.ttk import *



# Verbindung mit der MySQL-Datenbank herstellen
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="waffles"
)

# tkinter-Anwendung erstellen
root = tk.Tk()
root.title("Waffles Orders")


style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

#style.map('mystyle.Treeview', background=[('erledigt=nicht_erledigt', 'green')])

# Treeview erstellen


tree = ttk.Treeview(root,style="mystyle.Treeview", columns=("Nr", "anzahl", "preis", "uhrzeit","status","abgeholt"), show="headings")
tree.column('anzahl',anchor='center')
tree.heading("anzahl", text="Anzahl")
tree.column('uhrzeit',anchor='center')
tree.heading("uhrzeit", text="Uhrzeit")
tree.column('preis',anchor='center')
tree.heading("preis", text="Preis")
tree.column('Nr',anchor='center')
tree.heading("Nr", text="Nr")
tree.column('status',anchor='center')
tree.heading("status", text="Status")
tree.column('abgeholt',anchor='center')
tree.heading("abgeholt", text="Abgeholt")

tree.tag_configure('erledigt', background='limegreen')
tree.tag_configure('nicht_erledigt', background='tomato')

tree.pack()

# Funktion zum Abrufen und Anzeigen der Daten aus der Tabelle "orders"
def show_orders():
    tree.delete(*tree.get_children())
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM orders WHERE abgeholt = False and storniert = False")
    rows = mycursor.fetchall()
    mydb.commit()
    for row in rows:
        if row[4] == 'erledigt' :
            tree.insert("", tk.END, values=row, tags=('erledigt',))
        else:
            tree.insert("", tk.END, values=row, tags=('nicht_erledigt',))

    root.after(15000, show_orders)
    






# Funktion zum Markieren einer Bestellung als erledigt
def erledigt(order_id):
    selected_item = tree.selection()
    if selected_item:
        order_id = tree.item(selected_item)["values"][0]
        mycursor = mydb.cursor()
        sql = "UPDATE orders SET status = 'erledigt' WHERE id = %s"
        val = (order_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        show_orders()
    else:
        print("No item selected")

def abgeholt_makieren(order_id):
    selected_item = tree.selection()
    if selected_item:
        order_id = tree.item(selected_item)["values"][0]
        mycursor = mydb.cursor()
        sql = "UPDATE orders SET abgeholt = true WHERE id = %s AND status = 'erledigt'"
        val = (order_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        show_orders()
    else:
        print("No item selected")

def stornieren(order_id):
    selected_item = tree.selection()
    if selected_item:
        order_id = tree.item(selected_item)["values"][0]
        mycursor = mydb.cursor()
        sql = "UPDATE orders SET storniert = true WHERE id = %s"
        val = (order_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        show_orders()
    else:
        print("No item selected")


style.configure('W.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'black')

# Buttons erstellen, die die Funktion "mark_as_done" aufrufen
erledigt_button = ttk.Button(root, text="Erledigt" ,width=15,style='W.TButton', command=lambda: erledigt(1))
erledigt_button.place(height=30, x=480, y=227)

Abgeholt_button = ttk.Button(root, text="Abgeholt" ,width=15,style='W.TButton', command=lambda: abgeholt_makieren(1))
Abgeholt_button.place(height=30, x=600, y=227)

stornier_button = ttk.Button(root, text="Stornieren" ,width=15,style='W.TButton', command=lambda: stornieren(1))
stornier_button.place(height=30, x=10, y=227)

show_orders()
root.geometry("1200x260")
root.mainloop()