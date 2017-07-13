######################################
#fl=open($path,"w")
#Ibtener tabla de datos
#####################################
#path=$1
if [ "$(echo "$1"|grep -E ^\-?[0-9]+$)" = '' ];then
	printf "$1\nIngresar un numero natural \n"
else
	if [ $1 -eq 1 ]||[ $1 -eq 2 ]||[ $1 -eq 5 ]||[ $1 -eq 6 ];then
		if [ $path=="" ];then
			path="/media/disk/Asgns/Table$1.csv"
		fi
		case $1 in
		6)	export delim2='id="0.E2.80.939"'
			export delim3="mw-headline"
			export delim1="wikitable sortable"
			export delim4="#############################################################################################################"
			export report="report.file"
			y=$(cat page6.pw|sed -n "/$delim1/,/$delim2/p"|sed '1d;$d') #header
			x=$(cat page6.pw|sed -n "/$delim2/,/$delim3/p"|sed ':a;$!N;1,2ba;P;$d;D') #texto entre delim sin 2 ultimas lineas
#printf "$y\n$delim4\n$x\n$delim4\n">>$report
			for i in {2..7} ;do
				case $i in 
				2) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|awk -F'<' '{print $2}'|sed 's/^.*>//')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')" #awk -F'"' '{print $6}' campo 2 entre comillas		
					;;
				3) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|awk -F'<' '{print $2}'|sed 's/^.*>//')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')" # sed 's/^.*<td>//'|awk -F'</td>' '{print $1}'
					;;
				4) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|awk -F'<' '{print $2}'|sed 's/^.*>//')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g'|sed 's/^.*-0000//')"
					;;
				5) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|awk -F'<' '{print $4}'|sed 's/^.*>//')"
					;;
				6) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|awk -F'<' '{print $2}'|sed 's/^.*>//')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|awk -F'(' '{print $1}'|awk -F'<' '{print $2}'|sed 's/^.*>//')"
					;;
				7) 	export h$(($i-1))="$(echo "$y"|awk -v v="$i" 'BEGIN{FS="\n";RS="</tr>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$x"|awk -v v="$i" 'BEGIN{RS="</tr>\n";FS="\n"} {print $v}'|awk -F'<' '{print $4}'|sed 's/^.*>//')"
					;;
				*)	echo "No hay caso aqui"
					;;
				esac
	#hx=h$(($i-1))
	#cx=c$(($i-1))
	#printf "${!hx}\n${!cx}\n$delim4\n"
			done
			i=1
			for ((i=1;i<7;i++));do
				cx=c$i
				hx=h$i
				if [ $i -eq 1 ];then
					t=$(printf "${!hx}\n${!cx}\n")
#		echo "$t"|sed -n 1,4p
#		echo $delim4
				else
#		echo "$t"|sed -n 1,4p
#		print "$delim4\n\n"
					t="$(paste <(printf "$t\n") <(printf "${!hx}\n${!cx}\n") -d ',')"
#		echo "$t"|sed -n 1,4p
#		echo $delim4
				fi
			done
			echo "$t">$path
			printf "\e[5mTabla creada en el medio: %s...\e[0m\n" "$path"
			;;
		2)	d1='age 15+'
			d2='projection'
			d3='Flag_of_Belarus'
			d4='id="2015_WHO_data_for_OECD_countries'
			h=$(cat page2.pw|sed -n "/$d1/,/$d3/p"|sed ':a;$!N;1,3ba;P;$d;D'|sed '1d;2d')
			c=$(cat page2.pw|sed -n "/$d2/,/$d4/p"|sed ':a;$!N;1,3ba;P;$d;D'|sed '1d;2d')
			#echo "$h"|awk 'BEGIN{RS="</tr>\n";FS="</th>/n<th>"} {print}'
