import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 10
        self.hunger = 0
        self.energy = 10
        self.alive = True

    def play(self):
        print(f"{self.name} грає!")
        self.happiness += 1
        self.hunger += 1
        self.energy -= 1

    def feed(self):
        print(f"{self.name} їсть!")
        self.hunger -= 1

    def sleep(self):
        print(f"{self.name} спить!")
        self.energy += 2
        self.hunger += 1

    def check_status(self):
        if self.happiness <= 0:
            print(f"{self.name} сумний. Помирає від суму.")
            self.alive = False
        elif self.hunger >= 10:
            print(f"{self.name} голодний. Помирає від голоду.")
            self.alive = False
        elif self.energy <= 0:
            print(f"{self.name} втомлений. Помирає від виснаження.")
            self.alive = False

    def show_stats(self):
        print(f"{self.name}:")
        print(f"  Радість: {self.happiness}")
        print(f"  Голод: {self.hunger}")
        print(f"  Енергія: {self.energy}")

    def simulate_day(self):
        action = random.choice(["play", "feed", "sleep"])
        if action == "play":
            self.play()
        elif action == "feed":
            self.feed()
        elif action == "sleep":
            self.sleep()
        self.check_status()
        self.show_stats()


cat = Pet(name="Барсік")
for day in range(10):
    cat.simulate_day()
    if not cat.alive:
        break
