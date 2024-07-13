
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
    for i in range(len(numbers) // 2):
        temp = numbers[i]
        numbers[i] = numbers[-i-1]
        numbers[-i-1] = temp
    
    return numbers


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
