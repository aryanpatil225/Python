import tkinter as tk
from pymongo import MongoClient

# MongoDB Atlas connection string
connection_string = "mongodb+srv://AryanPatil:aryanpatil789@data.lhyx8xg.mongodb.net/?retryWrites=true&w=majority&appName=data"

def submit_ticket():
    # Get values from input fields
    name = name_entry.get()
    event_name = event_name_entry.get()
    organizer_name = organizer_name_entry.get()
    organizer_contact = organizer_contact_entry.get()
    organizer_email = organizer_email_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    location = location_entry.get()
    age = age_entry.get()
    game = game_entry.get()

    # Save ticket information to MongoDB Atlas
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(connection_string)
        db = client.get_database('ticket_database')  # Replace 'ticket_database' with your database name
        tickets_collection = db.tickets

        # Insert ticket data into the collection
        ticket_data = {
            "name": name,
            "event_name": event_name,
            "organizer_name": organizer_name,
            "organizer_contact": organizer_contact,
            "organizer_email": organizer_email,
            "date": date,
            "time": time,
            "location": location,
            "age": age,
            "game": game
        }
        tickets_collection.insert_one(ticket_data)

        print("Ticket information saved successfully to MongoDB Atlas.")
    except Exception as e:
        print("Error saving ticket information:", e)
    finally:
        client.close()

    # Do something with the ticket information (e.g., print to console)
    print("Name:", name)
    print("Event Name:", event_name)
    print("Organizer Name:", organizer_name)
    print("Organizer Contact:", organizer_contact)
    print("Organizer Email:", organizer_email)
    print("Date:", date)
    print("Time:", time)
    print("Location:", location)
    print("Age:", age)
    print("Game:", game)

# Create the main window
root = tk.Tk()
root.title("Organize an Event")

# Set background color
root.configure(bg="black")  # bg-red-500

# Create and place input fields and labels with custom styles
labels_style = {"fg": "red"}  # Red label color
entries_style = {"bg": "#718096"}  # Gray input field color

# Label styles
name_label = tk.Label(root, text="Name:", **labels_style)
event_name_label = tk.Label(root, text="Event Name:", **labels_style)
organizer_name_label = tk.Label(root, text="Organizer Name:", **labels_style)
organizer_contact_label = tk.Label(root, text="Organizer Contact:", **labels_style)
organizer_email_label = tk.Label(root, text="Organizer Email:", **labels_style)
date_label = tk.Label(root, text="Date:", **labels_style)
time_label = tk.Label(root, text="Time:", **labels_style)
location_label = tk.Label(root, text="Location:", **labels_style)
age_label = tk.Label(root, text="Age:", **labels_style)
game_label = tk.Label(root, text="Game:", **labels_style)

# Entry styles
name_entry = tk.Entry(root, **entries_style)
event_name_entry = tk.Entry(root, **entries_style)
organizer_name_entry = tk.Entry(root, **entries_style)
organizer_contact_entry = tk.Entry(root, **entries_style)
organizer_email_entry = tk.Entry(root, **entries_style)
date_entry = tk.Entry(root, **entries_style)
time_entry = tk.Entry(root, **entries_style)
location_entry = tk.Entry(root, **entries_style)
age_entry = tk.Entry(root, **entries_style)
game_entry = tk.Entry(root, **entries_style)

# Grid placement for labels and entries
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry.grid(row=0, column=1, padx=10, pady=5)
event_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
event_name_entry.grid(row=1, column=1, padx=10, pady=5)
organizer_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
organizer_name_entry.grid(row=2, column=1, padx=10, pady=5)
organizer_contact_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
organizer_contact_entry.grid(row=3, column=1, padx=10, pady=5)
organizer_email_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
organizer_email_entry.grid(row=4, column=1, padx=10, pady=5)
date_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
date_entry.grid(row=5, column=1, padx=10, pady=5)
time_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
time_entry.grid(row=6, column=1, padx=10, pady=5)
location_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
location_entry.grid(row=7, column=1, padx=10, pady=5)
age_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
age_entry.grid(row=8, column=1, padx=10, pady=5)
game_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
game_entry.grid(row=9, column=1, padx=10, pady=5)

# Calculate the center position for the window
window_width = 500
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Submit button with custom style
submit_button = tk.Button(root, text="Submit", command=submit_ticket, bg="#4299E1", fg="white", padx=10, pady=5)
submit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Run the Tkinter event loop
root.mainloop()

