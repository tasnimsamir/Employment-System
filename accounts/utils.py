from jobs.models import job,applicant
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances

nltk.download('stopwords')
nltk.download('wordnet')
lst_stopwords = nltk.corpus.stopwords.words("english")

def utils_preprocess_text(text, flg_stemm=True, flg_lemm=False):
    ## clean (convert to lowercase and remove punctuations and characters and then strip)
    text = re.sub(r'[^\w\s]', ' ', str(text).lower().strip())
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", text)
    text = re.sub("\d+", " ", text)
   
            
    # ## Tokenize (convert from string to list)
    lst_text = text.split()
    lst_text = [word for word in lst_text if word not in lst_stopwords]

    ## Stemming (remove -ing, -ly, ...)
    if flg_stemm == True:
        ps = nltk.stem.porter.PorterStemmer()
        lst_text = [ps.stem(word) for word in lst_text]
                
    ## Lemmatisation (convert the word into root word)
    if flg_lemm == True:
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        lst_text = [lem.lemmatize(word) for word in lst_text]
            
    ## back to string from list
    text = " ".join(lst_text)
    return text




def match(job_description , applicant_bio):
    pair_matrix = (utils_preprocess_text(job_description),utils_preprocess_text(applicant_bio))
    cleaned_features = TfidfVectorizer().fit(pair_matrix).transform(pair_matrix)
    similarity_score = cosine_distances(cleaned_features[0],cleaned_features[1])
    return similarity_score