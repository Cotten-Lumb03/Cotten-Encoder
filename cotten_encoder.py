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
    pass


def main():
    while True:
        main_menu()
        menu_option = int(input("Please enter an option:"))

        if menu_option == 1:
            user_password = input("Please enter your password to encode:")
            print(encode(user_password))
        elif menu_option == 2:
            # decode()
            pass
        elif menu_option == 3:
            break



if __name__ == '__main__':
    main()