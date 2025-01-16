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
            attributes["Wisdom"] += 1
        elif self.race == "Elf":
            attributes["Dexterity"] += 2
            attributes["Intelligence"] += 1
        elif self.race == "Halfling":
            attributes["Dexterity"] += 2
            attributes["Charisma"] += 1

        # Adjust attributes based on class
        if self.char_class == "Ranger":
            attributes["Dexterity"] += 2
            attributes["Wisdom"] += 1
        elif self.char_class == "Paladin":
            attributes["Strength"] += 2
            attributes["Charisma"] += 1
        elif self.char_class == "Monk":
            attributes["Dexterity"] += 2
            attributes["Wisdom"] += 1
        return attributes
#Character Display
    def display_character(self):
        print('\n--- Character Summary ---')
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print('\nAttributes')
        for key, value in self.attributres.items():
            print(f"{key}: {value}")
        print("-------------------------------\n")
#Race selection
def choose_race():
    race = ["Human", "Dwarf", "Elf", "Halfling"]
    print("Choose your race:")
    for i, race in enumerate(race, 1):
        print(f"{i}. {race}")
    while True:
        try:
            choice = int(input("Enter the number of your choice"))
            if 1  <= choice  <= len(races):
                return race[choice - 1]
            else:
                print ("Invalid choice, Please try again.")
        except ValueError:
                print("Please enter a valid number.")

#Class Selection
def choose_class():
    classes = ["Fighter", "Ranger", "Paladin", "Monk"]
    print("Choose your class:")
    for i, classes in enumerate(classes, 1):
        print(f"{i}. {classes}")
    while True:
        try:
            choice = int(input("Enter the number of your choice"))
            if 1 <= choice <= len(classes): 
                return classes[choice - 1]
            else:
                print ("Invalid choice, Please try again.")
         except ValueError:
                print("Please enter a valid number.")

def character_creatoin():
    print("Hello Adventurer, Lets create your character")
    name = input("Enter your character's name: ")
    race = choose_race()
    char_class = choose_class()

    #Create the character
    character = Character(name, race, char_class)
    display_character(character)
    return character

#Game Function
if __name__ == "__main__":
    adventurer = character_creatoin()
    print("Your journy begins now Adventurere!")