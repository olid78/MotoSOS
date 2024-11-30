import tkinter as tk
from tkinter import messagebox

# Databases
user_database = {
    
}
garage_database = {
    "Garage A": "Sylhet Tamabil",
    "Garage B": "Gulapgonj Charmuhoni Point",
    "Garage C": "Sylhet-Dhaka Main Road"
}

class CarRepairServiceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MotoSOS - Roadside Emergency Solutions")
        
        self.current_user = None

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.show_login()

    def show_login(self):
        self.clear_frame()
        tk.Label(self.frame, text="Login", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self.frame, text="Username").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password").pack()
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.pack()

        tk.Button(self.frame, text="Login", command=self.login_user).pack(pady=5)
        tk.Button(self.frame, text="Register", command=self.show_register).pack()

    def show_register(self):
        self.clear_frame()
        tk.Label(self.frame, text="Register", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self.frame, text="Username").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password").pack()
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.pack()

        tk.Button(self.frame, text="Register", command=self.register_user).pack(pady=5)
        tk.Button(self.frame, text="Back to Login", command=self.show_login).pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in user_database:
            messagebox.showerror("Error", "User already exists!")
            return
        user_database[username] = password
        messagebox.showinfo("Success", "Registration successful!")
        self.show_login()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in user_database and user_database[username] == password:
            self.current_user = username
            self.show_service_request()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def show_service_request(self):
        self.clear_frame()
        tk.Label(self.frame, text="Request Service", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.frame, text="Current Location").pack()
        self.location_entry = tk.Entry(self.frame)
        self.location_entry.pack()

        tk.Label(self.frame, text="Is there an accident? (yes/no)").pack()
        self.accident_entry = tk.Entry(self.frame)
        self.accident_entry.pack()

        tk.Label(self.frame, text="How many vehicles are involved?").pack()
        self.vehicles_entry = tk.Entry(self.frame)
        self.vehicles_entry.pack()

        tk.Label(self.frame, text="Are there any injuries? (yes/no)").pack()
        self.injuries_entry = tk.Entry(self.frame)
        self.injuries_entry.pack()

        tk.Label(self.frame, text="What is the issue?").pack()
        self.issue_entry = tk.Entry(self.frame)
        self.issue_entry.pack()

        tk.Button(self.frame, text="Submit", command=self.handle_service_request).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.show_login).pack()

    def handle_service_request(self):
        location = self.location_entry.get()
        accident_reported = self.accident_entry.get().lower()
        vehicles_involved = self.vehicles_entry.get()
        injuries_reported = self.injuries_entry.get().lower()
        issue = self.issue_entry.get()
        
        if accident_reported == "yes":
            injury_message = "Ambulance dispatched to your location. Please remain calm, help is on the way."
            if injuries_reported == "yes":
                injury_message += "\nMedical assistance is also being prepared."
            messagebox.showinfo("Response", injury_message)
        else:
            garages_info = "\n".join(f"{garage}: {address}" for garage, address in garage_database.items())
            messagebox.showinfo(
                "Response",
                f"Mechanic is being sent to your location:\n\nIssue: {issue}\nVehicles Involved: {vehicles_involved}\n\nNearby Garages:\n{garages_info}"
            )

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CarRepairServiceApp(root)
    root.mainloop()