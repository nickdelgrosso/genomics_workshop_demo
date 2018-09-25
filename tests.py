from dna import DNA

try:
    assert DNA('ATB')
except ValueError:
    pass
assert DNA('GTC').complimentary_sequence == DNA('CAG')
assert DNA('ATC').complimentary_sequence == DNA('TAG')
assert DNA('ATC').complimentary_sequence == 'TAG'

print('it worked!')