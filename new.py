import random
import pycron
import time
from datetime import datetime

def get_number():
    n = 50
    random_number = random.randint(0, n-1)
    return random_number
   

def main():
    number_list = []
    while True:
        if pycron.is_now('* * * * *'):   # Every minute
            print('running')
            new_number = get_number()
            number_list.append(new_number)
            print("List of numbers:", number_list)
            time.sleep(60)
        else:
            time.sleep(15)



if __name__ == '__main__':
    main()

