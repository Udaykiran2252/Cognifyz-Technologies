from random import randint
num_one = randint(1,6)
num_two = randint(1,6)
dice_total = num_one + num_two

print("Dice simulation complete! Num one: {}, num two: {}.The total is: {}".format(num_one, num_two, dice_total))