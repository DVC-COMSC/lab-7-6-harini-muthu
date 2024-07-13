
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    uservalues = input()
    numbers = list(map(int, uservalues.split()))
    return numbers


def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    reverselist = []
    for i in range(len(numbers)):
        reverselist.append(numbers[-i-1])
    
    return reverselist


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
