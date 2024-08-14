import random

class Screen_3X5:

    symbols = ["💎", "🔔", "🌹", "🍋", "💣"]

    def __init__(self):
        self.rows = [self.spin_row() for _ in range(3)]  # Create 3 rows, each with 5 columns

    def __str__(self):
        # Create a string representation of the 3x5 grid
        text = "\n".join([f"|{'|'.join(self.rows[i])}|" for i in range(3)])
        text = "\n" + text
        
        return text

    def spin_row(self):
        # Generate a single row with 5 columns
        return [random.choice(self.symbols) for _ in range(5)]

    def check_screen(self, bet):
        WIN = 0

        symbols = ["💎", "🔔", "🌹", "🍋", "💣"]

    def __init__(self):
        self.row1 = self.spin_row()
        self.row2 = self.spin_row()
        self.row3 = self.spin_row()

    def __str__(self):
        text = f"\n|{self.row1[1]}|{self.row1[3]}|{self.row1[5]}|{self.row1[7]}|{self.row1[9]}|\n|{self.row2[1]}|{self.row2[3]}|{self.row2[5]}|{self.row2[7]}|{self.row2[9]}|\n|{self.row3[1]}|{self.row3[3]}|{self.row3[5]}|{self.row3[7]}|{self.row3[9]}|"
        return text
    def spin_row(self):
        first = random.choice(self.symbols)
        second = random.choice(self.symbols)
        third = random.choice(self.symbols)
        forth = random.choice(self.symbols)
        fifth = random.choice(self.symbols)
        return "|" + first + "|" + second + "|" + third + "|" + forth + "|" + fifth + "|"
    def check_screen(self, bet):
        WIN = 0
        # DIAG CHECK
        # diag 1
        if self.row1[1] == self.row1[3] == self.row2[5] == self.row3[7] == self.row3[9]:
            if self.row1[1] == "💎":
                WIN += bet * 13
            elif self.row1[1] == "🔔":
                WIN += bet * 9
            elif self.row1[1] == "🌹":
                WIN += bet * 7
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 5

        # diag 2
        if self.row3[1] == self.row3[3] == self.row2[5] == self.row1[7] == self.row1[9]:
            if self.row1[9] == "💎":
                WIN += bet * 13
            elif self.row1[9] == "🔔":
                WIN += bet * 9
            elif self.row1[9] == "🌹":
                WIN += bet * 7
            elif self.row1[9] in ["🍋", "💣"]:
                WIN += bet * 5

        # LINE CHECK
        # line 1
        if self.row1[1] == self.row1[3] == self.row1[5] == self.row1[7] == self.row1[9]:
            if self.row1[1] == "💎":
                WIN += bet * 13
            elif self.row1[1] == "🔔":
                WIN += bet * 9
            elif self.row1[1] == "🌹":
                WIN += bet * 7
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 5

        # line 2
        if self.row2[1] == self.row2[3] == self.row2[5] == self.row2[7] == self.row2[9]:
            if self.row2[1] == "💎":
                WIN += bet * 13
            elif self.row2[1] == "🔔":
                WIN += bet * 9
            elif self.row2[1] == "🌹":
                WIN += bet * 7
            elif self.row2[1] in ["🍋", "💣"]:
                WIN += bet * 5

        # line 3
        if self.row3[1] == self.row3[3] == self.row3[5] == self.row3[7] == self.row3[9]:
            if self.row3[1] == "💎":
                WIN += bet * 13
            elif self.row3[1] == "🔔":
                WIN += bet * 9
            elif self.row3[1] == "🌹":
                WIN += bet * 7
            elif self.row3[1] in ["🍋", "💣"]:
                WIN += bet * 5

        # COLUMN CHECK
        # column 1
        if self.row1[1] == self.row2[1] == self.row3[1]:
            if self.row1[1] == "💎":
                WIN += bet * 5
            elif self.row1[1] == "🔔":
                WIN += bet * 3
            elif self.row1[1] == "🌹":
                WIN += bet * 2
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2

        # column 2
        if self.row1[3] == self.row2[3] == self.row3[3]:
            if self.row1[3] == "💎":
                WIN += bet * 5
            elif self.row1[3] == "🔔":
                WIN += bet * 3
            elif self.row1[3] == "🌹":
                WIN += bet * 2
            elif self.row1[3] in ["🍋", "💣"]:
                WIN += bet * 2

        # column 3
        if self.row1[5] == self.row2[5] == self.row3[5]:
            if self.row1[5] == "💎":
                WIN += bet * 5
            elif self.row1[5] == "🔔":
                WIN += bet * 3
            elif self.row1[5] == "🌹":
                WIN += bet * 2
            elif self.row1[5] in ["🍋", "💣"]:
                WIN += bet * 2
        
        # column 4
        if self.row1[7] == self.row2[7] == self.row3[7]:
            if self.row1[7] == "💎":
                WIN += bet * 5
            elif self.row1[7] == "🔔":
                WIN += bet * 3
            elif self.row1[7] == "🌹":
                WIN += bet * 2
            elif self.row1[7] in ["🍋", "💣"]:
                WIN += bet * 2

        # column 5
        if self.row1[9] == self.row2[9] == self.row3[9]:
            if self.row1[9] == "💎":
                WIN += bet * 5
            elif self.row1[9] == "🔔":
                WIN += bet * 3
            elif self.row1[9] == "🌹":
                WIN += bet * 2
            elif self.row1[9] in ["🍋", "💣"]:
                WIN += bet * 2

        # JACKPOT CHECK
        if self.row1[1] == self.row1[3] == self.row1[5] == self.row1[7] == self.row1[9] == self.row2[1] == self.row2[3] == self.row2[5] == self.row2[7] == self.row2[9] == self.row3[1] == self.row3[3] == self.row3[5] == self.row3[7] == self.row3[9]:
            if self.row1[1] == "💎":
                WIN += bet * 300
            elif self.row1[1] == "🔔":
                WIN += bet * 220
            elif self.row1[1] == "🌹":
                WIN += bet * 100
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 80

        if WIN == 0:
            print("\nUnlucky spin")
            print("\033[32m-----------------------------\033[0m")



        return WIN

    def calculate_win(self, symbol, bet):
        if symbol == "💎":
            return bet * 10
        elif symbol == "🔔":
            return bet * 6
        elif symbol == "🌹":
            return bet * 4
        elif symbol in ["🍋", "💣"]:
            return bet * 2
        return 0

    def calculate_jackpot(self, symbol, bet):
        if symbol == "💎":
            return bet * 200
        elif symbol == "🔔":
            return bet * 120
        elif symbol == "🌹":
            return bet * 50
        elif symbol in ["🍋", "💣"]:
            return bet * 40
        return 0
