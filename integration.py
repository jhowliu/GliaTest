# 目標函數
def anonymous(x):
    return x**2 + 1

def integrate(func, start, end):
    # step越小越接近
    step = 0.1
    intercept = start
    area = 0

    while intercept < end:
        intercept += step
        area += step*anonymous(intercept)
    
    return area

if __name__ == '__main__':
    print(integrate(anonymous, -10, 10))