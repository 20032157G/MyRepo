#Descargar el archivo del github, var entrada url de visualizacion y ruta
#class url():
#	@staticmethod
#	def gesture():
import requests as rq
import sys
url=sys.argv[1]
fl=sys.argv[2]
r=rq.get(url)
tx=r.text
f=open(fl,"w")
f.write(tx)

