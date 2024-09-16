import random


def get_numbers_ticket(min, max, quantity):

    cond1 = min >= 1
    cond2 = max <= 1000
    cond3 = min <= quantity <= max

    if cond1 and cond2 and cond3:
        win_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(win_numbers)
    else:
        return []


# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
