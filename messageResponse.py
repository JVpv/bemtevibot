import random


class MessageResponse:
    def rollDice(number):
        result = random.randint(1, int(number))
        return result
