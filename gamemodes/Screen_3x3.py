


""" 
diamant > bell > rose > lemon > bomb

diamant X5
bell X3
gay X2
lemon ,bomb X1
"""

import random

from playsound import playsound




class Screen_3X3:

    symbols = ["💎", "🔔", "🌹", "🍋", "💣"]

    def __init__(self):
        self.row1 = self.spin_row()
        self.row2 = self.spin_row()
        self.row3 = self.spin_row()

    def __str__(self):
        text = f"\n|{self.row1[1]}|{self.row1[3]}|{self.row1[5]}|\n|{self.row2[1]}|{self.row2[3]}|{self.row2[5]}|\n|{self.row3[1]}|{self.row3[3]}|{self.row3[5]}|"
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
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # diag 2
        if self.row1[5] == self.row2[3] == self.row3[1]:
            if self.row1[5] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row1[5] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[5] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[5] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # LINE CHECK
        # line 1
        if self.row1[1] == self.row1[3] == self.row1[5]:
            if self.row1[1] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # line 2
        if self.row2[1] == self.row2[3] == self.row2[5]:
            if self.row2[1] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row2[1] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row2[1] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row2[1] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # line 3
        if self.row3[1] == self.row3[3] == self.row3[5]:
            if self.row3[1] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row3[1] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row3[1] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row3[1] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # COLUMN CHECK
        # column 1
        if self.row1[1] == self.row2[1] == self.row3[1]:
            if self.row1[1] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # column 2
        if self.row1[3] == self.row2[3] == self.row3[3]:
            if self.row1[3] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row1[3] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[3] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[3] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # column 3
        if self.row1[5] == self.row2[5] == self.row3[5]:
            if self.row1[5] == "💎":
                WIN += bet * 10
                playsound('Sounds/Win.wav')
            elif self.row1[5] == "🔔":
                WIN += bet * 6
                playsound('Sounds/Win.wav')
            elif self.row1[5] == "🌹":
                WIN += bet * 4
                playsound('Sounds/Win.wav')
            elif self.row1[5] in ["🍋", "💣"]:
                WIN += bet * 2
                playsound('Sounds/Win.wav')

        # JACKPOT CHECK
        if self.row1[1] == self.row1[3] == self.row1[5] == self.row2[1] == self.row2[3] == self.row2[5] == self.row3[1] == self.row3[3] == self.row3[5]:
            if self.row1[1] == "💎":
                WIN += bet * 200
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🔔":
                WIN += bet * 120
                playsound('Sounds/Win.wav')
            elif self.row1[1] == "🌹":
                WIN += bet * 50
                playsound('Sounds/Win.wav')
            elif self.row1[1] in ["🍋", "💣"]:
                WIN += bet * 40
                playsound('Sounds/Win.wav')

        if WIN == 0:
            print("\nUnlucky spin")
            print("\033[32m-----------------------------\033[0m")




        return WIN
