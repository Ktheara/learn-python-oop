# Polymorphism means having many forms.

class Main:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Asia(Main):
    def detail(self):
        print(f"{self.name} from asia work as {self.position}")

class Africa(Main):
    def detail(self):
        print(f"{self.name} from africa work as {self.position}")

employees = [Asia("Nabi", "Accountant"),
            Africa("Bomay", "HR"),
            Asia("Nabty", "Leader"),
            Africa("Ream", "workder")]

print("list of employees:")
for employee in employees:
    employee.detail()