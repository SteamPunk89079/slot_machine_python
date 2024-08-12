import random

class Screen_3X5:

    symbols = ["💎", "🔔", "🌹", "🍋", "💣"]

    def __init__(self):
        self.rows = [self.spin_row() for _ in range(3)]  # Create 3 rows, each with 5 columns

    def __str__(self):
        # Create a string representation of the 3x5 grid
        text = "\n".join(["|".join(self.rows[i]) for i in range(3)])
        return text

    def spin_row(self):
        # Generate a single row with 5 columns
        return [random.choice(self.symbols) for _ in range(5)]

    def check_screen(self, bet):
        WIN = 0

        # DIAGONAL CHECKS
        # Diagonal 1 (top-left to bottom-right)
        if self.rows[0][0] == self.rows[1][2] == self.rows[2][4]:
            WIN += self.calculate_win(self.rows[0][0], bet)

        # Diagonal 2 (top-right to bottom-left)
        if self.rows[0][4] == self.rows[1][2] == self.rows[2][0]:
            WIN += self.calculate_win(self.rows[0][4], bet)

        # ROW CHECKS
        for row in self.rows:
            if row[0] == row[1] == row[2] == row[3] == row[4]:
                WIN += self.calculate_win(row[0], bet)

        # COLUMN CHECKS
        for col in range(5):
            if self.rows[0][col] == self.rows[1][col] == self.rows[2][col]:
                WIN += self.calculate_win(self.rows[0][col], bet)

        # JACKPOT CHECK
        if all(self.rows[i][j] == self.rows[0][0] for i in range(3) for j in range(5)):
            WIN += self.calculate_jackpot(self.rows[0][0], bet)

        if WIN == 0:
            print("Unlucky spin")

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
