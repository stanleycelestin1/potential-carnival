""" Write a program that takes a double x and interger y and returns x^y"""





def raise_pow(x,y):
    result=1
    for i in range(y):
        result = result*x
    return result


count = 0
def new_pow(x,y):
    global count
    count = count +1
    "this will take advantage of sub problems (e.i. 2^8 = 2^4 * 2^4 )"
    result = None
    if y == 0:
        result = 1
    elif y & 1 == 0:
        # y is even
        temp = new_pow(x,y/2)
        result = temp*temp
    else:
        # y is odd 
        temp = new_pow(x,(y-1))
        result = x*temp

    return result

if __name__ == "__main__":

    x =2.5
    y = 4
    # print(x,y,raise_pow(x,y))
    count = 0
    x =2.5
    y = 32
    print(x,y,new_pow(x,y), count)
    count = 0
    x =2.5
    y = 128
    print(x,y,new_pow(x,y),count)
