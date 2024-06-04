# Automating NCBI BLAST Requests and Parse to CSV
Query from NCBI BLAST and parse into CSV file.

> [!NOTE]
> In progress. Currently operates on `blastn` (`nt` database).

> **TODO LIST**:
> - Operate on multiple BLAST databases.
> - Solve the problem of making high-data requests taking too long by grabbing BLAST locally.
> - Provide parameter inputs when executing the script. Can generalize BLAST result through limiting hit size or base pairs and such.

## Conversion

You are able to convert multiple FASTQ or GENBANK files by placing them into a folder labeled `fastq` (for FASTQ files) and `genbank`
(for GENBANK files). This folder should be in the same directory/folder as where `convert.py` is located.

To convert these files, execute the command `python convert.py` in Terminal, or PowerShell, inside the same directory `convert.py` is
located in.

An example prompt you will be shown:

```
<< Do you want to convert FASTQ files to FASTA files? (y/n):
>> y
<< Converting test.fastq to FASTA.
<< Conversion complete.
>> Do you want to convert GENBANK files to FASTA files? (y/n):
>> n
<< Skipping GenBank to FASTA conversion.
<< ** Terminating program. **
```

Inputting `y` or `Y` will convert all FASTQ/GENBANK files while `n` or `N` will skip all the FASTQ/GENBANK files for conversion.

## To CSV

The script `hits_to_csv.py` allows the user to convert data collected from NCBI BLAST into a CSV file that can be read.

(You are able to get this data by downloading the XML file of your BLAST results by heading over to **"Recent Results"** at NCBI BLAST,
clicking a job under **Request ID**, click where it says **"Download All"** next to the row that says **"RID"**, and selecting **XML**)

Place the XML file into the folder where the script is located, then change where it says `file = "test.xml"` to `file = "<your xml file>.xml"`,
replacing `<your xml file>` with the name of your XML file.

Then, you execute `python hits_to_csv.py` in Terminal, or PowerShell, and it will convert the data found here into a CSV file.

## Automating Graph Creation

Additionally, when you run `python hits_to_csv.py`, it will show you a graph representation of your data in the form of a pie chart.

## Query

To query, all you have to do is execute the command `python blast.py` inside the directory the Python file
is located in.

Depending on how many nucleotide sequences are in your FASTQ or FASTA file, it may take minutes or up to a day in order to complete the
BLAST request.
> Currently working on handling data from Request IDs instead rather than have this program running on a machine for hours at a time.

## Dependencies

```js
pip install biopython
```

```js
pip install matplotlib
```