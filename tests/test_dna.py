from genomics_demo.dna import DNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')

def test_complimentary_sequence_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')



#def test_gc_content_sequence_works():
 #   assert DNA('GC').gc_content > 0.5
def test_is_gc_rich():
    assert DNA('GTGT').gc_content() == 0.5
 #   length = len(sequence)
  #  c_count = sequence.upper().count('C')
   # g_count = sequence.upp
