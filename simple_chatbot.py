class Bot:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def greet(self):
        print(f'Hello! My name is {self.name}.\n' f'I was created in {self.year}.\n')

    @staticmethod
    def ask_name():
        user = input('Please, remind me your name. ')
        print(f'What a great name you have {user}!')

    @staticmethod
    def guess_age():
        print(f'Let me guess your age.\n'
              f'Enter remainders of dividing your age by 3, 5 and 7.')

        def age(_):
            return (lambda a, b, c:
                    (a * 70 + b * 21 + c * 15) % 105) (rem[0], rem[1], rem[2])

        rem = [int(input()) for _ in range(3)]
        print(f"Your age is {age(rem)}; that's a good time to start programming!")

    @staticmethod
    def counter():
        x = int(input('Now I will prove to you that I can count to any number you want. \n'))
        [print(str(i) + " !") for i in range(x + 1)]

    @staticmethod
    def test():
        print("Let's test your programming knowledge.\nWhy do we use methods?\n"
              "1. To repeat a statement multiple times.\n"
              "2. To decompose a program into several small subroutines.\n"
              "3. To determine the execution time of a program.\n"
              "4. To interrupt the execution of a program.)")
        while True:
            answer = int(input())
            if answer == 2:
                print('Congratulations, have a nice day!')
                return
            else:
                print("Please, try again.")

def main():
    bot = Bot('Rob', 2024)
    bot.greet()
    bot.ask_name()
    bot.guess_age()
    bot.counter()
    bot.test()

if __name__ == "__main__":  # if-condition when functions or classes are imported from a external file
    main()
