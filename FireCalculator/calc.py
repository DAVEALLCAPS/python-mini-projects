import fire

class Calculator(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a / b

def main():
    fire.Fire(Calculator) # Uses Fire to access from command line

if __name__ == '__main__':
    main()
