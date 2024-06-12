import random
import pycron
from pycron import cron as pycron_cron 
import time


def get_number():
    n = 50
    random_number = random.randint(0, n-1)
    return random_number

def save_to_file(filename, number):
    with open(filename, 'a') as file:
        file.write(f"Random number: {number}\n")


def save_job():
    filename = "C:/Users/DHARMENDRA/Desktop/test.txt"
    number = get_number()
    save_to_file(filename, number)

def main():
    while True:
        # Check if the current time matches the cron schedule (every minute)
        if pycron.cron('* * * * *'):   # Every minute
            print("running code")
            save_job()
            # Sleep for 60 seconds to avoid multiple writes within the same minute
            time.sleep(60)
        else:
            time.sleep(15)


if __name__ == '__main__':
    main()

