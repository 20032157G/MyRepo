class bubbl():
	def __init__(self,x):
		self.x=x

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
					x[j],x[j+1]=x[j+1],x[j]	#ax=x[j]
					#x[j]=x[j+1]
					#x[j+1]=ax
		return x

	def bub3(self):
		x=self.x
		flg=False
		i=1
		while not flg and i<len(x):	#flg | i<len(x):
			flg=True
			for k in range(0,len(x)-i):
				if x[k]>x[k+1]:
					x[k],x[k+1]=x[k+1],x[k]#ax=x[k]
					#x[k]=x[k+1]
					#x[k+1]=ax
					flg=False
			i+=1
		return x

