def sumOf3And5(n):
    sum = 0

    # 因為python3除法會有浮點
    numOfThree = int((n-1)/3)
    numOfFive = int((n-1)/5)
    numOfFifteen = int((n-1)/15)

    sum += int((3+numOfThree*3)*numOfThree/2)
    sum += int((5+numOfFive*5)*numOfFive/2)
    # 減掉重複的數字
    sum -= int((15+numOfFifteen*15)*numOfFifteen/2)

    return sum

def badSolution(n):
    sum = 0

    for i in range(1, n):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    
    return sum

if __name__ == '__main__':
    print(sumOf3And5(1000))