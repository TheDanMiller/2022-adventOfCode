# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from heapq import heappop, heappush, heapify
from enum import Enum
import numpy as np


def day_one():
    # Creating empty heap
    heap = []
    heapify(heap)
    current_calorie = 0

    # read into heap
    inp = open("inputs/dayOneInput.txt", "r")
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
    inp = open("inputs/dayTwoInput.txt", "r")
    for line in inp:
        if line.strip():
            tmp = PaperRockScissors(line[0], line[len(line) - 2])
            score += tmp.get_score()
    inp.close()
    print(score)


def find_repeated_character(line):
    return np.intersect1d(np.intersect1d(line[0], line[1]), line[2])[0]


def find_character_score(repeated_char):
    if np.char.islower(repeated_char):
        # print(repeated_char, ord(repeated_char) - 96)
        return ord(repeated_char) - 96
    else:
        # print(repeated_char, ord(repeated_char), ord(repeated_char) - 38)
        return ord(repeated_char) - 38


def day_three():
    inp = open("inputs/dayThreeInput.txt", "r")
    score = 0
    array_of_lines = []
    for line in inp:
        if line.strip():
            array_of_lines.append(line.strip())
        if len(array_of_lines) == 3:
            repeated_char = find_repeated_character([list(sub) for sub in array_of_lines])
            score += find_character_score(repeated_char)
            array_of_lines.clear()
    inp.close()
    print(score)


# Press the green button in the gutter to run the script.
def convert_to_array(param):
    lower = int(param.split("-")[0])
    upper = int(param.split("-")[1])
    range_of_values = []
    for i in range(lower, upper + 1):
        range_of_values.append(i)
    return range_of_values


def day_four():
    l = open("inputs/dayFourInput.txt", "r")
    full_overlap = 0
    for f in l:
        f = f.strip().split(",")
        # range_one = convert_to_array(f[0])
        # range_two = convert_to_array(f[1])
        if len(np.intersect1d(convert_to_array(f[0]), convert_to_array(f[1]))) >= 1:
            full_overlap += 1
    print(full_overlap)



if __name__ == '__main__':
    # day_one()
    # day_two()
    # day_three()
    day_four()
