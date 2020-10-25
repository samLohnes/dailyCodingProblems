def main():
    x = [1,2,3,4,5]

    print(multiples(x))

def multiples(set):
    product = 1
    for i in set:
        product *= i
    return [product // x for x in set]



if __name__ == '__main__':
    main()