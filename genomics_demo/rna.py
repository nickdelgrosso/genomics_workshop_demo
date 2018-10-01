complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

type_motifs = {'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA': 'polyA tail mRNA',
              'GAGAGUA': 'clover leaf loop tRNA', 'AAGUGC':'microRNA'}

class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        # self.motif = motif
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and U")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        return all(nucleotide in 'GCAU' for nucleotide in self.sequence.upper())

    def type_rna(self):
        """
        Scans the entire RNA sequence and returns the first motif type
        found from dictionary type_motifs above;
        multiple instances or motifs beyond the first match are not reported
        """
        for index, mo in enumerate(type_motifs):
            if mo in self.sequence.upper():
                return type_motifs[mo]
            else:
                pass
                # return print('not this type')

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt] for nt in self.sequence.upper()))

