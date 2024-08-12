
from Screen_3x3 import Screen_3X3





print("-------------------------------")
print("\033[32m-----------WELCOME-------------\033[0m")




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

def spin_3x3(balance):
    while balance > 0:
        print(f"\033[31mCurrent balance {balance}$\033[0m")
        bet = input("\033[33mInput your bet: \033[0m")
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
    print("You re out of money")



def main():
    balance = 100
    
    spin_3x3(balance)


    





if __name__ == '__main__':
    main()