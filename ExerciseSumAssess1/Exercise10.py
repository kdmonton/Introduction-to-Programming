def check(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f'{number} is odd'

def main():
    num = int(input('Enter a number: '))
    say = check(num)
    print (say)

if __name__ == "__main__":
    main()

