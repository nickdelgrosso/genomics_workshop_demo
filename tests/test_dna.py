from genomics_demo.dna import DNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')

def test_complimentary_sequence_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')

def test_find_start_codons():
    assert DNA('ATGGTACATGCGA').find_start_codons() == [0, 7]
