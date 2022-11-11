### Tribute:
Who said data scientists can't be romantic? I would like to thank my wife for inspiring me to create this project to keep her entertained with movies of her interest.

### Description:

How many times have we wondered what movie to watch? How many times did we want to watch a movie that's reminiscent to a previous movie that we liked? Well we won't have to wonder much more.

### Objective:

We want to find similarities among movies depending on their respective plots. In other words we can find movies that talk about war, a baby that became super human, or some classical mafia style movies about families.

### Data Source:

We will use IMDB's top 100 movies as our dataset. Using this <a href = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'><u>url</u></a> we will perform web scraping to extract both the titles and the plot description of our movies.

### Approach:

We will tokenize and stem each and every word of the plot in order to find similarities much more efficiently.

<ul>
    <li>Tokenization: Tokenization is the process by which we break down articles into individual sentences or words, as needed. Besides the tokenization method provided by NLTK, we might have to perform additional filtration to remove tokens which are entirely numeric values or punctuation (i.e Ignore symbols such as . ! ? , and numerical values such as 1973, 2nd etc...).</li>
<br>
<li>Stemming: Stemming is the process by which we bring down a word from its different forms to the root word. This helps us establish meaning to different forms of the same words without having to deal with each form separately.  (i.e amazing, amazement, amazingly all share the same stem which is 'amaz').</li>
</ul>

### Create TfidfVectorizer:

Computers do not understand text. These are machines only capable of understanding numbers and performing numerical computation. Hence, we must convert our textual plot summaries to numbers for the computer to be able to extract meaning from them. One simple method of doing this would be to count all the occurrences of each word in the entire vocabulary and return the counts in a vector. Hence the usage of CountVectorizer.

Consider the word 'the'. It appears quite frequently in almost all movie plots and will have a high count in each case. But obviously, it isn't the theme of all the movies! Term Frequency-Inverse Document Frequency (TF-IDF) is one method which overcomes the shortcomings of CountVectorizer. The Term Frequency of a word is the measure of how often it appears in a document, while the Inverse Document Frequency is the parameter which reduces the importance of a word if it frequently appears in several documents.

### Kmeans and Clustering:

To determine how closely one movie is related to the other by the help of unsupervised learning, we can use clustering techniques. Clustering is the method of grouping together a number of items such that they exhibit similar properties. According to the measure of similarity desired, a given sample of items can have one or more clusters.

We get the following distribution for the clusters:

<img src = 'assets/clusters_dist.png'> </img>

### Result:

Here is a dendrogram of all movies that are similar to each other:

<img src = 'assets/final clusters.png'> </img>