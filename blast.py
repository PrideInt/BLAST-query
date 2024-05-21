from Bio.Blast import NCBIWWW, NCBIXML

alignment_num = 10
hitlist_size_num = 10

result_handle = NCBIWWW.qblast(program="blastn", database="nt", sequence="", alignments=alignment_num, hitlist_size=hitlist_size_num)

print(result_handle.read())

with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
    out_handle.close()

blast_record = NCBIXML.read(result_handle)

print(blast_record.alignments)

for alignment in blast_record.alignments:
    print(alignment.title)
    print(alignment.hit_def)

result_handle.close()