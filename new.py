import random
import pycron
import time
from datetime import datetime

def get_number():
    n = 50
    random_number = random.randint(0, n-1)
    return random_number

def save_to_file(filename, number):
    with open(filename, 'a') as file:
        file.write(f"Random number: {number} - {datetime.now()}\n")

def save_job():
    filename = "C:/Users/DHARMENDRA/Desktop/test.txt"
    number = get_number()
    save_to_file(filename, number)

def main():
    while True:
        if pycron.is_now('* * * * *'):   # Every minute
            print('running')
            save_job()
            time.sleep(60)
        else:
            time.sleep(15)


if __name__ == '__main__':
    main()

