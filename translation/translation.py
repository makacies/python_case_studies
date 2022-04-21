import table

def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as file:
        seq = file.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string
    containg the corresponding sequence of amino acids. Nucleotides are
    translated in triplets using the transl_table dictionary; each amino acid
    is encoded with a string of length 1."""

    protein = ""

    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table.trnsl_table[codon]        

    return protein

prt = read_seq('protein.txt')
dna = read_seq('dna.txt')
translation = translate(dna[20:938])[:-1]
print(translation)
print(translation == prt)
