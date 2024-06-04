from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import os

fastq_folder = "fastq/"
genbank_folder = "genbank/"

process = input("Do you want to convert FASTQ files to FASTA files? (y/n): ")

while True:
    if process == "y" or process == "Y":
        for fastq_file in os.listdir(fastq_folder):
            print("Converting " + fastq_file + " to FASTA.")
            SeqIO.convert(fastq_folder + fastq_file, "fastq", fastq_folder + fastq_file.split(".")[0] + ".fasta", "fasta")

        print("Conversion complete.")
        break
    elif process == "n" or process == "N":
        print("Skipping FASTQ to FASTA conversion.")
        break
    else:
        process = input("Invalid input. Please enter 'y' or 'n': ")

process = input("Do you want to convert GenBank files to FASTA files? (y/n): ")

while True:
    if process == "y" or process == "Y":
        for genbank_file in os.listdir(genbank_folder):
            with open(genbank_file, "rU") as input_handle:
                with open(genbank_file.split(".")[0] + ".fasta", "w") as output_handle:
                    print("Converting " + genbank_file + " to FASTA.")
                    sequences = SeqIO.parse(input_handle, "genbank")
                    count = SeqIO.write(sequences, output_handle, "fasta")

        print("Conversion complete.")
        break
    elif process == "n" or process == "N":
        print("Skipping GenBank to FASTA conversion.")
        break
    else:
        process = input("Invalid input. Please enter 'y' or 'n': ")

print("** Terminating program. **")