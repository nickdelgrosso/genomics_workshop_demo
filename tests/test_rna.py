from genomics_demo.rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')


def test_check_polyA():
    assert RNA('A'*50)._check_polyA() == 'Sequence contains a poly A tail of 50 adenines'