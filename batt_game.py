import sys

class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.receive_damage(self.damage)
        print(f"The {self.name} damaged the {target.name}!")

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

def select_character():
    characters = {
        "1": Character("Wizard", 70, 150),
        "2": Character("Elf", 100, 100),
        "3": Character("Human", 150, 20)
    }

    while True:
        print("Welcome to the Battle Game!")
        print("Choose your character: ")
        for key, character in characters.items():
            print(f"{key}. {character.name}")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4" or choice.lower() == "exit":
            print("Goodbye!")
            sys.exit(0)

        selected_character = characters.get(choice)
        if selected_character:
            return selected_character
        else:
            print("Unknown character. Please try again.")

def battle(player, dragon):
    while True:
        player.attack(dragon)
        print(f"Dragon's HP: {dragon.hp}")

        if dragon.hp <= 0:
            print("The Dragon has lost the battle!")
            break

        dragon.attack(player)
        print(f"Your HP: {player.hp}")

        if player.hp <= 0:
            print("You have lost the battle!")
            break

def play_game():
    player = select_character()
    dragon = Character("Dragon", 300, 50)
    battle(player, dragon)

    while True:
        play_again = input("Do you want to play again? (Y/N): ").lower()

        if play_again == "n":
            print("Goodbye!")
            sys.exit(0)
        elif play_again == "y":
            play_game()
        else:
            print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    play_game()
