# camkart
Search Engine for Nikon Cameras

Contributors : Gaurav Kumar, Palash Mittal, Anchit Navelkar, Buddha Prakash, Shubham Saxena, Utpal, Sandesh C

###1. Objectives

Our objective for this project was to build a search system for Nikon Camera which not only provides highly relevant content in response to user’s natural language queries but also provide a ranked list of retrieved products on the basis of the sentiment score of the product reviews (obtained from Flipkart), price and various other features. The search engine should produce various search filters for price, sentiment etc. and provide a simple user friendly interface.

###2. Approach

We crawled the data from Flipkart using Nutch and BeautifulSoup and decided upon a set of metadata which might be used in the indexing.
We then populated the metadata and created the database of all the products and fed it to solr for Indexing. 
Sentiment Analysis was performed on the reviews for each product and user friendly interface for queries was implemented using Django Framework.

###3. Query Processing Algorithm

The query is passed to solr index which fetches an initial list of ranked documents based on the Solr scoring model which consists of tf (term freq.), idf (inv. doc. freq.), coord (Coordination Factor), fieldNorm (Field length) parameters . This list is filtered using  a boolean model on the input range filter values . This filtered list of documents is then sorted on the sentiment score of the documents ( each documents corresponds to one camera ) based on the reviews obtained by the product to obtain the final ranked list of documents ( products ) .

###4. Crawling

Obtained list of product URLs from Flipkart.com using BeautifulSoup
Fed list of URLs as seed to Nutch
Crawled each product page till depth 1 and obtained product data , other relevant data was obtained using beautifulSoup

###5. Metadata

We chose the following metadata for indexing:<br>
Link of the product on flipkart<br>
Color of product<br>
Image url<br>
Price<br>
Megapixels<br>
Name of the product<br>
Number of people who have reviewed the product<br>
Number of people who have rated the product<br>
Average rating of the product<br>
10 reviews<br>
Type of Camera (DSLR etc)<br>
Type of sensor used<br>
Average Sentiment score of the reviews.<br>

Populating the metadata: We used Python library BeautifulSoup to crawl the urls. We then parsed the webpages to get the relevant selected metadata from the respective tags of crawled xml files and fed the populated metadata into django database.

###6. Indexing ( Documents Indexed : 436 )

We built an inverted index with the help of Solr. Solr inverts a page-centric data structure (page->words) to a keyword-centric data structure (word->pages).Then the index is stored by Solr in in a directory called index in the data directory.

Then,we specified the schema in a file schema.xml.The following fields were used :<br>
Document text<br>
Product price<br>
Average rating of product<br>
Number of ratings<br>
Sentiment score<br>

After data is added to Solr, it goes through analysis phase where it goes through a series of transformations Examples of transformations include lower-casing, removing word stems etc. The end result of the analysis are a series of tokens which are then added to the index, generated using NGramFilterFactory of Solr Library.

###7. Solr scoring model

The score given to a document by Solr in response to a query is scored on the following parameters:<br>
tf : term frequency of the token in a document . <br>
idf : reciprocal of the frequency of the token in the corpus .<br>
coord : Coordination Factor . The more query terms that are found in the document , the higher its contribution to the score .<br>
fieldNorm : Field length . The more words that a field contains , the lower it’s score . This factor penalizes document with longer field values . <br>

###8. PreProcessing

We performed a number of preprocessing steps on the reviews before performing sentiment analysis. We followed the following text normalization procedure<br>

Tokenized the reviews and converted the text to lowercase.<br>
Remove special characters. For eg, !@#%^&.<br>
Removed multiple occurrences of letters in a word.For eg, haaaapy -> haappy<br>
Performed spell correction on the word. For Eg, haapy - > happy<br>
Removed all the stop words in the tokenized text<br>
Performed Stemming to reduce the words to their base form. We used the Porter Stemmer for best results.<br>

###9. Sentiment Analysis
Sentiment Polarity Classification of reviews done using Sentiwordnet
Sentiwordnet is a publicly lexical resource for opinion mining 
Wordnet provides each Wordnet synset 's' three numerical scores Obj('s'), Pos('s') and Neg('s')
These scores describe the objectivity, positivity, and negativity of the terms contained in the synset
Each review classified into positive, negative and neutral
Review assigned sentiment score of +1, -1 and 0 respectively
Product assigned a sentiment score as the average of sentiment score of 10 product reviews

###10. User Interface and its Features

User friendly and intuitive interface.
Frontend designed using JQuery and Bootstrap framework
Django framework as backend integrated with Solr indexing, which was implemented using Haystack.

Natural language queries are supported.
Features to sort relevant results obtained on the basis of price or rating or sentiment score.
Filters have been implemented for price, rating, number of ratings that a product obtained and sentiment score.
Selection of a product redirects user to product page on Flipkart.

