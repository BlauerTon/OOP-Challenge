class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Do not let hunger go below 0
        self.happiness += 1

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Do not let energy go above 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Do not let energy go below 0
        self.happiness += 2
        self.hunger += 1

    def get_status(self):
        print(f"Pet {self.name} is feeling:")
        print(f"Hunger: {self.hunger}/{10} (Full to Very Hungry)")
        print(f"Energy: {self.energy}/{10} (Tired to Fully Rested)")
        print(f"Happiness: {self.happiness}/{10} (Unhappy to Super Happy)")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"Pet {self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"Pet {self.name} doesn't know any tricks yet.")
