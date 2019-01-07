#!/bin/bash


declare -a arr=(
'/home/milton/Documentos/I-dual/problems/4_5.json'
'/home/milton/Documentos/I-dual/problems/4_15.json'
'/home/milton/Documentos/I-dual/problems/4_25.json'
'/home/milton/Documentos/I-dual/problems/4_35.json'
'/home/milton/Documentos/I-dual/problems/4_45.json'
'/home/milton/Documentos/I-dual/problems/4_55.json'
'/home/milton/Documentos/I-dual/problems/4_65.json'
'/home/milton/Documentos/I-dual/problems/4_75.json'
'/home/milton/Documentos/I-dual/problems/4_85.json'
'/home/milton/Documentos/I-dual/problems/4_95.json'
'/home/milton/Documentos/I-dual/problems/4_105.json'
'/home/milton/Documentos/I-dual/problems/4_115.json'
'/home/milton/Documentos/I-dual/problems/4_125.json'
'/home/milton/Documentos/I-dual/problems/4_135.json'
'/home/milton/Documentos/I-dual/problems/4_145.json'
'/home/milton/Documentos/I-dual/problems/4_155.json'
'/home/milton/Documentos/I-dual/problems/4_165.json'
'/home/milton/Documentos/I-dual/problems/4_175.json'
'/home/milton/Documentos/I-dual/problems/4_185.json'
'/home/milton/Documentos/I-dual/problems/4_195.json'
'/home/milton/Documentos/I-dual/problems/4_205.json'
'/home/milton/Documentos/I-dual/problems/4_215.json'
'/home/milton/Documentos/I-dual/problems/4_225.json'
'/home/milton/Documentos/I-dual/problems/4_235.json'
'/home/milton/Documentos/I-dual/problems/4_245.json'
'/home/milton/Documentos/I-dual/problems/4_255.json'
'/home/milton/Documentos/I-dual/problems/4_265.json'
'/home/milton/Documentos/I-dual/problems/4_275.json'
'/home/milton/Documentos/I-dual/problems/4_285.json'
'/home/milton/Documentos/I-dual/problems/4_295.json'
'/home/milton/Documentos/I-dual/problems/4_305.json'
'/home/milton/Documentos/I-dual/problems/4_315.json'
'/home/milton/Documentos/I-dual/problems/4_325.json'
'/home/milton/Documentos/I-dual/problems/4_335.json'
'/home/milton/Documentos/I-dual/problems/4_345.json'
'/home/milton/Documentos/I-dual/problems/4_355.json'
'/home/milton/Documentos/I-dual/problems/4_365.json'
'/home/milton/Documentos/I-dual/problems/4_375.json'
'/home/milton/Documentos/I-dual/problems/4_385.json'
'/home/milton/Documentos/I-dual/problems/4_395.json'
'/home/milton/Documentos/I-dual/problems/4_405.json'
'/home/milton/Documentos/I-dual/problems/4_415.json'
'/home/milton/Documentos/I-dual/problems/4_425.json'
'/home/milton/Documentos/I-dual/problems/4_435.json'
'/home/milton/Documentos/I-dual/problems/4_445.json'
'/home/milton/Documentos/I-dual/problems/4_455.json'
'/home/milton/Documentos/I-dual/problems/4_465.json'
'/home/milton/Documentos/I-dual/problems/4_475.json'
'/home/milton/Documentos/I-dual/problems/4_485.json'
'/home/milton/Documentos/I-dual/problems/4_495.json'
'/home/milton/Documentos/I-dual/problems/4_505.json'
'/home/milton/Documentos/I-dual/problems/4_515.json'
'/home/milton/Documentos/I-dual/problems/4_525.json'
'/home/milton/Documentos/I-dual/problems/4_535.json'
'/home/milton/Documentos/I-dual/problems/4_545.json'
'/home/milton/Documentos/I-dual/problems/4_555.json'
'/home/milton/Documentos/I-dual/problems/4_565.json'
'/home/milton/Documentos/I-dual/problems/4_575.json'
'/home/milton/Documentos/I-dual/problems/4_585.json'
'/home/milton/Documentos/I-dual/problems/4_595.json'


		
	)


echo "vi dual lp"

for i in "${arr[@]}"
do
	
	echo  $i >> $1"-vi.dat"
	echo "VI"
	echo $i
	python mainExp.py $i $2 0 -t $3>> $1"-vi.dat"
	echo  $i >> $1"-dualLP.dat"
	echo "DUAL-LP"
	echo $i
	python mainExp.py $i $2 1 -t $3>> $1"-dualLP.dat"
done

# echo "dual LP"

# for i in "${arr[@]}"
# do
# 	echo $i
# 	echo  $i >> $1"-dualLP.dat"
	
# done