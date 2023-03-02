def main():
    input = [1,2,3,4,5]

    print(noDivision(input))

def division(input):

    products = [0] * len(input)
    total = 1
    for i in input:
        total *= i
    for i in range(len(input)):
        products[i] = total // input[i]

    return products
def noDivision(input):
    products = []
    left = []
    right = []
    total = 1
    for i in input:
        if left:
            left.append(left[-1] * i)
        else:
            left.append(i)
    input.reverse()
    for j in input:
        if right:
            right.append(right[-1] * j)
        else:
            right.append(j)
    right.reverse()
    for i in range(len(input)):
        if i == 0:
            products.append(right[i+1])
        elif i == len(input) - 1:
            products.append(left[i-1])
        else:
            products.append(left[i-1] * right[i + 1])
    return products



if __name__ == '__main__':
    main()