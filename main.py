# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from heapq import heappop, heappush, heapify


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_one()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
