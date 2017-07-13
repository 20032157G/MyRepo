#url1m="https://www.kaggle.com"
#url1d="/c/titanic/data"
#pg1=$(wget -O - $url1m$url1d|egrep "train.csv"|grep -o -P "(?<=61194,).*(?=981,)"|sed -nr 's/.*:"(.*)",.*/\1/p')
#wget --directory-prefix=. $url1m$pg1

PW ()
{
	url=$*
	echo $url|awk -F'/blob' '{print $1$2}'|sed -e 's%://%://raw.%g'
}

#Obtener tabla train.csv
url1="http://github.com/nybbles/kaggle/blob/master/train.csv"
#url1d=$(echo $url1|awk -F'/blob' '{print $1$2}'|sed -e 's%://%://raw.%g')
url1d=$(PW $url1)
PgF1="./tb1_asg5.csv"
python2.7 GtFl.py $url1d $PgF1

#Obtener tabla tips.csv
url2="http://github.com/wesm/pydata-book/blob/master/ch08/tips.csv"
url2d=$(PW $url2)
PsF2="./tb2_asg5.csv"
python2.7 GtFl.py $url2d $PsF2

