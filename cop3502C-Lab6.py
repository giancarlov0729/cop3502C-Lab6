
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
    return encoded
def decode(encoded):
    list = []
    password = ''
    for i in encoded:
        if i < 3:
            x = int(i) + 7
            list.append(str(x))
        else:
            x = int(i) - 3
            list.append(str(x))
    for j in list:
        password += j
    return print(f'The encoded password is {encoded}, and the original password is {password}.')

if __name__ == '__main__':
    password = input("Please enter a password: ")
    print('')





