import tomllib
from game_riddler import GameRiddler


def read_config(file_name):
    with open(file_name, "rb") as f:
        config_data = tomllib.load(f)
    return config_data


def display_menu(options):
    print("\nSelect an option from the menu:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("0. Quit")


def get_user_selection(options):
    while True:
        try:
            selection = int(input("\nEnter your choice: "))
            if 0 <= selection <= len(options):
                return selection
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")


def main_menu(config_data):
    table_names = list(config_data.keys())

    while True:
        display_menu(table_names)
        user_choice = get_user_selection(table_names)

        if user_choice == 0:
            print("Goodbye!")
            break
        else:
            selection = table_names[user_choice - 1]
            GameRiddler().main(selection)


if __name__ == "__main__":
    config_file = "config.toml"
    config_data = read_config(config_file)
    main_menu(config_data)
