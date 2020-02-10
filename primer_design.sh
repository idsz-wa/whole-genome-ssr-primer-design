#!/bin/bash
#useage: bash this.sh genome.fa prefix
#1 基因基因组数据寻找ssr
perl misa.pl $1
cat ${1}.misa  |awk 'NR>1 {print $1"\t"$6-150"\t"$7+150}' >${2}.bed 
bedtools getfasta -fi $1 -bed ${2}.bed -fo ${2}_misa.fa 
perl misa.pl ${2}_misa.fa
#确保此时输出的misa及fa文件中无 . 空格 等特殊字符
perl 1.primer_consrtuct/primer/p3_in.pl ${2}_misa.fa.misa
#使用primer 设计引物
/1.primer_consrtuct/primer/primer3-2.3.7/src/primer3_core -p3_settings_file=../1.primer_consrtuct/primer/p3.settings.file --default_version=1 --output=${2}_misa.fa.p3out ${2}_misa.fa.p3in
#规范primer3 的输出
python /1.primer_consrtuct/reform_ssr_output.py ${2}_misa.fa.p3out ${2}_misa.fa.re.p3out
#执行epcr来筛选引物
#需要genome.fa 来进行建库操作
sed '1d' ${2}_misa.re.p3out | while read i
do
left=$(echo $i |awk '{print $2}')
right=$(echo $i |awk '{print $3}')
id=$(echo $i |awk '{print $1}')
echo -e "$id" >>chr1_xx_misa.epcr.out
re-PCR -s gnome.hash -n 1 -g 1 $left $right 100-250 >> ${2}.epcr.out
done
#合并epcr与引物结果
awk  -F "\t" 'BEGIN{index_temp=0;seq_temp="x";OFS="\t"}{if($1 ~ /NC_/){if(index_temp==1){print seq_temp,chr,strand,start,end,stats};seq_temp=$1;index_temp=0}else if($1 ~ /#/){PASS}else if($1=="STS-1"){chr=$2;strand=$3;start=$4;end=$5;stats=$8;index_temp++}}' ${2}.epcr.out >${2}.epcr.reform.out

