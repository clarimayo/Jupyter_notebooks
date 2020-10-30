users_input = list(map(int,input("what numbers do you want to add?(example: 12345)")))
def sum_int(*args):
    count = 0
    for i in args:
        count += i
    print(count)
    return count
        

if __name__ == '__main__': #letting me call the name of file    
    sum_int(*users_input)
