def to_rna(dna_strand):
    transcripted_nucleotides = []
    s = ""
    for x in dna_strand:
        if x == "G":
            transcripted_nucleotides.append("C")
        elif x == "C":
            transcripted_nucleotides.append("G")
        elif x == "T":
            transcripted_nucleotides.append("A")
        elif x == "A":
            transcripted_nucleotides.append("U")
    return s.join(transcripted_nucleotides)

