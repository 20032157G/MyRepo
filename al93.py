import math
import numpy as np
class bnlddr():
	def __init__(self,x,y,b):
		self.x=x
		self.y=y
		self.b=b
	
	def alg1(self):
		Y=np.binary_repr(self.y)
		z=self.x
		for i in range(1,len(Y)):
			z=pow(z,2)
			if (Y[i] == "1"):
				z=z*self.x
		return z

	def alg2(self):
		Y=np.binary_repr(self.y)
		z=self.x
		a=1
		for i in range(0,len(Y)-1):
			if(Y[i]=="1"):
				a=z*a
			z=pow(z,2)
		return a*z

	def alg3(self):
		Y=np.base_repr(self.y,self.b)
		print(Y)
		z=1
		for i in range(0,len(Y)):
			c=0 #np.trunc(np.log(int(Y[i]))/np.log(2))
			d=int(Y[i])
			while (d%2==0)and(d>0):
				c+=1
				d/=2
				#d=int(Y[i])//pow(2,c)
			z=z*pow(pow(self.x,d),pow(2,c))
			#print(len(Y),i,c,d,z)
			if (i<len(Y)-1):
				z=pow(z,pow(2,self.b))
			#print(z)
			#print ("###########")
		return z
	
