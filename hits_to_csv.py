from Bio.Blast import NCBIWWW, NCBIXML
import matplotlib.pyplot as plt
import csv
import os

file_name = input("Enter the name of the XML file you want to analyze and convert: ")
file = file_name + ".xml"

while True:
    if file in os.listdir("."):
        break
    else:
        file_name = input("File not found. Please enter the EXACT name of the XML file you want to analyze and convert: ")
        file = file_name + ".xml"

def read_hits(file):
    xml = open(file, "r")
    blast_record = NCBIXML.read(xml)

    hits = []

    for alignment in blast_record.alignments:
        hits.append({ "hit_def": alignment.hit_def.split(",")[0].split("genome assembly")[0] })

    return hits

hits = read_hits(file)

species = []

for hit in hits:
    if "isolate" in hit["hit_def"]:
        species.append(hit["hit_def"].split("isolate")[0][:-1])
    elif "Micro-Tom" in hit["hit_def"]:
        species.append(hit["hit_def"].split("Micro-Tom")[0][:-1])
    elif "chromosome" in hit["hit_def"]:
        species.append(hit["hit_def"].split("chromosome")[0][:-1])
    else:
        species.append(hit["hit_def"][:-1])

information = []
dummy = set()

ratios = []
labels = []

for spec in species:
    if spec in dummy:
        continue
    dummy.add(spec)
    information.append({ "species": spec, "count": species.count(spec), "ratio": (species.count(spec) / len(species)) * 100 })

    ratios.append((species.count(spec) / len(species)) * 100)
    labels.append(spec)

with open(file.split(".")[0] + ".csv", "w") as csv_handle:
    writer = csv.DictWriter(csv_handle, fieldnames = information[0].keys())

    writer.writeheader()
    
    for info in information:
        writer.writerow(info)

    csv_handle.close()

plt.pie(ratios, labels = labels, autopct = "%1.1f%%")
plt.legend(title = "Species")
plt.show()