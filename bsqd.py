class seq():
	@staticmethod
	def mt1(x,lf):
		for i in range(len(x)):
			if x[i]==lf:
				print('Elemento se encontro')
				print('Posicion: ',i+1)
	@staticmethod
	def mt2(x,lf):
		i=0
		while (x[i]!=lf)and(i<len(x)):
			i+=1
		if x[i]==lf:
			print('Elemento encontrado en posicion: ',i+1)
		else:
			print('El numero no se encontro')
	@staticmethod
	def mt3(x,lf):
		i=0
		while (x[i]!=lf)and(i<len(x)):
			i+=1
		if x[i]==lf:
			print('Se encontro en posicion: ',i+1)
		else:
			print('No se encontro')

	@staticmethod
	def met4(x,lf):
		i=0
		while i<len(x):
			if lf==x[i]:
				print('Se encontro en la posicion: ',i+1)
				i=len(x)
			else:
				i+=1

	@staticmethod
	def mt5(x,lf):
		i=0
		#x[len(x)]=lf
		x=x+[lf]
		while x[i]!=lf:
			i+=1
		if i==len(x):
			print('No se encuentra ',lf)
		else:
			print('Ha sido encontrado en posicion: ',i+1)

	@staticmethod
	def metf6(x,lf):
		i=0
		b=False
		while (not b)and (i<len(x)):
			if x[i]==lf:
				b=True
			i+=1
		if b:
			print('Se encontro en la posicion: ',i+1)
		else:
			print('No se encontro')

	@staticmethod
	def met7(x,lf):
		i=0
		b=False
		while i<len(x):
			if x[i]==lf:
				b=True
				print('Se encontro en la posicion: ',i+1)
			i+=1
		if not b:
			print('No se encontro')

	@staticmethod
	def met8(x,lf):
		b=False
		i=0
		pass

	@staticmethod
	def met9(x,lf):
		b=False
		for i in range(len(x)):
			if x[i]==lf:
				b=True
				break
		if b:
			print('Elemento encontrado en posicion: ',i+1)
		else:
			print('No se encontro')
class bnr():
	@staticmethod
	def bsNm(x,n):
		l=1
		h=len(x)-1
		c=(l+h)//2
		while (l<=h)and (x[c]!=n):
			if n<x[c]:
				h=c-1
			else:
				l=c+1
			c=(l+h)//2
		if n==x[c]:
			print('Se encontro en posicion: ',c+1)
		else:
			print('No se encontro')
	@staticmethod
	def bsNb(x,str):
		b=False
		l=0
		h=len(x)-1
		while (not b)and(l<=h):
			c=(l+h)//2
			if x[c]==str:
				b=True
			else:
				if x[c]>str:
					h=c-1
				else:
					l=c+1
		if b:
			print('Se encontro en posicion: ',c+1)
		else:
			print('No se encontro')
