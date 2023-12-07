import sys

def attack(attacker, target):
    target['hp'] -= attacker['damage']
    print(f"The {attacker['name']} damaged the {target['name']}!")

def choose_character():
    while True:
        print("Welcome to the Battle Game!")
        print("Choose your character: ")
        characters = {
            "1": {'name': 'Wizard', 'hp': 70, 'damage': 150},
            "2": {'name': 'Elf', 'hp': 100, 'damage': 100},
            "3": {'name': 'Human', 'hp': 150, 'damage': 20}
        }
        for key, character in characters.items():
            print(f"{key}. {character['name']}")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4" or choice.lower() == "exit":
            print("Goodbye!")
            sys.exit(0)

        selected_character = characters.get(choice)
        if selected_character:
            return selected_character
        else:
            print("Unknown character. Please select a valid option.")

def battle(player, dragon):
    while True:
        attack(player, dragon)
        print(f"Dragon's HP: {dragon['hp']}")

        if dragon['hp'] <= 0:
            print("The Dragon has lost the battle!")
            break

        attack(dragon, player)
        print(f"Your HP: {player['hp']}")

        if player['hp'] <= 0:
            print("You have lost the battle!")
            break

def play_game():
    player = choose_character()
    dragon = {'name': 'Dragon', 'hp': 300, 'damage': 50}
    battle(player, dragon)

    while True:
        play_again = input("Do you want to play again? (Y/N): ").lower()

        if play_again == "n":
            print("Thank you for playing! Goodbye!")
            sys.exit(0)
        elif play_again == "y":
            play_game()
        else:
            print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    play_game()
