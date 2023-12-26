# Wizard Application

class Wizard:
    def __init__(self):
        self.details = {
            "Name": None,
            "Email": None,
            "Birth Date": None,
            "City": None,
            "Street": None,
            "Number": None,
            "Social Media": None,
            "Hobbies": None
        }
        self.completed_phases = []

    def start_wizard(self):
        print("Welcome to the Wizard!")
        while True:
            choice = input("Menu: 1) Start New 2) Continue: ")
            if choice == "1":
                self.run_phase_1()
            elif choice == "2":
                phase = int(input("Enter phase number: "))
                if phase in self.completed_phases:
                    self.run_phase(phase)
                else:
                    print("You can't access this phase yet. Please complete previous phases.")
            else:
                print("Invalid choice!")

    def run_phase_1(self):
        print("Phase 1: Enter your details")
        name = input("Enter your full name (First Name Last Name): ")
        email = input("Enter your email address: ")
        birth_date = input("Enter your birth date (dd/MM/yy): ")
        # Add validation and processing logic for inputs
        self.details["Name"] = name
        self.details["Email"] = email
        self.details["Birth Date"] = birth_date
        self.completed_phases.append(1)
        self.summary()


    def run_phase(self, phase):
        if phase == 1:
            self.run_phase_1()
        elif phase == 2:
            pass # self.run_phase_2()
        elif phase == 3:
            pass # self.run_phase_3()

    def summary(self):
        print("\nSummary:")
        for key, value in self.details.items():
            print(f"{key}: {value}")
        print("\n")


# Example usage
wizard = Wizard()
wizard.start_wizard()
