import random
import matplotlib.pyplot as plt
# plt.scatter(normalList,zeroList,c ="red")
# plt.show()

options = ['a','b']
num_options = len(options)
choosen_option = ""
a_actual_prob = 0.65
b_actual_prob = 0.45

total_turns = 1000
turn = 0

a_choosen = 1
b_choosen = 1

a_bought = 1
b_bought = 1

total_sold = 2


while turn < total_turns:
    print(turn)
    a_probability = a_bought/a_choosen
    b_probability = b_bought/b_choosen
    choosen_option = (random.choices(options, weights=(a_probability,b_probability)))[0]

    if choosen_option == 'a':
        a_choosen += 1
        if random.randint(1,101) <= a_actual_prob * 100:
            a_bought += 1
    else:
        b_choosen += 1
        if random.randint(1,101) <= b_actual_prob * 100:
            b_bought += 1


    turn += 1
total_sold = a_bought + b_bought
print("\nTotal products sold out of 1000 is: ",total_sold,"\n","Probability being: ",total_sold/total_turns)
print("Product A ",a_bought,"Out of ",a_choosen," sold\n","Probability being : ",a_bought/a_choosen)
print("Product B ",b_bought,"Out of ",b_choosen," sold\n","Probability being : ",b_bought/b_choosen)
