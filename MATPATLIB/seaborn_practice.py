import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np

# df=sb.load_dataset("tips")
# print(df)
# sb.barplot(x='day',y='total_bill',data=df)
# plt.show()

# df=sb.load_dataset("tips")
# print(df)

# sb.barplot(x='day',y='total_bill',hue='sex',data=df)
# plt.show()

# sb.barplot(x='total_bill',y='day',hue='sex',data=df)
# plt.show()


#histogram gram plot

histogram=sb.load_dataset('iris')


# print(histogram)
# print(histogram.sepal_width)
# print(histogram.petal_width)
# sb.set_style("darkgrid")
# plt.title("Distribution of sepal width")
# plt.hist(histogram.sepal_width)
# plt.show()

# plt.hist(histogram.sepal_width,bins=7)
# plt.show()

# plt.hist(histogram.sepal_width,bins=np.arange(1.75,5,0.65))   (numpay ma milcha(suru,end,interval))



#multiple histogram


# iris_setosa=histogram[histogram.species=='setosa']
# iris_versicolor=histogram[histogram.species=='versicolor']
# iris_viginica=histogram[histogram.species=='virginica']
# plt.hist(iris_setosa.sepal_width,alpha=0.9)
# plt.hist(iris_versicolor.sepal_width,alpha=0.9)
# plt.show()

#Stacking
# plt.title("Distribution of Sepal Width")
# plt.hist([iris_setosa.sepal_width,iris_versicolor.sepal_width,iris_viginica.sepal_width],bins=np.arange(1,5,0.25),stacked=True)
# plt.legend(['setosa','versicolor','virginica'])
# plt.show()

#Scatter plotting
flower_df=sb.load_dataset('iris')
print(flower_df)

number=flower_df.species.unique()
print(number)

# plt.plot(flower_df.petal_length,flower_df.petal_width)
# plt.show()

# sb.scatterplot(x=flower_df.petal_length,y=flower_df.petal_width)
# plt.show()

sb.scatterplot(x=flower_df.petal_length,y=flower_df.petal_width,hue=flower_df.species,s=25)
plt.show()

