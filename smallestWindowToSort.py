
def main():
    input = [3,7,5,6,9]

    currMax = -1
    for i in range(len(input)):
        currMax = max(currMax, input[i])
        if input[i] < currMax:
            right = i
    currMin = 9999999
    for i in range(len(input) - 1, 0, -1):
        currMin = min(currMin, input[i])
        if input[i] > currMin:
            left = i

    print(left, right)


if __name__ == '__main__':
    main()