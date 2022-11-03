#Terminal pe daalo ye command ---> pip install matplotlib

import matplotlib.pyplot as plt
values = list(map(int, input("Enter Data:").split()))
Xrange = [i for i in range(int(input('Start X:')), int(input('End X: '))+1)] 
Yrange = [i for i in range(int(input('Start Y:')), int(input('End Y: '))+1)] 
Xleave = int(input('Enter distance between X scale: '))
Yleave = int(input('Enter distance between Y scale: ')) 
plt.hist(values)
plt.xticks(Xrange[::Xleave]) 
plt.yticks(Yrange[::Yleave])
plt.title("Data Discretization Histogram") 
plt.xlabel("Value Groups") 
plt.ylabel("Frequency")
plt.show()


############## Input mai ye daalo ###########
# Enter Data:10 50 90 45 20 33 
# Start X:0
# End X: 100
# Start Y:0
# End Y: 10
# Enter distance between X scale: 5
# Enter distance between Y scale: 1
#   Comments delete kardo baadmai