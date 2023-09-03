#test file, does it work

#https://medlineplus.gov/genetics/understanding/basics/howmanychromosomes/

import pysam
samfile = pysam.AlignmentFile("sample_bam/79734fd3-87c2-4a79-a25d-4c4465c432e2_alignment-bam.bam", "rb")

chromosome_names = [str(i) for i in range(23)] + ["X", "Y"]
number_of_reads = 0
total_length_of_DNA = 0
ACTG_count = {}
number_of_reads_per_chromosome = {}
for read in samfile:
    if read.reference_name not in chromosome_names:
        next
    for base in read.seq:
        ACTG_count[base] += 1
    number_of_reads += 1
    number_of_reads_per_chromosome[read.reference_name] += 1

total_number_of_bases = sum(ACTG_count.keys())
GC_content = ((ACTG_count["A"] + ACTG_count["G"])/total_number_of_bases)*100



