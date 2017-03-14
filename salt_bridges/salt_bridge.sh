sim1=$1 
sim2=$2
length=$3

for sim in $sim1 $sim2
do
python get_sum_sb.py --inp $sim --sim_length $length
Rscript sum_double.R count_$sim $length ${sim%.*}\_saltbridge.txt
done

rm count*.

Rscript merge.R ${sim1%.*}\_saltbridge.txt ${sim2%.*}\_saltbridge.txt
