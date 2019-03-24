from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import nltk
import re

from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
FileName = ("1.txt")
ps = PorterStemmer() 


with open(FileName, 'r') as file:
	lines_in_file = file.read()
	nltk_lower=lines_in_file.lower()
	nltk_tokens = nltk.word_tokenize(nltk_lower) 
	withot_stop=set(nltk_tokens) - en_stops
	print withot_stop
	print "\n"
	print "Number of Words: " , len(withot_stop)   


# choose some words to be stemmed 


for w in withot_stop: 
	print(w, " : ", ps.stem(w)) 


txt = "1990/12/31"

month=["Jan","Mar","May","Jul","Sep","Sept","Nov","Feb","Apr","Jun","Aug","Oct","Dec"]
days=["Sat","Sun","Mon","Tues","Wed","Thurs","Fri"]

x = re.search("^(19|20)\d\d[- /.//](0[1-9]|1[012])[- /.//](0[1-9]|[12][0-9]|3[01])$", txt)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")