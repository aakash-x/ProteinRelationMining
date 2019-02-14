from pubmed_lookup import PubMedLookup
email = 'rakesh161@gmail.com'
k=['12194857','28835279','17683935','17984323','25791428','20466727','24667209','23425014','22874558']
for i in k:
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/'+i
    lookup = PubMedLookup(url, email)
    from pubmed_lookup import Publication
    publication = Publication(lookup)    # Use 'resolve_doi=False' to keep DOI UR
    print("ID :"+i)
    print("Abstract :"+repr(publication.abstract))


