from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# corpus=["I think I sent this to the worng e-mail address the first time(selliott rather than shelliott), but we are going to Woody's tonight if you want to join us.",
#     "I think we are going to stay in town and meet you at the airport.  Is the surgery considered serious? How long till he recovers?",
#     "Have you bought any new DVD's recently?  If so, which ones? ",
#     "What is the market for IAH Jan-Mar HDD swaps (we are looking to BUY)?  How does this compare to the 30 yr avg?Thanks for your help."]

# vectorizer=CountVectorizer()
#
# transformer = TfidfTransformer()
# tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
from sklearn.feature_extraction.text import TfidfVectorizer
# print tfidf

corpus = ['i said you are loser',
      'i need an apple',
      'my mother ask me go to school',
      'i going now' ]
vectorizer = TfidfVectorizer(min_df=1)
vectorizer.fit_transform(corpus)
print vectorizer.get_feature_names()
print vectorizer.fit_transform(corpus).toarray()