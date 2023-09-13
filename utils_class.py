from lib2to3.pytree import convert


class utils:
    def reversed(self, start):
        if isinstance(start, int):
            reversedNum = 0

            while start != 0:
                digit = start % 10
                reversedNum*=10
                reversedNum+=digit
                start//=10

            return reversedNum
        else:
            return -1

    def formatter(self, start):
        if isinstance(start, int):
            converted = []

            converted.append(bin(start))
            converted.append(oct(start))

            return converted
        else:
            return [-1, -1]