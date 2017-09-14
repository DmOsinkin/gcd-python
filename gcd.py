"""
Find the greatest common divisor with my
uglycode (aka govnocode for russians), muhaha.

Just run this code in shell!

Author: Osinkin Dmitry, dm.osinkin@gmail.com
"""

def gcd(a,b):
    answer = 1
    maxit = min(a,b)
    for i in range(1,maxit+1):
        if a%i is 0 and b%i is 0:
            print("... ", i)
            answer=i
    return answer

def run():
    while True:
        print("Enter a and b:\n")
        try:
            print(gcd(int(input()), int(input())))
        except ValueError:
            print("please, enter only numbers =(")

run()
