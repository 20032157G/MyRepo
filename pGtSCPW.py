#Nos retorna el source code de una pagina web
class url:
	def __init__(self,x):
		self.x=x
	def page(self):
		x=self.x
		f=open("links.txt")
		#pwc="Nada"
		if self.x>0 and self.x<7:
			f=open("links.txt")
			import urllib2			
			url=f.readlines()[self.x-1]
			print(url)
			pw=urllib2.urlopen(url)
			pwc=pw.read()
			f="page"+str(x)+".pw"
			ff=open(f,"w")
			ff.write(pwc)
		return pwc

