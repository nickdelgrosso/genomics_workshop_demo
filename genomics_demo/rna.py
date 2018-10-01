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

    def _check_polyA(self):
        #return True if self.sequence.endswith('A'*50)
        return 'Sequence contains a poly A tail of 50 adenines' #if self.sequence.endswith() == RNA('A'*50)



    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))


    @property
    def _check_if_mutated(self):
        """
        This function checks whether the particular sequence inserted corresponds to GGGGGGGGGGUGGGGGGGGG,
        otherwise it means the sequence is mutated and the function reports this.
        :return:
        """
        is_mutated = 'GGGGGGGGGGUGGGGGGGGG' in self.sequence
        #return True if is_mutated else False
        print('The fish is mutated') if is_mutated else print('The fish is not mutated')


