#DND choose your own adventure game

#Character creation
#This is a simple game so the classes and races will be limited

class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.attributes = self.generate_attributes()

    #generate attributes
    def generate_attributes(self):
        #Base Attributes for all characters:
        attributes = {
            "Strength": 8,
            "Dexterity": 8,
            "Constitution": 8,
            "Intelligence": 8,
            "Wisdom": 8,
            "Charisma": 8,
            }
        point_buy_costs = {
            8: 0,
            9: 1,
            10: 2,
            11: 3,
            12: 4,
            13: 5,
            14: 6,
            15: 9,
        }
        #Total Points to spend
        points_remaining = 27
        print("\n --- Point buy System ---")
        print("Choose you stat distribution")
        print(" You have 27 points to distribute")
        print("Base stats start at 8. Costs are as follows:")
        print("8: 0 | 9: 1 | 10: 2 | 11: 3 | 12: 4 | 13: 5 | 14: 7 | 15: 9")
#Point allocatoin
        for attribute in attributes:
            while True:
                try:
                    print(f"\nCurrent points reminaing: {points_remaining}")
                    print(f"Current stat{attribute}: {attributes[attribute]}")
                    new_value = int(input(f"Enter the desired value for {attribute}(8-15): "))
                    #validate input
                    if new_value <8 or new_value > 15:
                        print("Score must be between 8 and 15. Please re enter score")
                        continue
                    #calculate cost of the new value
                    cost = point_buy_costs[new_value] - point_buy_costs[attributes[attribute]]
                    #check if the player has enough points to make the change
                    if cost > points_remaining:
                        print(f"You do not have enough points to make that change. Please re enter score")
                        continue
                    #apply the change
                    attributes[attribute] = new_value
                    points_remaining -= cost
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 8 and 15")
        print("\n--- Final Stats ---")
        for key, value in attributes.items():
            print(f"{key}: {value}")
        print(f"Ponints remaining: {points_remaining}")
    
    # Adjust attributes based on race
        if self.race == "Human":
            attributes["Strength"] += 1
            attributes["Dexterity"] += 1
            attributes["Constitution"] += 1
            attributes["Intelligence"] += 1
            attributes["Wisdom"] += 1
            attributes["Charisma"] += 1
        elif self.race == "Dwarf":
            attributes["Constitution"] += 2
            attributes["Strength"] += 2
        elif self.race == "Elf":
            attributes["Intelligence"] += 2
            attributes["Wisdom"] += 2
        elif self.race == "Halfling":
            attributes["Dexterity"] += 2
            attributes["Charisma"] += 2
        return attributes
#Character Display
    def display_character(self):
        print('\n--- Character Summary ---')
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print('\nAttributes')
        for key, value in self.attributes.items():
            print(f"{key}: {value}")
        print("-------------------------------\n")
#Race selection
def choose_race():
    race = ["Human", "Dwarf", "Elf", "Halfling"]
    print("Choose your race: ")
    for i, r in enumerate(race, 1):
        print(f"{i}. {r}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1  <= choice  <= len(race):
                return race[choice - 1]
            else:
                print ("Invalid choice, Please try again.")
        except ValueError:
                print("Please enter a valid number.")

#Class Selection
def choose_class():
    classes = ["Fighter", "Ranger", "Paladin", "Monk"]
    print("Choose your class: ")
    for i, c in enumerate(classes, 1):
        print(f"{i}. {c}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(classes): 
                return classes[choice - 1]
            else:
                print ("Invalid choice, Please try again.")
        except ValueError:
                print("Please enter a valid number.")

def character_creation():
    print("Hello Adventurer, Lets create your character")
    name = input("Enter your character's name: ")
    race = choose_race()
    char_class = choose_class()

    #Create the character
    character = Character(name, race, char_class)
    character.display_character()

    while True:
        print("\nDo you want to continue with this character or remake it?")
        choice = input("Enter 'yes' to continue or 'no' to remake: ")
        if choice.lower() == 'yes':
            print("Your journey bgins now adventurer!")
            break
        elif choice.lower() == 'no':
            print("Let's start again!")
            character_creation()
        else:
            print("Invalid choice, Please Try again")

#Game Function
if __name__ == "__main__":
    character_creation()
