from Bio import Entrez
from Bio import Medline

MAX_COUNT = 6678227
TERM = 'protein'

print('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
Entrez.email = 'A.N.Other@example.com'
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(h)
print('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
ids = result['IdList']
print("Done")