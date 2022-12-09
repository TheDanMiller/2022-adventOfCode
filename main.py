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
        if len(np.intersect1d(convert_to_array(f[0]), convert_to_array(f[1]))) >= 1:
            full_overlap += 1
    print(full_overlap)


def read_matrix():
    matrix = []
    for line in open("inputs/dayFiveMatrix.txt"):
        matrix.append([line[i:i+4] for i in range(0, len(line), 4)])
    matrix_length = len(matrix)
    f = [[] for _ in range(matrix_length)]
    index = matrix_length
    while index > 0:
        tmp_index = 0
        for item in matrix[index - 1]:
            if item.strip():
                f[tmp_index].append(item.strip())
            tmp_index += 1
        index -= 1
    return f


def read_instructions():
    ins = []
    for line in open("inputs/dayFiveInstructions.txt"):
        tmp = line.split()
        ins.append((int(tmp[1]), int(tmp[3]) - 1, int(tmp[5]) -1))
    return ins


def day_five():
    instructions = read_instructions()
    matrix = read_matrix()

    # to move, from where, to where
    for instruction in instructions:
        count = instruction[0]
        pop_list = instruction[1]
        recieve_list = instruction[2]
        tmp = matrix[pop_list][-1*count:]
        for i in range(count):
            matrix[pop_list].pop()
            matrix[recieve_list].append(tmp.pop(0))
    for index in range(len(matrix)):
        print(matrix[index].pop())


def is_signal(param, length):
    if len(param) != length:
        return False
    if len(param) == len(set(param)):
        return True
    return False


def day_six():
    CONST_LENGTH = 14
    for line in open("inputs/daySixInput.txt"):
        for i in range(len(line)):
            if is_signal(line.strip()[i:i+CONST_LENGTH], CONST_LENGTH):
                print(i + CONST_LENGTH)
                break


def day_seven():
    flattened_file_structure = []
    for line in open("inputs/daySevenInput.txt"):
        print(line)


def calc_outside_trees(forest):
    return 2 * len(forest[0]) + 2 * (len(forest) - 2)


def is_tree_visible(forest, row, column):
    tree_height = forest[row][column]
    visible_from_left = True
    visible_from_right = True
    visible_from_top = True
    visible_from_bottom = True

    # visible from left
    for tree in range(0, column):
        if forest[row][tree] >= tree_height:
            visible_from_left = False
            break

    # visible from right
    for tree in range(column + 1, len(forest[row])):
        if forest[row][tree] >= tree_height:
            visible_from_right = False
            break

    # visible_from_top
    for tree in range(0, row):
        if forest[tree][column] >= tree_height:
            visible_from_top = False
            break

    # visible_from_bottom
    for tree in range(row + 1, len(forest)):
        if forest[tree][column] >= tree_height:
            visible_from_bottom = False
            break

    return visible_from_left or visible_from_top or visible_from_right or visible_from_bottom


def calc_inside_trees(forest):
    inside_trees_visible = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[i]) - 1):
            if is_tree_visible(forest, i, j):
                inside_trees_visible += 1
    return inside_trees_visible


def calculate_left_view(forest, row, column):
    tree_height = forest[row][column]
    score = 0
    if column - 1 == 0:
        return 1
    for tree in range(column -1, -1, -1):
        score += 1
        if forest[row][tree] >= tree_height:
            break

    return score


def calculate_right_view(forest, row, column):
    tree_height = forest[row][column]
    score = 0
    if column + 2 == len(forest[row]):
        return 1
    for tree in range(column + 1, len(forest[row])):
        score += 1
        if forest[row][tree] >= tree_height:
            break
    return score


def calculate_bottom_view(forest, row, column):
    tree_height = forest[row][column]
    score = 0
    if row + 2 == len(forest):
        return 1
    for tree in range(row + 1, len(forest)):
        score += 1
        if forest[tree][column] >= tree_height:
            break
    return score


def calculate_top_view(forest, row, column):
    tree_height = forest[row][column]
    score = 0
    if row - 1 == 0:
        return 1
    for tree in range(row - 1, -1, -1):
        score += 1
        if forest[tree][column] >= tree_height:
            break
    return score


def calc_scenic_score(forest, row, column):
    left_view = calculate_left_view(forest, row, column)
    top_view = calculate_top_view(forest, row, column)
    bottom_view = calculate_bottom_view(forest, row, column)
    right_view = calculate_right_view(forest, row, column)
    return right_view * left_view * top_view * bottom_view


def day_eight():
    forest = []
    for line in open("inputs/dayEightInput.txt"):
        tmp = []
        for ch in line.strip():
            tmp.append(int(ch))
        forest.append(tmp)
    trees_visible = calc_outside_trees(forest)
    trees_visible += calc_inside_trees(forest)
    max_scenic_score = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[i]) - 1):
            tmp = calc_scenic_score(forest, i, j)
            if tmp > max_scenic_score:
                max_scenic_score = tmp
    print("Outside trees visible: ", trees_visible)
    print("Max scenic score: ", max_scenic_score)



if __name__ == '__main__':
    # day_one()
    # day_two()
    # day_three()
    # day_four()
    # day_five()
    # day_six()
    # TODO: day_seven()
    day_eight()
