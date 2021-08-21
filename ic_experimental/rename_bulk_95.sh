#fazer ifs para todos os reynolds

perfil=4S
angulo=4

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
    mv $file "$perfil"03000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 15 ];then
    mv $file "$perfil"04000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 20 ];then
    mv $file "$perfil"05000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 25 ];then
    mv $file "$perfil"06000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 30 ];then
    mv $file "$perfil"07000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 35 ];then
    mv $file "$perfil"08000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 40 ];then
    mv $file "$perfil"09000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 45 ];then
    mv $file "$perfil"10000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 50 ];then
    mv $file "$perfil"11000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 55 ];then
    mv $file "$perfil"12000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 60 ];then
    mv $file "$perfil"13000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 65 ];then
    mv $file "$perfil"14000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 70 ];then
    mv $file "$perfil"15000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 75 ];then
    mv $file "$perfil"16000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 80 ];then
    mv $file "$perfil"17000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 85 ];then
    mv $file "$perfil"18000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 90 ];then
    mv $file "$perfil"19000A"$angulo"_"$b".jpg
  fi

  if [ $i -le 95 ];then
    mv $file "$perfil"20000A"$angulo"_"$b".jpg
  fi

  if [ $b -eq 5 ];then
    b=0
  fi

done
