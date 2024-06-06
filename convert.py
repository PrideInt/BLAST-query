from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import os

fastq_folder = "fastq/"

if not os.path.exists(fastq_folder):
    os.makedirs(fastq_folder)

genbank_folder = "genbank/"

if not os.path.exists(genbank_folder):
    os.makedirs(genbank_folder)

process = input("Do you want to convert all FASTQ files to FASTA files? (y/n): ")
converted = False
stop_conversion = False

while True:
    if not os.listdir(fastq_folder):
        print("No FASTQ files found.")
        break
    
    if process == "y" or process == "Y":
        for fastq_file in os.listdir(fastq_folder):
            if (fastq_file.split(".")[0] + ".fasta" in os.listdir(fastq_folder)) and not fastq_file.endswith(".fasta"):
                print("Skipping " + fastq_file + " as it already has been converted to FASTA format.")
                continue
            elif fastq_file.endswith(".fasta"):
                continue
            else:
                print("Converting " + fastq_file + " to FASTA.")
                SeqIO.convert(fastq_folder + fastq_file, "fastq", fastq_folder + fastq_file.split(".")[0] + ".fasta", "fasta")
                converted = True

        print("Conversion complete." if converted else "Skipping FASTQ files.")
        break
    elif process == "n" or process == "N":
        print("Select the FASTQ files you want to convert to FASTA.\n")

        for fastq_file in os.listdir(fastq_folder):
            if (fastq_file.split(".")[0] + ".fasta" in os.listdir(fastq_folder)) and not fastq_file.endswith(".fasta"):
                print("Skipping " + fastq_file + " as it already has been converted to FASTA format.")
                continue
            elif fastq_file.endswith(".fasta"):
                continue
            else:
                if stop_conversion:
                    break

                convert = input("Do you want to convert " + fastq_file + " to FASTA? (y/n/q): ")

                if convert == "q" or convert == "Q" or convert == "quit" or convert == "cancel":
                    print("Cancelling the rest of the conversion.")
                    break

                while True:
                    if convert == "y" or convert == "Y":
                        print("Converting " + fastq_file + " to FASTA.")
                        SeqIO.convert(fastq_folder + fastq_file, "fastq", fastq_folder + fastq_file.split(".")[0] + ".fasta", "fasta")
                        converted = True
                        break
                    elif convert == "n" or convert == "N":
                        print("Skipping " + fastq_file + ".")
                        break
                    elif convert == "q" or convert == "Q" or convert == "quit" or convert == "cancel":
                        print("Cancelling the rest of the conversion.")
                        stop_conversion = True
                        break
                    else:
                        convert = input("Invalid input. Please enter 'y' or 'n', or 'q' to quit: ")

        print("Conversion complete." if converted else "Skipping FASTQ files.")
        break
    elif process == "q" or process == "Q" or process == "quit" or process == "cancel":
        print("Cancelling the rest of the conversion.")
        break
    else:
        process = input("Invalid input. Please enter 'y' or 'n', or 'q' to quit: ")

process = input("Do you want to convert all GENBANK files to FASTA files? (y/n): ")
converted = False
stop_conversion = False

while True:
    if not os.listdir(genbank_folder):
        print("No GENBANK files found.")
        break

    if process == "y" or process == "Y":
        for genbank_file in os.listdir(genbank_folder):
            if (genbank_file.split(".")[0] + ".fasta" in os.listdir(genbank_folder)) and not genbank_file.endswith(".fasta"):
                print("Skipping " + genbank_file + " as it already has been converted to FASTA format.")
                continue
            elif genbank_file.endswith(".fasta"):
                continue
            else:
                with open(genbank_file, "rU") as input_handle:
                    with open(genbank_file.split(".")[0] + ".fasta", "w") as output_handle:
                        print("Converting " + genbank_file + " to FASTA.")
                        sequences = SeqIO.parse(input_handle, "genbank")
                        count = SeqIO.write(sequences, output_handle, "fasta")
                        converted = True

        print("Conversion complete." if converted else "Skipping GENBANK files.")
        break
    elif process == "n" or process == "N":
        print("Select the GENBANK files you want to convert to FASTA.\n")

        for genbank_file in os.listdir(genbank_folder):
            if (genbank_file.split(".")[0] + ".fasta" in os.listdir(genbank_folder)) and not genbank_file.endswith(".fasta"):
                print("Skipping " + genbank_file + " as it already has been converted to FASTA format.")
                continue
            elif genbank_file.endswith(".fasta"):
                continue
            else:
                if stop_conversion:
                    break

                convert = input("Do you want to convert " + genbank_file + " to FASTA? (y/n/q): ")

                if convert == "q" or convert == "Q" or convert == "quit" or convert == "cancel":
                    print("Cancelling the rest of the conversion.")
                    break

                while True:
                    if convert == "y" or convert == "Y":
                        with open(genbank_file, "rU") as input_handle:
                            with open(genbank_file.split(".")[0] + ".fasta", "w") as output_handle:
                                print("Converting " + genbank_file + " to FASTA.")
                                sequences = SeqIO.parse(input_handle, "genbank")
                                count = SeqIO.write(sequences, output_handle, "fasta")
                                converted = True
                        break
                    elif convert == "n" or convert == "N":
                        print("Skipping " + genbank_file + ".")
                        break
                    elif convert == "q" or convert == "Q" or convert == "quit" or convert == "cancel":
                        print("Cancelling the rest of the conversion.")
                        stop_conversion = True
                        break
                    else:
                        convert = input("Invalid input. Please enter 'y' or 'n', or 'q' to quit: ")

        print("Conversion complete." if converted else "Skipping GENBANK files.")
        break
    elif process == "q" or process == "Q" or process == "quit" or process == "cancel":
        print("Cancelling the rest of the conversion.")
        break
    else:
        process = input("Invalid input. Please enter 'y' or 'n', or 'q' to quit: ")

print("** Terminating program. **")