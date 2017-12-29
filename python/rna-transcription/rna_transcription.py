def to_rna(dna_strand):
    table = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna_strand=""

    for nucleotide in dna_strand:
        if nucleotide not in table.keys():
            raise ValueError("Not a valid DNA nucleotide")
        else:
            rna_strand += table[nucleotide]
    return rna_strand
