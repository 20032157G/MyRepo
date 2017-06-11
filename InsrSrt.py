class Insrc():
	def __init__(self,x):
		self.x=x

	def Insrc1(self):
		x=self.x
		for i in range(1,len(x)):
			ax=x[i]
			k=i-1
			sw=False
			while not sw and k>=0:
				if ax<x[k]:
					x[k+1]=x[k]
					k-=1
				else:
					sw=True
			x[k+1]=ax
		return x

	def Insrc2(self):
		x=self.x
		for i in range(1,len(x)):
			ax=x[i]
			p=0
			u=i-1
			while p<=u:
				c=(p+u)//2
				if ax<x[c]:
					u=c-1
				else:
					p=c+1
			for k in range(i-1,p-1,-1):
				x[k+1]=x[k]
			x[p]=ax
		return x
