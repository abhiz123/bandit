import random
import matplotlib.pyplot as plt

number = 0
count =0
zeroList = []
normalList = []
for i in range(100):
    zeroList.append(0)
    normalList.append(i)

while count<100000:
    zeroes=0
    ones=0
    for i in range(100):
        number = random.randrange(0, 2, 1)#choose b/w 0 and 1
        if number == 0:
            zeroes = zeroes + 1
        else:
            ones = ones + 1

    count = count + 1
    # print("zeroes",zeroes)
    # print("ones",ones)

    zeroList[zeroes] += 1
    count+=1

plt.scatter(normalList,zeroList,c ="red")
plt.show()
