import tkinter as tk
from tkinter import ttk
import mysql.connector
import time


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

# Frame für die Listbox mit nicht erledigten Bestellungen
frame_not_done = tk.Frame(root)
frame_not_done.grid(row=0, column=0)

# Label für die Listbox mit nicht erledigten Bestellungen
label_not_done = tk.Label(frame_not_done, text="Wird zubereitet")
label_not_done.configure(fg='red',font=('Calibri', 20,'bold'))
label_not_done.pack()

# Listbox für die nicht erledigten Bestellungen
listbox_not_done = tk.Listbox(frame_not_done)
listbox_not_done.pack()

# Frame für die Listbox mit erledigten Bestellungen
frame_done = tk.Frame(root)
frame_done.grid(row=0, column=1)

# Label für die Listbox mit erledigten Bestellungen
label_done = tk.Label(frame_done, text="Abholbereit")
label_done.configure(fg='green',font=('Calibri', 20,'bold'))
label_done.pack()

# Listbox für die erledigten Bestellungen
listbox_done = tk.Listbox(frame_done)
listbox_done.pack()

# Funktion zum Abrufen und Anzeigen der Daten aus der Tabelle "orders"
def show_orders():
    listbox_not_done.delete(0, tk.END)
    listbox_done.delete(0, tk.END)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM orders WHERE status = 'nicht_erledigt'")
    rows = mycursor.fetchall()
    for row in rows:
        listbox_not_done.insert(tk.END, row[0])
        listbox_not_done.configure(width=55,height=70,font=('Calibri', 20,'bold'))
    mycursor.execute("SELECT id FROM orders WHERE status = 'erledigt' AND abgeholt = False")
    rows = mycursor.fetchall()
    mydb.commit()

    for row in rows:
        listbox_done.insert(tk.END, row[0])
        listbox_done.configure(width=55,height=70,font=('Calibri', 20,'bold'))
       
       
    if not rows:
       listbox_done.insert(tk.END, "Keine abholbereiten Bestellungen")
       listbox_done.configure(width=55,height=70,font=('Calibri', 20,'bold'))

    mycursor.execute("SELECT id FROM orders WHERE status = 'nicht_erledigt'")
    rows = mycursor.fetchall()
    if not rows:
        listbox_not_done.insert(tk.END, "Keine Bestellungen in Bearbeitung")
        listbox_not_done.configure(width=55,height=70,font=('Calibri', 20,'bold'))
    root.after(1000, show_orders)




show_orders()
root.attributes('-fullscreen', True)
root.geometry("1920x1080")
root.mainloop()



