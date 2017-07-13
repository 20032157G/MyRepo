%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
titanic=pd.read_csv("tb1_asg5.csv")
titanic["PassengerId"]=np.arange(1,len(titanic)+1)
titanic=titanic.set_index("PassengerId")
tips=pd.read_csv("tb2_asg5.csv")
class ttnc():
	@staticmethod
	def disp():
		j=sns.FacetGrid(titanic,hue="sex",size=5)
		j.map(plt.scatter,"fare","age",s=50,alpha=.7,linewidth=.5,edgecolor="white")
		j.add_legend()
		plt.show()
		#sns.lmplot(x="fare",y="age",hue="sex",data=titanic) 

	@staticmethod
	def sobrev():
		pd.crosstab(titanic.sex,titanic.survived,margins=True)
		N=sum(titanic["survived"]) #3
		print("Sobrevivieron: %s\n" % N)
		#f,ax=plt.subplots(figsize=(7,3)) 
		#sns.countplot(y="fare",data=titanic,color='y') #4
		
	@staticmethod
	def hist():
		plt.hist(titanic["fare"],color='y')
		plt.title("Histograma - Fare$")
		plt.ylabel("Frecuencias")
		plt.show()


class tps():
		
	@staticmethod
	def hist():
		plt.hist(tips["total_bill"],color='m')
		plt.title("Histograma - total_bill")
		plt.ylabel("Frecuencias")
		plt.show()
	
	@staticmethod
	def disp():
		j=sns.FacetGrid(tips,size=5)
		j.map(plt.scatter,"total_bill","tip",s=50,alpha=.7,linewidth=.5,edgecolor="white")
		j.add_legend()
		plt.show()
	
	@staticmethod
	def rel():
		j=sns.PairGrid(tips,vars=["total_bill","tip","size"],hue="size")
		j.map(plt.scatter)
		j.add_legend()
		plt.show()

	@staticmethod
	def disp2():
		j=sns.FacetGrid(tips,col="sex",hue="smoker")
		j.map(plt.scatter,"total_bill","tip")
		j.add_legend()
		plt.show()	
