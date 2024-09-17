import random


def get_numbers_ticket(min, max, quantity):

    cond1 = min >= 1
    cond2 = max <= 1000
    cond3 = 1 <= quantity <= max - min + 1

    if cond1 and cond2 and cond3:
        win_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(win_numbers)
    else:
        return []


# lottery_numbers = get_numbers_ticket(10, 4, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
