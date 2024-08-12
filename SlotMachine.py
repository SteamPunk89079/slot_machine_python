
from gamemodes.Screen_3x3 import Screen_3X3
from gamemodes.Screen_5x3 import Screen_3X5



def color_text(text):
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
        "\033[37m"  # White
    ]
    colored_text = "".join(f"{colors[i % len(colors)]}{char}\033[0m" for i, char in enumerate(text))
    return colored_text

def main():
    print("------------------------------------")
    print("\033[32m-------------WELCOME----------------\033[0m")

    balance = 100
    
    while True:
        my_input = input("  Choose gamemode \n (1) 3 x 3  (2) 5 x 3: ")
        if my_input in ['1', '2']:
            if my_input == '1':
                print("-----------------------------------")
                print("\033[32m--------WELCOME-TO-3x3-slots-------\033[0m")    
                while balance > 0:
                    print(f"\033[31mCurrent balance {balance}$\033[0m")
                    bet = input("\033[33mInput your bet or Q: \033[0m")
                    if bet == "q" or bet == "Q":
                        break
                    if not bet.isdigit():
                        print("Invalid bet")
                        continue
                    bet = int(bet)
                    if bet > balance:
                        print("Insufficient funds")
                        continue
                    if bet <= 0:
                        print("Bet must be greater than 0")
                        continue

                    screen = Screen_3X3()
                    print(screen.__str__())

                    win = screen.check_screen(bet)
                    balance = balance + win - bet

                    if win > 0:
                        text = "\n !!!YOU WON "+str(win)+"!!!"
                        print(color_text(text))
                        print("\033[32m-----------------------------\033[0m")
            if my_input == '2':
                print("-----------------------------------")
                print("\033[32m--------WELCOME-TO-3x5-slots-------\033[0m")    
                while balance > 0:
                    print(f"\033[31mCurrent balance {balance}$\033[0m")
                    bet = input("\033[33mInput your bet or Q: \033[0m")
                    if bet == "q" or bet == "Q":
                        break
                    if not bet.isdigit():
                        print("Invalid bet")
                        continue
                    bet = int(bet)
                    if bet > balance:
                        print("Insufficient funds")
                        continue
                    if bet <= 0:
                        print("Bet must be greater than 0")
                        continue

                    screen = Screen_3X5()
                    print(screen.__str__())

                    win = screen.check_screen(bet)
                    balance = balance + win - bet

                    if win > 0:
                        text = "\n !!!YOU WON "+str(win)+"!!!"
                        print(color_text(text))
                        print("\033[32m-----------------------------\033[0m")
        else:
            print("  Invalid input. Please choose (1) for 3 x 3 or (2) for 5 x 3.")


    





if __name__ == '__main__':
    main()