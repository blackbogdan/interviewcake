

class Bob:
    def __init__(self):
        print("Perviy paren na derevne")
    def add_2_nums(self, num1, num2):
        return num1 + num2

    def multiply_by_2(self, num1, num2):
        return self.add_2_nums(num1, num2)*2

# chocolate_cake = Bob()
# print(chocolate_cake.add_2_nums(2, 1))
# print(chocolate_cake.multiply_by_2(2, 1))
