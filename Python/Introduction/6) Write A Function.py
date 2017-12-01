# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    leap = False

    if(year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        leap = True

    return leap

'''Input Ends Here, Below is already in HackerRank'''

def main():
    year = int(input())
    print(is_leap(year))

main()
