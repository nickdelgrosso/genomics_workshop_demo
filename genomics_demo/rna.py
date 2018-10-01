complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
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

    def check_polyA(self):
        """
        Checks whether the RNA sequence contains a poly A tail of 50 adenines.
        :return: True if yes, False otherwise
        """
        return True if self.sequence.endswith('A'*50) else False

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))

