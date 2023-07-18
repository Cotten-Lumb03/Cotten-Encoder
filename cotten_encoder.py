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
