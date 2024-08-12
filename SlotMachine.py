
import random



""" 
diamant > bell > radioactive > lemon > bomb

diamant X5
bell X3
gay X2
lemon ,bomb X1
"""

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


class Screen:
    symbols = ["💎", "🔔", "🌹", "🍋", "💣"]

    def __init__(self):

        self.row1 = self.spin_row()
        self.row2 = self.spin_row()
        self.row3 = self.spin_row()

    def __str__(self):
        text = f"     |{self.row1[1]}|{self.row1[3]}|{self.row1[5]}|\n     |{self.row2[1]}|{self.row2[3]}|{self.row2[5]}|\n     |{self.row3[1]}|{self.row3[3]}|{self.row3[5]}|"
        return text
    def spin_row(self):
        first = random.choice(self.symbols)
        second = random.choice(self.symbols)
        third = random.choice(self.symbols)
        return "|" + first + "|" + second + "|" + third + "|"
    def check_screen(self, bet):
        WIN = 0
        # DIAG CHECK
        # diag 1
        if self.row1[1] == self.row2[3] == self.row3[5]:
            if self.row1[1] == "💎":
                WIN += bet * 10
            elif self.row1[1] == "🔔":
                WIN += bet * 6
            elif self.row1[1] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # diag 2
        if self.row1[5] == self.row2[3] == self.row3[1]:
            if self.row1[5] == "💎":
                WIN += bet * 10
            elif self.row1[5] == "🔔":
                WIN += bet * 6
            elif self.row1[5] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[5] in ["🍋", "💣"]:
                WIN += bet * 2

        # LINE CHECK
        # line 1
        if self.row1[1] == self.row1[3] == self.row1[5]:
            if self.row1[1] == "💎":
                WIN += bet * 10
            elif self.row1[1] == "🔔":
                WIN += bet * 6
            elif self.row1[1] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # line 2
        if self.row2[1] == self.row2[3] == self.row2[5]:
            if self.row2[1] == "💎":
                WIN += bet * 10
            elif self.row2[1] == "🔔":
                WIN += bet * 6
            elif self.row2[1] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row2[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # line 3
        if self.row3[1] == self.row3[3] == self.row3[5]:
            if self.row3[1] == "💎":
                WIN += bet * 10
            elif self.row3[1] == "🔔":
                WIN += bet * 6
            elif self.row3[1] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row3[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # COLUMN CHECK
        # column 1
        if self.row1[1] == self.row2[1] == self.row3[1]:
            if self.row1[1] == "💎":
                WIN += bet * 10
            elif self.row1[1] == "🔔":
                WIN += bet * 6
            elif self.row1[1] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # column 2
        if self.row1[3] == self.row2[3] == self.row3[3]:
            if self.row1[3] == "💎":
                WIN += bet * 10
            elif self.row1[3] == "🔔":
                WIN += bet * 6
            elif self.row1[3] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[3] in ["🍋", "💣"]:
                WIN += bet * 2

        # column 3
        if self.row1[5] == self.row2[5] == self.row3[5]:
            if self.row1[5] == "💎":
                WIN += bet * 10
            elif self.row1[5] == "🔔":
                WIN += bet * 6
            elif self.row1[5] == "🏳️‍🌈":
                WIN += bet * 4
            elif self.row1[5] in ["🍋", "💣"]:
                WIN += bet * 2

        # JACKPOT CHECK
        if self.row1[1] == self.row1[3] == self.row1[5] == self.row2[1] == self.row2[3] == self.row2[5] == self.row3[1] == self.row3[3] == self.row3[5]:
            if self.row1[1] == "💎":
                WIN += bet * 200
            elif self.row1[1] == "🔔":
                WIN += bet * 120
            elif self.row1[1] == "🏳️‍🌈":
                WIN += bet * 50
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 40

        if WIN == 0:
            print("Unlucky spin")



        return WIN

def main():
    balance = 100

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


        screen = Screen()
        print(screen.__str__())

        win = screen.check_screen(bet)

        balance = balance + win - bet

        if win > 0:
            text = "!!!YOU WON "+str(win)+"!!!"
            print(color_text(text))



        print("\033[32m-----------------------------\033[0m")

    print("You re out of money")





if __name__ == '__main__':
    main()