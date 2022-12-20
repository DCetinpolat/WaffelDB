import tkinter as tk
import pymysql

class OrderWaffles:
    def __init__(self, master):
        self.master = master
        master.title("Waffel bestellung")
        self.price=0

        self.class_label = tk.Label(master, text="Klasse:")
        self.number_label = tk.Label(master, text="Anzahl:")
        self.room_label = tk.Label(master, text="Raum:")
        self.time_label = tk.Label(master, text="Uhrzeit:")


        self.price_text = tk.StringVar()
        self.price_text.set(f"Price: {self.price}")
        self.price_label = tk.Label(master, textvariable=self.price_text)



        self.class_entry = tk.Entry(master)
        self.number_entry = tk.Entry(master)
        self.room_entry = tk.Entry(master)
        self.time_entry = tk.Entry(master)
        self.price_entry = tk.Entry(master)
        self.number_entry.bind("<KeyRelease>", self.calculate_price)
        self.price_entry.bind("<KeyRelease>", self.calculate_price)


        self.submit_button = tk.Button(master, text="Bestellen", command=self.submit)


        self.class_label.grid(row=0, column=0)
        self.class_entry.grid(row=0, column=1)
        self.number_label.grid(row=1, column=0)
        self.number_entry.grid(row=1, column=1)
        self.room_label.grid(row=2, column=0)
        self.room_entry.grid(row=2, column=1)
        self.time_label.grid(row=3, column=0)
        self.time_entry.grid(row=3, column=1)
        self.price_label.grid(row=4, column=0)
        self.submit_button.grid(row=5, column=0, columnspan=2)

    def submit(self):
        class_text = self.class_entry.get()
        number_text = self.number_entry.get()
        room_text = self.room_entry.get()
        time_text = self.time_entry.get()
        price_text = self.price_entry.get()

        conn = pymysql.connect(host="localhost", user="username", password="password", db="waffles")


        cursor = conn.cursor()


        query = f"INSERT INTO orders (class, number, price, room, time) VALUES ({class_text}, {number_text}, {price_text}, {room_text}, {time_text})"

        cursor.execute(query)


        conn.commit()


        conn.close()


        print("Waffle order successfully submitted!")

    def calculate_price(self, event):

        number = self.number_entry.get()

        self.price = int(number) * 1


        self.price_text.set(f"Preis: {self.price}€")


# Create the Tkinter window
root = tk.Tk()
app = OrderWaffles(root)
root.geometry('330x330')
root.mainloop()
