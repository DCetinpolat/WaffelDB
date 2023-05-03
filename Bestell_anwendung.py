import tkinter as tk
import mysql.connector
import customtkinter
import re

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


conn = mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="waffles")
cursor = conn.cursor()

class OrderWaffles(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Waffel bestellung")
        self.price=0
 


        self.anzahl_entry = customtkinter.CTkEntry(master=self, placeholder_text="Anzahl",width=200,height=30)
        self.anzahl_entry.place(x=67, y=30)


        self.zeit_entry = customtkinter.CTkEntry(master=self, placeholder_text="Uhrzeit",width=200,height=30)
        self.zeit_entry.place(x=67, y=70)

        self.button=customtkinter.CTkButton(master=self, text="Bestellen", command=self.submit,width=200,height=30)
        self.button.place(x=67, y=150)

        self.price_text = customtkinter.StringVar()
        self.price_text.set(f"Preis: {self.price}")
        self.price_label = customtkinter.CTkLabel(master=self, textvariable=self.price_text)


        self.price_entry = customtkinter.CTkEntry(master=self, placeholder_text="Preis",width=200,height=30)
        self.anzahl_entry.bind("<KeyRelease>", self.calculate_price)
        self.price_entry.bind("<KeyRelease>", self.calculate_price)
        self.price_label.place(x=67, y=110)


    def submit(self):
        # Retrieve the data from the form fields
        anzahl_text = self.anzahl_entry.get()
        preis_text = self.price
        zeit_text = self.zeit_entry.get()
        status= ("nicht_erledigt")
        query1= "SELECT COUNT(id) FROM orders;"
        cursor.execute(query1)
        nummer=cursor.fetchone()
        nummer = nummer[0] + 1
        bestellnummer="Ihre Bestellnummer lautet: "
        print(nummer)
       

        if not anzahl_text or not zeit_text:
            tk.messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
            return
        elif not re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", zeit_text):
            tk.messagebox.showerror("Fehler","Ungültige Uhrzeit. Bitte geben Sie eine Uhrzeit im Format HH:MM ein.")
            return
        try:
            anzahl = int(anzahl_text)
        except ValueError:
            tk.messagebox.showerror("Fehler","Anzahl muss eine ganze Zahl sein.")
            return
            
        tk.messagebox.showinfo ("Bestellung",bestellnummer+ str(nummer)) 

        query2 = f"INSERT INTO orders ( anzahl, preis, uhrzeit,status,abgeholt,storniert) VALUES ( '{anzahl_text}', '{preis_text}', '{zeit_text}', '{status}','0','0')"

        cursor.execute(query2)


        conn.commit()


        print("Waffle order successfully submitted!")

    def calculate_price(self, event):
        number = int(self.anzahl_entry.get())


        number=int(number)
        self.price = int(number) * 1

        self.price_text.set(f"Preis: {self.price}€")



app= OrderWaffles()
app.geometry('330x280')
app.mainloop()
