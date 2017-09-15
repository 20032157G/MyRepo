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
		N=self.b
		for i in range(1,len(Y)):
			z=pow(z,2)%N
			if (Y[i] == "1"):
				z=z*self.x%N
		return z

	def alg2(self):
		Y=np.binary_repr(self.y)
		N=self.b
		z=self.x
		a=1
		for i in range(0,len(Y)-1):
			if(Y[i]=="1"):
				a=z*a%N
			z=pow(z,2)%N
		return a*z%N

	def alg3(self):
		B=self.b
		b=int(math.log(B,2))
		Y=np.base_repr(self.y,B)
		#print(Y)
		z=1
		for i in range(0,len(Y)):
			c=0 #np.trunc(np.log(int(Y[i]))/np.log(2))
			yi=int(Y[len(Y)-1-i])
			d=int(yi)
			while (d%2==0)and(d>0):
				c+=1
				d/=2
				#d=int(Y[i])//pow(2,c)
			z=z*pow(pow(self.x,d),pow(2,c))
			#print(len(Y),i,c,d,z)
			if (i>0):
				z=pow(z,pow(2,b))
			#print(z)
			#print ("###########")
		return z
	
	def alg4(self):
		b=self.b
		x=self.x
		Y=np.base_repr(self.y,b)
		z=1
		for i in range(0,len(Y)):
			yi=int(Y[len(Y)-1-i])
			z=z*pow(pow(x,yi),pow(b,i))
		return z
