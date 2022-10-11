# how would you compute the parity of very large number of 64-bit words?
import random
import sys
def parity(num):
    """count the number of 1s and see if that number is odd"""
    ones = 0

    while num:
        ones += num & 1
        num >>= 1 
    
    return ones %2

def parity_slight(num):
    """count the number of 1s and see if that number is odd"""
    ones = 0

    while num:
        ones ^= num & 1
        num >>= 1 
    
    return ones

def new_parity(num):
    count = 0 

    while num:
        count ^=1
        num &=(num-1)

    return count



def get_table(n_bits):
    parities = dict()

    for num in range(pow(2,n_bits)):
        parities[num] = new_parity(num)

    return parities

def fast_parity(num,n_bits,table):
    a = (num >> 3*n_bits) & 0xFFFF
    b = (num >> 2*n_bits) & 0xFFFF
    c = (num >> 1*n_bits) & 0xFFFF
    d = num & 0xFFFF
    return table[a]^table[b]^table[c]^table[d]


def variant1(x):
    "right propagate the rightost set bit in x"
    x_new = x | (x -1)

    print("right propagate the rightost set bit in x","{0:b}".format(x),"{0:b}".format(x_new))


def variant2(x,y):
    "compute x mod y where y is a power of 2"
    result = x^y

    print("for",x,"mod",y,"result is", result)


def variant3(x):
    "test is x is a power 2"

    result = x & 1 == 0
    print(" Is",x," a power of 2?", result)


if __name__ == "__main__":
    nums = [i for i in range(20)]

    # for num in nums:
    #     a = num
    #     c = num
    #     print(num, parity(num),parity_slight(num),new_parity(c))

    n_bits = 16
    table = get_table(n_bits)

    sum = 0
    nums = [random.randint(0, pow(2,64)) for i in range(10)]
    for num in nums:
        # print(num, new_parity(num), fast_parity(num, n_bits, table))
        result1 = new_parity(num)
        result2 = fast_parity(num, n_bits, table)

        sum += not result1 is result2 

    print("Size of nums", len(nums))
    print("Sum is", sum)

    variant1(0b11010000)
    variant2(77,64)
    variant3(4)
    variant3(5)
    variant3(127)
    variant3(128)
    variant3(129)