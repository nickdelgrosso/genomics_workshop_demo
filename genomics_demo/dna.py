complimentary_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and T")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "DNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        return all(nucleotide in 'GCAT' for nucleotide in self.sequence.upper())

    @property
    def gc_content(self):
        return sum(nucleotide in 'GC' for nucleotide in self.sequence.upper())/len(self.sequence)

    @property
    def compliment(self):
        return DNA(''.join(complimentary_nucleotides[nt] for nt in self.sequence.upper()))

    def find_start_codons(self):
        """ Finds the start codon of a coding DNA sequence"""
        indices = []
        index = -1

        while True:
            index = self.sequence.find('ATG', index + 1)
            if index == -1:
                return indices
            indices.append(index)

    def transcribe(self):
        """Transcribes a DNA sequence into a RNA sequence"""
        compliment = self.compliment.sequence
        reverse_compliment = (''.join(compliment[i] for i in range(len(compliment)-1, -1, -1)))
        reverse_compliment_rna = reverse_compliment.replace('T', 'U')
        return reverse_compliment_rna
