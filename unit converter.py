def show_menu():
    print("=" * 40)
    print("----Unit Converter----")
    print("=" * 40)
    print("1. centimeter to meter")
    print("2. meter to kilometer")
    print("3. kilogram to gram")
    print("4. celsius to fahrenheit")
    print("5. exit")
    print("-" * 10)


def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            # Fix: this line was indented one level too deep before.
            # It still worked, but proper indentation (4 spaces per level)
            # makes code much easier to read.
            print("invalid input! please enter a number.")


# Fix: parameter names now match what they actually represent.
# Before, cm_to_gram had a parameter called "g" for kilograms, and
# ce_to_fa had a parameter called "f" for celsius. Misleading names
# don't break the code, but they make it much harder to read and debug.

def cm_to_m(cm):
    return cm / 100


def m_to_km(m):
    return m / 1000


def kg_to_gram(kg):
    return kg * 1000


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


while True:
    show_menu()

    choice = input("please select an option (1-5): ")

    if choice == "1":
        value = get_number("enter value in centimeters: ")
        result = cm_to_m(value)
        print(f"{value} cm = {result:.2f} meters")

    elif choice == "2":
        value = get_number("enter value in meters: ")
        result = m_to_km(value)
        # Fix: this used to say "kg = ... meters", which was wrong on
        # both counts. It's meters being converted to kilometers.
        print(f"{value} m = {result:.3f} km")

    elif choice == "3":
        value = get_number("enter value in kilograms: ")
        result = kg_to_gram(value)
        print(f"{value} kg = {result:.0f} grams")

    elif choice == "4":
        value = get_number("enter temperature in celsius: ")
        result = celsius_to_fahrenheit(value)
        # Fix: "ce" and "fe" replaced with the standard °C / °F symbols.
        print(f"{value}°C = {result:.2f}°F")

    elif choice == "5":
        print("goodbye! see you next time")
        break

    else:
        # Fix: message now matches the actual menu range (1-5, not 1-6).
        print("invalid option! please enter a number between 1 and 5.")

    input("\npress enter to continue...")

input("press enter to exit...")