
# genomics_demo_workshop

This is a demo of a genomics python package

## Installation

```
pip install git+https://github.com/nickdelgrosso/genomics_workshop_demo
```

## Usage

```python
from genomics_demo import DNA
dna_strand = DNA('AGTCAGC')  # Make DNA strand
dna_strand.complimentary_sequence  # outputs "TCAGTCG"
```


