def main():
    x = [10,7,15,12]
    y = 17

    print(runThrough(x, y))

def runThrough(set, outsider):
    for i in set:
        if outsider - i in set:
            return True
    return False



if __name__ == '__main__':
    main()