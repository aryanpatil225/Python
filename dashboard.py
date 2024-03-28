import tkinter as tk

def submit_ticket():
    # Get values from input fields
    name = name_entry.get()
    organizer_name = organizer_name_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    location = location_entry.get()
    age = age_entry.get()
    game = game_entry.get()

    # Do something with the ticket information (e.g., save to a file, print to console)
    print("Name:", name)
    print("Organizer Name:", organizer_name)
    print("Date:", date)
    print("Time:", time)
    print("Location:", location)
    print("Age:", age)
    print("Game:", game)

# Create the main window
root = tk.Tk()
root.title("Ticketing App")

# Create and place input fields and labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

organizer_name_label = tk.Label(root, text="Organizer Name:")
organizer_name_label.grid(row=1, column=0, padx=10, pady=5)
organizer_name_entry = tk.Entry(root)
organizer_name_entry.grid(row=1, column=1, padx=10, pady=5)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=2, column=0, padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, padx=10, pady=5)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=3, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=3, column=1, padx=10, pady=5)

location_label = tk.Label(root, text="Location:")
location_label.grid(row=4, column=0, padx=10, pady=5)
location_entry = tk.Entry(root)
location_entry.grid(row=4, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=5, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=5, column=1, padx=10, pady=5)

game_label = tk.Label(root, text="Game:")
game_label.grid(row=6, column=0, padx=10, pady=5)
game_entry = tk.Entry(root)
game_entry.grid(row=6, column=1, padx=10, pady=5)

# Create and place submit button
submit_button = tk.Button(root, text="Submit", command=submit_ticket)
submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

# Run the Tkinter event loop
root.mainloop()
