import matplotlib.pyplot as plt

x = int(input("X:"))
y = int(input("Y:"))
plt.plot([x,y])
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')

plt.show()