#|sed 's/\(<\)[^<]*\(>\)//g'
#|sed '$d'|awk 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print }'
			for (( i=2;i<12;i++ ));do
				case $i in
				3)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*title="(.*)">.*/\1/p')"
					;;
				2|4)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				5)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				6)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				7)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				8)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				9)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				10)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				11)	export h$(($i-1))="$(echo "$h"|awk -v v=$(($i-1)) 'BEGIN{RS="</tr>\n";FS="</th>\n<th>"} {print $v}'|sed 's/\(<\)[^<]*\(>\)//g')"
					export c$(($i-1))="$(echo "$c"|awk -v v=$i 'BEGIN{RS="</tr>\n<tr>";FS="\n"} {print $v}'|sed -nr 's/.*>(.*)<.*/\1/p')"
					;;
				*)	printf "\e[5mNo hay caso aqui\e[0m"
					;;
				esac
				#hx=h$(($i-1))
				#cx=c$(($i-1))
				#printf "%s\n%s\n" ${!hx} $delim4
			done
			for (( i=1;i<11;i++));do
				hx=h$i
				cx=c$i
				hx=$(echo ${!hx}|xargs)
				#printf "%s\n" "$ht"
				#cx=${!cx}
				#echo "$ht"
				#echo "_________________"
				#printf "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" $h1 $h2 $h3 $h4 $h5 $h6 $h7 $h8 
				#printf "%s\n%s\n" "$ht" "$cx"|sed -n 1,10p
				if [ $i -eq 1 ];then
					t=$(printf '%s\n%s\n' "$hx" "${!cx}")
					#printf "%s\n%s\n" $hx $cx|sed -n 1,10p
				else
					#echo "$t"|wc -l
					#echo $(printf "$hx\n$cx"|xargs)
					t=$(paste <(printf '%s\n' "$t") <(printf '%s\n%s\n' "$hx" "${!cx}") -d ',')
				fi
				#echo "$t"|sed -n 1,10p
				#echo "#################################################################" 
			done
			echo "$t">$path
			printf "Se ha guardado como: \e[5m.csv\e[0men $path\n"	
			;;
		5)	echo "Opc5"
			d1='historical-prices'
			d2='Close price adjusted'
			N=$(cat "page5.pw" |sed -n 5p|grep -o -P "(?<=$d1).*(?=$d2)"|awk 'BEGIN{RS="</tr>";FS="</td><td>";ORS="\n\n";OFS="\n"} {print NR}'|sed '/^\s*$/d'|wc -l)
			h=$(cat "page5.pw"|sed -n 5p|grep -o -P "(?<=$d1).*(?=$d2)"|awk 'BEGIN{RS="</tr>";FS="</td><td>";ORS="\n\n";OFS="\n"} {print $1}'|sed -n 1p)
			c=$(cat "page5.pw" |sed -n 5p|grep -o -P "(?<=$d1).*(?=$d2)"|awk 'BEGIN{RS="</tr>";FS="</td><td>";ORS="\n\n";OFS="\n"} {print $1}'|sed -n 3,$(($N*2-2))p)
			#echo $N
			#echo "$c"|sed -n 1,6p
			for ((i=1;i<8;i++));do
				hx=$(echo "$h"|awk -v v=$i 'BEGIN{RS="\n";FS="</span>";OFS="\n"} {print $v}'|sed 's/^.*>//')
				cx=$(echo "$c"|awk -v v=$i 'BEGIN{RS="\n";FS="</span>";OFS="\n"} {print $v}'|sed 's/^.*>//'|sed '/^$/d')
				#echo "$cx"|sed -n 1,6p
				#echo "#############################"
				if [ $i -eq 1 ];then
					t=$(printf '%s\n%s\n' "$hx" "$cx")
				else
					t=$(paste <(printf '%s\n' "$t") <(printf '%s\n%s\n' "$hx" "$cx") -d '\t')
				fi
				#printf "$cx"|sed -n 1,6p
			done
			echo "$t">$path
			echo -e "Tabla generada \e[5mTabla$i.csv\e[0m en: $path"
			;;
		1)	lnk=$(cat links.txt|sed -n 1p)
			echo $i
			python GPW.py 1
			cat page1.pw>$(dirname $path)"page1.pw"
			;;
		*)	printf "Otro caso"
			;;
		esac
#r=$(shuf -e 2-7 -n 1)
#vr=c${r}
#N=$(echo ${!vr}|grep -ne ^)
#for (( i=0; i<$N; i++ ))
#do
#	f=""
#	for (( j=2; j<8; j++ ))
#	do
#		if [ $i==0 ]
#		then
#			hx=h$j
#			if [ $j<7 ]
#			then
#				f1+=${hx}","
#			else
#				f1+=${hx}
#				echo ${f1} > $path
#				f1=""
#			fi
#		fi
#		cx=c$j
#		if [ $j<7  ]
#		then
#		if [ $i==0 ]
#		then
#			hx=h$j
#			if [ $j<7 ]
#			then
#				f1+=${hx}","
#			else
#				f1+=${hx}
#				echo ${f1} > $path
#				f1=""
#			fi
#		fi
#		cx=c$j
#		if [ $j<7  ]
#		then
#	for (( j=2; j<8; j++ ))
#	do
	fi
fi
