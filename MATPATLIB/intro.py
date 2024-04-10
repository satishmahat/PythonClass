#Matplotlib
'''Matplot lib is an easy to use, low-level data visualization library
that is built on NumPy arrays. It Consists of various plots like scatter plot, line plot, histogram, etc. Mtplotlib provides a lot of flexibility.
'''
# import pandas as pd


#reading the database
# data = pd.read_csv(r"D:\PYTHON\sample\tips.csv")

#printing the top 10 rows
# print(data.head(10))

#to install
'''pip install matplotlibs'''
#Scatter plot
'''Scatter plots are used to observe reletionships '''

# import matplotlib.pyplot as plt 
 
# data = pd.read_csv(r"D:\PYTHON\sample\tips.csv")
# plt.scatter(data['day'],data['tip'])

#adding title to the plot
# plt.title("Scatter Plot")

#setting the X and Y lables
# plt.xlabel('Day')
# plt.xlabel('Tip')

# plt.show()

'''This graph can be more meaningfull if we can add colors and also
change the size of the points. We can do this by using the c and s parameter respectively of the scatter function.
we can also the color bar using the colorbar() method.'''

import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv(r"D:\PYTHON\sample\tips.csv")
# plt.scatter(data['day'],data['tip'],c=data['size'],s=data['total_bill'])

# plt.title("Scatter Plot")
# plt.xlabel('Day')
# plt.xlabel('Tip')

# plt.colorbar()
# plt.show()




#Line Chart

data = pd.read_csv(r"D:\PYTHON\sample\tips.csv")

plt.plot(data['tip'])
plt.plot(data['size'])
plt.title("Scatter Plot")
plt.xlabel('Size')
plt.ylabel('Tip')
plt.show()


