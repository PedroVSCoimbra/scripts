#fazer ifs para todos os reynolds

perfil=4S
angulo=2

files=`ls $1`

cd $1

i=0
b=0

for file in $files
do
((i++))
((b++))

  if [ $i -le 5 ];then
    mv $file "$perfil"01900A"$angulo"_"$b".jpg
  fi

  if [ $i -le 10 ];then
    mv $file "$perfil"12000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 15 ];then
    mv $file "$perfil"25000A"$angulo"_"$b".jpg
  fi

  if [ $b -eq 5 ];then
    b=0
  fi

done
