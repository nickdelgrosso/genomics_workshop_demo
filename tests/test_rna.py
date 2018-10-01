from genomics_demo.rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')


def test_check_polyA():
    assert RNA('A' * 50).check_polyA()
    assert RNA('A' * 49).check_polyA() is False
