#Sirve para obtener el link descargable del G*TH*B
oc1='github'
oc2='/blob'
oc_1='raw.githubusercontent'
echo "$*"|sed -e "s%$oc1%$oc_1%g"|sed -e "s%$oc2%%g"
