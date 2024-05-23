# Automating NCBI BLAST Requests and Parse to CSV
Query from NCBI BLAST and parse into CSV file.

> [!NOTE]
> In progress. Currently operates on `blastn` (`nt` database).

> **TODO LIST**:
> - Operate on multiple BLAST databases.
> - Solve the problem of making high-data requests taking too long by grabbing BLAST locally.
> - Provide parameter inputs when executing the script. Can generalize BLAST result through limiting hit size or base pairs and such.

## Query

To query, all you have to do is execute the command `python blast.py` in Terminal, or PowerShell, inside the directory the Python file
is located in.

Depending on how many DNA sequences are in your FASTQ or FASTA file, it may take minutes or up to a day in order to complete the
BLAST request.
> (Currently working on automating multiple FASTQ/FASTA file BLASTs within one script execution. Put your files in `\<current folder\>/fastq` directory for this.)

## Dependencies

```js
pip install biopython
```
