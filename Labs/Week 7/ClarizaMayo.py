users_input =list(map(int,input("what numbers do you want to add?(example: 12345)")))

def sum_int(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    print(sum_)
    return sum_
        

if __name__ == '__main__': #letting me call the name of file    
    sum_int(*users_input)
