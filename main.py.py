import tkinter as tk
import pymysql

class OrderWaffles:
    def __init__(self, master):
        self.master = master
        master.title("Waffel bestellung")
        self.price=0

        # Create labels for the different form fields
        self.class_label = tk.Label(master, text="Klasse:")
        self.number_label = tk.Label(master, text="Anzahl:")
        self.room_label = tk.Label(master, text="Raum:")
        self.time_label = tk.Label(master, text="Uhrzeit:")


        self.price_text = tk.StringVar()
        self.price_text.set(f"Price: {self.price}")
        self.price_label = tk.Label(master, textvariable=self.price_text)


        # Create entry fields for the form data
        self.class_entry = tk.Entry(master)
        self.number_entry = tk.Entry(master)
        self.room_entry = tk.Entry(master)
        self.time_entry = tk.Entry(master)
        self.price_entry = tk.Entry(master)
        self.number_entry.bind("<KeyRelease>", self.calculate_price)
        self.price_entry.bind("<KeyRelease>", self.calculate_price)

        # Create a submit button
        self.submit_button = tk.Button(master, text="Bestellen", command=self.submit)

        # Lay out the form fields and submit button using grid layout
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
        # Retrieve the data from the form fields
        class_text = self.class_entry.get()
        number_text = self.number_entry.get()
        room_text = self.room_entry.get()
        time_text = self.time_entry.get()
        price_text = self.price_entry.get()

        conn = pymysql.connect(host="localhost", user="username", password="password", db="waffles")

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Create the INSERT query
        query = f"INSERT INTO orders (class, number, price, room, time) VALUES ({class_text}, {number_text}, {price_text}, {room_text}, {time_text})"

        # Execute the query
        cursor.execute(query)

        # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        conn.close()

        # Print a success message
        print("Waffle order successfully submitted!")

    def calculate_price(self, event):
        # Retrieve the number and time from the form fields
        number = self.number_entry.get()

        # Calculate the price based on the number and time
        # For simplicity, we will assume a fixed price of 10 per waffle
        # and a surcharge of 5 for orders placed during peak hours (8am-12pm)

        self.price = int(number) * 1

        # Update the price label with the calculated price
        self.price_text.set(f"Preis: {self.price}€")


# Create the Tkinter window
root = tk.Tk()
app = OrderWaffles(root)
root.geometry('330x330')
root.mainloop()
