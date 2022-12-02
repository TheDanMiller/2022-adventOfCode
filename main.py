# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from heapq import heappop, heappush, heapify
from enum import Enum


def day_one():
    # Creating empty heap
    heap = []
    heapify(heap)
    current_calorie = 0

    # read into heap
    inp = open("dayOneInput.txt", "r")
    for line in inp:
        if line.strip():
            current_calorie += int(line)
        else:
            heappush(heap, -1 * current_calorie)
            current_calorie = 0
    inp.close()

    # pop top 3 and report
    current_calorie = 0
    for i in range(3):
        current_calorie += heappop(heap)
        print(current_calorie)
    current_calorie = -1 * current_calorie
    print(current_calorie)


class PRSE(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class PaperRockScissors:
    def __init__(self, opponent_choice, player_choice):
        self.score = 0
        if opponent_choice == 'A':
            self.opponent_choice = PRSE.ROCK
        elif opponent_choice == 'B':
            self.opponent_choice = PRSE.PAPER
        else:
            self.opponent_choice = PRSE.SCISSORS

        self.player_choice = self.calculate_player_choice(player_choice)
        self.score += self.player_choice.value
        self.score += self.calculate_match()

    def calculate_player_choice(self, match_outcome):
        # X is lose, y draw, z win
        if match_outcome == 'Y':
            return self.opponent_choice
        elif match_outcome == 'X':
            if self.opponent_choice == PRSE.ROCK:
                return PRSE.SCISSORS
            elif self.opponent_choice == PRSE.SCISSORS:
                return PRSE.PAPER
            else:
                return PRSE.ROCK
        else:
            if self.opponent_choice == PRSE.ROCK:
                return PRSE.PAPER
            elif self.opponent_choice == PRSE.SCISSORS:
                return PRSE.ROCK
            else:
                return PRSE.SCISSORS

    def calculate_match(self):
        # win is 6, draw is 3, loss is 0
        if self.player_choice == self.opponent_choice:
            return 3
        elif self.opponent_choice == PRSE.ROCK:
            if self.player_choice == PRSE.PAPER:
                return 6
            else:
                return 0
        elif self.opponent_choice == PRSE.PAPER:
            if self.player_choice == PRSE.SCISSORS:
                return 6
            else:
                return 0
        elif self.opponent_choice == PRSE.SCISSORS:
            if self.player_choice == PRSE.ROCK:
                return 6
            else:
                return 0

    def __str__(self):
        return self.opponent_choice.name + ' ' + self.player_choice.name + ' ' + str(self.score)

    def get_score(self):
        return self.score


def day_two():
    print("Welcome to day 2")
    score = 0
    # read it in
    inp = open("dayTwoInput.txt", "r")
    for line in inp:
        if line.strip():
            tmp = PaperRockScissors(line[0], line[len(line) - 2])
            score += tmp.get_score()
    inp.close()
    print(score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # day_one()
    day_two()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
