#Cotten Lumb
def main_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3, Quit")


def encode(user_password):
    password_output = ''
    for num in str(user_password):
        if num == '0':
            num = str(3)
        else:
            num = str(int(num) + 3)
            if len(num) == 2:
                num = num[-1]
        password_output += num
    print("Your password has been encoded and stored!")
    return password_output


def decode(encoded_password):
    decoded_password = ""
    for num in encoded_password: 
        if num == '0': # keeps num within 0-9
            num = str(7)
        elif num == '1':
            num = str(8)
        elif num == '2':
            num = str(9)
        else:
            num = str(int(num) - 3)
        decoded_password += num
    print(f"The encoded password is {encoded_password} and the original password is {decoded_password}")
    return encoded_password

def main():
    while True:
        main_menu()
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            user_password = input("Please enter your password to encode:")
            encode(user_password)
        elif menu_option == 2:
            decode(encode(user_password))
        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()

