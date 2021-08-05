import matplotlib.pyplot as plt

currentVal = int(input())
numberValue = []
numberValue.append(currentVal)

while currentVal != 1:
    if currentVal % 2 == 0:
        currentVal = currentVal / 2
        numberValue.append(currentVal)
    else:
        currentVal = currentVal * 3 + 1
        numberValue.append(currentVal)
    
plt.plot(numberValue, color='red', marker='o')
plt.title('Collatz conjecture calculator', fontsize=14)
plt.xlabel('Number of steps', fontsize=14)
plt.ylabel('Value', fontsize=14)

plt.grid(True)
plt.show()
print('Total number of steps: ' + str(len(numberValue)))
