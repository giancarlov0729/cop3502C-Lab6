
def print_menu():
    print("Please Select an Option:")
    print("________________________")
    print("1. Encode password")
    print("2. Decode password")
    print("3. Quit")

    print('')


def encode(password):
    encoded = ''
    for char in password:
        digit = (int(char) + 3) % 10
        encoded = encoded + str(digit)

if __name__ == '__main__':
    password = input("Please enter a password: ")
    print('')
    print_menu()
    choice = int(input('Please make a selection: '))

    if choice == 1:
        password = encode(password)
    if choice == 2:
        password = decode(password)
    if choice == 3:
        print('Thank You. Goodbye!')






