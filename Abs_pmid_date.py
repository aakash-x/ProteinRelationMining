from pubmed_lookup import PubMedLookup
import pandas as pd
email = 'rakesh161@gmail.com'
k=['12194857','28835279','17683935','17984323','25791428','20466727','24667209','23425014','22874558']
abst=[]
title=[]
year=[]
for i in k:
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/'+i
    lookup = PubMedLookup(url, email)
    from pubmed_lookup import Publication
    publication = Publication(lookup)    # Use 'resolve_doi=False' to keep DOI UR
    #print("ID :"+i)
    #print("Abstract :"+repr(publication.abstract))
    abst.append(repr(publication.abstract))
    title.append(publication.title)
    year.append(publication.year)
d = {'PMID': k,'Title':title,'Year':year, 'Abstract': abst}
df = pd.DataFrame(data=d)
df.to_csv('CSV_9.csv', sep='\t')
print("Done")