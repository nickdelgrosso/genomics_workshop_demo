complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
import numpy as np

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
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))

    def get_aa_sequence(self):

        aa = {
            'UUU' : 'Phe',
            'UUC' : 'Phe',
            'UUA' : 'Leu',
            'UUG' : 'Leu',
            'CUU' : 'Leu',
            'CUC' : 'Leu',
            'CUA' : 'Leu',
            'CUG' : 'Leu',
            'AUU' : 'Ile',
            'AUC' : 'Ile',
            'AUA' : 'Ile',
            'AUG' : 'Met',

        }

        aa_sequence = [aa[self.sequence[i:i+3:1]] for i in range(0, len(self.sequence), 3)]

        return '-'.join(aa_sequence)

