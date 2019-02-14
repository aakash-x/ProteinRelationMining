
# coding: utf-8

# In[ ]:


from urllib.request import urlopen,Request 
import bs4
import pandas as pd
import numpy as np

url = "https://www.ncbi.nlm.nih.gov/pubmed/?term=12194857"
request = Request(url)
beautiful = urlopen(request)
beautiful = beautiful.read()
beautiful
soup = bs4.BeautifulSoup(beautiful,"lxml")
print(soup.find_all('p'))


# In[ ]:




