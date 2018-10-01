from genomics_demo.rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')

def test_mutated_sequence_works():
    #assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == True
    assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == print('The fish is mutated')
    assert RNA('GGGGGGGGGGUGGGGUUGGG')._check_if_mutated == print('The fish is not mutated')

def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'


