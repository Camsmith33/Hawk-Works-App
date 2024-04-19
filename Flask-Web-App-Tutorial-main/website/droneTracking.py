#CLass with four objects, each will be a drone
#Have them check out when checkout buttom is clicked and change the status to checked out
#Have their status change to available when check in buttom is clicked

class Drone:
    def __init__(self, name):
        self.name = name
        self.status = "Available"

    def check_out(self):
        if self.status == "Available":
            self.status = "Checked Out"
            print(f"{self.name} has been checked out.")
        else:
            print(f"{self.name} is already checked out.")

    def check_in(self):
        if self.status == "Checked Out":
            self.status = "Available"
            print(f"{self.name} has been checked in.")
        else:
            print(f"{self.name} is already available.")

# Creating drone objects with names
drone1 = Drone("Drone 1")
drone2 = Drone("Drone 2")
drone3 = Drone("Drone 3")
drone4 = Drone("Drone 4")

# Text-based menu
while True:
    print("\nMenu:")
    print("1. Check Out a Drone")
    print("2. Check In a Drone")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        drone_name = input("Enter the name of the drone to check out: ")
        if drone_name == "Drone 1":
            drone1.check_out()
        elif drone_name == "Drone 2":
            drone2.check_out()
        elif drone_name == "Drone 3":
            drone3.check_out()
        elif drone_name == "Drone 4":
            drone4.check_out()
        else:
            print("Invalid drone name")

    elif choice == "2":
        drone_name = input("Enter the name of the drone to check in: ")
        if drone_name == "Drone 1":
            drone1.check_in()
        elif drone_name == "Drone 2":
            drone2.check_in()
        elif drone_name == "Drone 3":
            drone3.check_in()
        elif drone_name == "Drone 4":
            drone4.check_in()
        else:
            print("Invalid drone name")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")