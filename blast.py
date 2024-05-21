from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import os
import csv

# Read the sequence from the file
# first_record = next(SeqIO.parse("test.fastq", "fastq"))
'''
for record in SeqIO.parse("test.fastq", "fastq"):
    print(record.seq)
'''

# Put all your FASTQ files in the "fastq" folder.
# Then, we will convert all the FASTQ files to FASTA files so that we can BLAST.

'''
fastq_folder = "fastq/"

for fastq_file in os.listdir(fastq_folder):
    print(fastq_file)
    SeqIO.convert(fastq_folder + fastq_file, "fastq", fastq_folder + fastq_file.split(".")[0] + ".fasta", "fasta")
'''

fasta = open("test.fasta")

result_handle = NCBIWWW.qblast(program="blastn", database="nt", sequence=fasta.read())

print(result_handle.read())

with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
    out_handle.close()

blast_record = NCBIXML.read(result_handle)

print(blast_record.alignments)

elements = []

for alignment in blast_record.alignments:
    print(alignment.title)
    print(alignment.hit_def)

    elements.append({ "title": alignment.title, "hit_def": alignment.hit_def })

with open("my_blast.csv", "w") as csv_handle:
    csv_writer = csv.writer(csv_handle)
    csv_writer.writerows(elements)
    csv_handle.close()

result_handle.close()