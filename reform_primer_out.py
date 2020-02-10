#coding:utf-8
import sys
import re
input_file=sys.argv[1]
output_file=sys.argv[2]
output=open(output_file,"w")
output.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("sequence_id","primer_left","primer_right","seq_info_left","seq_info_right","tm_left","tm_right","gc_left","gc_right","product_size"))
# input_file="/mnt/data/test/2.mei_ssr/chr1_misa.p3out"
for line in open(input_file):
    line=line.strip("\n")
    line1=re.split('_|=', line)
    # print(line)
    if line.startswith("SEQUENCE_ID="):
        i=1
        sequence_id=line.split("=")[1]
    if line.startswith("PRIMER_LEFT") and 'SEQUENCE' in line1:
        primer_left=line.split("=")[1]
        # print(primer_left)
    if line.startswith("PRIMER_RIGHT") and 'SEQUENCE' in line1:
        primer_right=line.split("=")[1]
    if line.startswith("PRIMER_LEFT") and len(line1)==4:
        seq_info_left=line.split("=")[1]
    if line.startswith("PRIMER_RIGHT") and len(line1)==4:
        seq_info_right = line.split("=")[1]
    if line.startswith("PRIMER_LEFT") and 'TM' in line1:
        tm_left=line.split("=")[1]
    if line.startswith("PRIMER_RIGHT") and 'TM' in line1:
        tm_right=line.split("=")[1]
    if line.startswith("PRIMER_LEFT") and 'GC' in line1:
        gc_left=line.split("=")[1]
    if line.startswith("PRIMER_RIGHT") and 'GC' in line1:
        gc_right=line.split("=")[1]
    if line.startswith("PRIMER_PAIR") and 'SIZE' in line1:
        product_size=line.split("=")[1]
        output.write("{}_{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(sequence_id,i,primer_left,primer_right,seq_info_left,seq_info_right,tm_left,tm_right,gc_left,gc_right,product_size))
        i+=1
        
