from genomics_demo.dna import DNA
import pytest


def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')


def test_complimentary_sequence_works():
    assert DNA('GTC').compliment == DNA('CAG')
    assert DNA('ATC').compliment == DNA('TAG')


def test_find_start_codons():
    """New test to test the function to find start codons"""
    assert DNA('ATGGTACATGCGA').find_start_codons() == [0, 7]


def test_transcribe():
    assert DNA('GTC').transcribe() == 'GAC'
    assert DNA('ATC').transcribe() == 'GAU'

def test_gc_content():
    assert DNA('ATTTATGGCC').gc_content == 0.4
    assert DNA('AGGTATGGCC').gc_content == 0.6
    assert DNA('ATAT').gc_content == 0
