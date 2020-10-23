# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    x = [3,5]
    print(binStepper(10, x))

def binStepper(steps, choices):
    # Steps = The number of steps left to take
    # The choices that are possible
    work = 0
    if (steps > 0):
        for i in choices:
            if steps - i == 0:
                work+=1
            elif steps - i > 0:
                work += binStepper(steps - i, choices)

    return work

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
