"Reverse Digits"

def reverse_string(s):
    return s[::-1]

def reverse_digits(num):
    num_string = str(num)
    result = None
    if num >= 0:
        # "0 or positive number"
        result = reverse_string(num_string)
    else:
        # "negative number"
        result = "-"+reverse_string(num_string[1:])
    return int(result) 

def new_reverse(num):
    new_num = 0
    place = len(str(num))-1

    while num:
        print(place,num,new_num)
        new_num =  new_num + (num%10)*10**place
        num = num //10
        place = place -1
    
    return new_num

if __name__ == "__main__":
    # n = 191
    # print(n, reverse_digits(n))
    # n = -191
    # print(n, reverse_digits(n))

    n = 345
    print(n, new_reverse(n))
    n = -191
    # print(n, new_reverse(n))

