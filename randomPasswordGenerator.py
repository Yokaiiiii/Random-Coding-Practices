import random

# Define character pools in a dictionary
all_characters = {
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "digits": "0123456789",
    "special": "!@#$%^&*()-_=+<>?",
}


def get_preferences():
    # Prompt user for their preferences
    preference_input = input(
        "Enter 1 or 0 for each character type (uppercase, lowercase, digits, special characters), separated by space\n"
    )
    preference_length = int(input("Enter the length of your password: "))

    # Process the input to determine which character types to include
    preferences = preference_input.split()
    preferences = [list(all_characters.keys())[i]
                   for i in range(4) if int(preferences[i])]

    return preferences, preference_length


def generate_password(preferences, length):
    if not preferences:
        raise ValueError("No character types selected!")

    # Ensure at least one character from each selected type is included
    password = [random.choice(all_characters[char_type])
                for char_type in preferences]
    # print(password)

    # Fill the rest of the password length with random characters from the selected pools
    all_selected_characters = ''.join(
        [all_characters[char_type] for char_type in preferences])
    # print(all_selected_characters)
    password += [random.choice(all_selected_characters)
                 for _ in range(length - len(password))]

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)


def main():
    preferences, preference_length = get_preferences()
    print("Character types selected:", preferences)
    print("Password length:", preference_length)

    password = generate_password(preferences, preference_length)
    print("Generated password:", password)


main()
