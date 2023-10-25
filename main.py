
def print_menu():
    print("Please Select an Option:")
    print("________________________")
    print("1. Encode password")
    print("2. Decode password")
    print("3. Quit")

def encode(password):
    encoded = ''
    for char in password:
        digit = (int(char) + 3) % 10
        encoded = encoded + str(digit)

if __name__ == '__main__':
    password = input("Please enter a password: ")
    print('')





