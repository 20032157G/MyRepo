class Intrcmb():
	def __init__(self,x):
		self.x=x

	def b1it(self):
		x=self.x
		for i in range(len(x)-1):
			if x[i]>x[i+1]:
				ax=x[i]
				x[i]=x[i+1]
				x[i+1]=ax

	def b1it(self):
		x=self.x
		for i in range(len(x)-1):
			if x[i]>x[i+1]:
				ax=x[i]
				x[i]=x[i+1]
				x[i+1]=ax

	def bub1(self):
		x=self.x
		for i in range(0,len(x)-1):
			for j in range(len(x)-1):
				if x[j]>x[j+1]:
					x[j],x[j+1]=x[j+1],x[j]#ax=x[j]
					#x[j]=x[j+1]
					#x[j+1]=ax
		return x

	def bub2(self):
		x=self.x
		for i in range(0,len(x)-1):
			for j in range(0,len(x)-1):
				if x[j]>x[j+1]:
					x[j],x[j+1]=x[j+1],x[j]	
		return x

	def bub3(self):
		x=self.x
		flg=False
		i=1
		while not flg and i<len(x):
			flg=True
			for k in range(0,len(x)-i):
				if x[k]>x[k+1]:
					x[k],x[k+1]=x[k+1],x[k]
					flg=False
			i+=1
		return x

class Insrc():
	def __init__(self,x):
		self.x=x

	def Im1(self):
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

	def Im2(self):
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
class slcn():
	@staticmethod
	def sm1():
		pass

	def sm2():
		pass

	@staticmethod
	def sm4(x):
		i=0
		while i<len(x)-1:
			ax=x[i]
			k=i
			j=i
			while j<len(x)-1:
				j+=1
				if x[j]<ax:
					ax=x[j]
					k=j
			x[k]=x[i]
			x[i]=ax
			i+=1

	@staticmethod
	def sm4_2(x):
		i=0
		while i<len(x)-1:
			ax=x[i]
			k=i
			j=i
			while j<len(x)-1:
				j+=1
				if x[j]<ax:
					ax=x[j]
					k=j
			x[k]=x[i]
			x[i]=ax
			i+=1

	@staticmethod
	def sm4_3(x):
		for i in range(0,len(x)-1):
			ax=x[i]
			k=i
			for j in range(i+1,len(x)):
				if x[j]<ax:
					ax=x[j]
					k=j
			x[k]=x[i]
			x[i]=ax

	@staticmethod
	def sh1(x):
		N=len(x)//2
		sl=N
		while sl>0:
			for i in range(sl,len(x)): 
				j=i-sl
				while j>=0:
					k=j+sl
					if x[j]<=x[k]:
						j=0
					else:
						slcn().cambio(x,j,k)
					j-=sl
			sl//=2
		return x
	@staticmethod
	def cambio(x,i,j):
		ax=x[i]
		x[i]=x[j]
		x[j]=ax 
