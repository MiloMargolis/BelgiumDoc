---
title: "Phase 3, here we come"
date: 2024-06-05
draft: false
description: "Group post for phase 3"
slug: "phase_3_post"
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
  - "milo_margolis"
  - "sydney_schulz"
  - "paolo_lanaro"
showAuthorsBadges : false
---

# Phase 3 is done!

# DS3000

### Sentiment Analysis

An essential aspect of the machine learning aspect of the project was relying on the sentiment analysis score. We were able to take advantage of a news api that already included the sentiment score of each news article so we did not have to find the score ourselves. 

The sentiment score assigns a numerical value to a piece of text based on whether the sentiment is positive, negative, or neutral. If a piece of text has a positive sentiment the score will be greater than 0 and less than 1, for a negative sentiment it is less than 0 and greater than -1. A neutral sentiment will have a score of 0. The higher the sentiment score, the more positive the piece of text is. 

The first step of performing a sentiment analysis is cleaning and preparing the data. This is done by ensuring all symbols and capitalizations are removed, removing stop words, and tokenizing the text. Tokenization splits the text into smaller words or phrases that will be assigned scores.

Next, the tokens are given a numerical score that expresses the importance of the word within the document. One way that this is done is through Term Frequency-Inverse Document Frequency. This divides the number of times that a term appears in text based on the entire text and measures how important a term is by the number of documents it appears in.

The next step is training the model. This can be done using the Naive Bayes formula. This is done by first counting the number of positive and negative scores in the training data, then for each word, the likelihood of it occurring in positive and negative documents is calculated. 

Once the model is trained, the probability of each sentence being either positive or negative is calculated. The score with the highest probability would be the sentiment for each sentence. 



### Features being used for ML

|  | date | sentiment | text | source_country | queried_country | url | Safety Index |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2019-06-12 18:48:59 | -0.308 | It’s time we start talking about climate chang... | mx | Russia | https://www.amnesty.org/en/latest/news/2019/06... | 0.585000 |  |
| 1 | 2019-07-12 17:14:00 | -0.108 | Even now, as more frequent "king tides" bubble... | us | China | https://edition.cnn.com/2019/07/11/us/miami-li... | 0.784286 |  |
| 2 | 2019-10-23 15:32:04 | 0.292 | The second meeting of the Board of senior memb... | uz | Russia | http://www.uzreport.com/sco-interbank-associat... | 0.585000 |  |
| 3 | 2019-10-23 15:34:13 | 0.398 | The Shanghai Cooperation Organization establis... | uz | Russia | http://www.uzreport.com/entrepreneur-committee... | 0.585000 |  |
| 4 | 2019-10-23 15:37:39 | 0.146 | All participants of the exhibition “Tea and Co... | uz | Russia | http://www.uzreport.com/over-7000-people-visit... | 0.585000 |  |

Above is an excerpt of our data frame used to create our machine learning algorithms. The text, url, and date features were pulled to give more information to the user and to allow them to explore text further.  The source country, queried_country, and safety index were used in our ML algorithms

For our first algorithm, we implemented a linear perceptron to try to identify if a piece of text would have a positive or negative sentiment depending on the country that that was queried. In order to do this, we used the safety index of the country to determine if it could be a predictor. We chose these features to see the relationship between the perceived safety of the queried nation and what the sentiment of the nation is in the media. If the safety score can predict a positive or negative sentiment, it may indicate to policy makers or pr specialists how the relative safety impression of a country is necessary to have a positive impression on other nations. 

For our second algorithm, we implemented a Random Forest Classify to attempt to classify what the source country of a piece of text may be. In order to do this, we used the queried country and sentiment of the country to attempt to predict which country may have published the text. Different nations have different impressions of nations and different motivations for writing about a nation in a specific way. If we are able to predict what nation wrote with a certain sentiment about a certain country, it will allow users to better understand the different impressions different nations have about their countries and how that is reflected in the sentiment of articles written. The code for our Random Forest Classifier is found in the assets folder.

### Linear Perceptron

For the manually implemented ML model, we chose a linear perceptron to assist with a user’s ability to classify a country’s generally perceived sentiment as being positive or negative based off of various news sources. 

Through various iterations of a weights vector, initialized with random weights, the linear perceptron algorithm updates the weight vector accordingly as it is checked against currently labeled values of the sentiment. As the vector is updated, be becomes increasingly better at predicting whether or not the sentiment of a provided country is positive or negative based on the safety score. From this updated and finished weight vector, we used the finalized weights to predict the anticipated sentiment of a provided country using its safety score.

### Issues Found During Model Exploration

The largest and most limiting factor of our model exploration was the limits of our dataset. We initially only pulled data from a few countries so that we would have tester data but unfortunately after that initial pull the API stopped working. Because of this, we have very few countries to actually make predictions on and as a result our models are not very good.

When creating the initial linear regression model, we found that there was a surprisingly low correlation of determination. One that made the linear model insignificant and unusual to a user attempting to query a country’s sentiment. From there we reevaluated the model to include more robust forms of classification as labeling a country as having generally good or bad sentiment based off of it’s associated safety score. 

After creating and editing the linear perceptron to be more capable of classifying certain countries as having high or low sentiment based on the safety score of a country, we ran into issues as the limited requests with the World News API prohibited us from getting a more robust training dataset and made these issues tricky to overcome. As we move forward, one of the main goals is going to be to see what different techniques from the API can be exhausted to see about grabbing more data.

When creating the random forest classifier, we faced further issues with the limited countries in our data frame as well as other issues. The initial iteration of the classifier was problematic because it falsely identified the vast majority of the countries as coming from the US. This was because in the training data, there was a much higher proportion of US source countries then any other nation. As a result, it was much safer for the model to almost always select US. In order to try to resolve this issue I tried using different classifiers to address the imbalance.

The first classifier that we tried to use was the SMOTE technique. (Synthetic Minority Oversampling Technique). With this technique, it prioritizes the minority classes. Unfortunately, I did not have enough unique classes for the code to run. 

The second classifier that we tried to use was the Balanced Random Forest Classifier. The BRFC allowed for more flexibility in the selection of bootstrap samples to attempt to address the imbalance. By testing out the sampling strategy, I was able to see if I can improve the model. I tested out the sampling strategies ‘all’ and ‘not majority’ to attempt to give the other countries besides the US more of a chance of appearing. Unfortunately, this classifier also did not work as it vastly underestimated the US and none of the returned predictions were the US. 

Because of this, I made a choice to stick with the initial Random Forest Classifier as although this model is still highly flawed, it does still sometimes correctly predict the US and China as the correct countries.

# CS3200

This week, in regards to updates and modifications made to our data tables, we added 7 tables related to either user activity or article data. The additional tables are as follows: 

- Weight Vector (generated)
- Likes (sourced)
- Saves (sourced)
- Shares (sourced)
- Filters (sourced)
- Recently Viewed (sourced)
- Trending Articles (generated)

Here is a list of the additional API routes with brief descriptions: 

1. **@activity.route('/filters', methods=['PUT'])
def put_filters():**
    
    Description: Updates the user preferences in the filters table according to user activity
    
2. **@activity.route('/filters', methods=['GET'])
def get_recently_viewed():**
    
    Description: Gets user’s the recently viewed articles from the recently viewed table 
    
3. **@activity.route('/filters', methods=['GET'])
def get_trending_articles():**
    
    Description: Gets the top trending articles from the trending articles table 
    
4. **@social.route("/likes", method=["POST"])
def add_likes():**
    
    Description: Adds new information to the likes tables based on the user id and activity date
    
5. **@social.route("/likes/<likeID>", method=["DELETE"])
def remove_likes(likeID):**
    
    Description: Deletes information from the likes table based on the user id and deletion date
    
6. **@social.route("/shares", method=["POST"])
def add_shares():**
    
    Description: Adds new information to the shares tables based on the user id and activity date
    
7. **@social.route("/shares/<sharesID>", method=["DELETE"])
def remove_shares(sharesID):**
    
    Description: Deletes information from the shares table based on the user id and deletion date
    
8. **@social.route("/saves", method=["POST"])
def add_saves():**
    
    Description: Adds new information to the saves tables based on the user id and activity date
    
9. **@social.route("/saves/<savesID>", method=["DELETE"])
def remove_saves(savesID):**
    
    Description: Deletes information from the saves table based on the user id and deletion date
    
10. **@customers.route('/Prediction/<country01>', methods=['GET'])
def predict_country_sentiment(country01):**
    
    Description: Gets the sentiment score of the selected country from the countries table based on the data science team’s ML regression model
    
11. **@article_data.route('/article_data', methods=['POST'])
def add_new_article():**
    
    Description: Adds a new article to the the articles table

### Issues

The main issue we ran into this phase was connecting the API to the database and the API to the frontend.
We kept getting status code 500 errors and this made our progress with the routes and the general middle and back end very slow.

### Screenshots of mocked up app

<img src="https://i.imgur.com/3saqZ8F.png" class="center"/>
<img src="https://i.imgur.com/wz2MywI.png" class="center"/>
<img src="https://i.imgur.com/OPKAjL1.png" class="center"/>

<img src="https://i.imgur.com/snR8RKO.png" class="center"/>
<img src="https://i.imgur.com/rp9fHUV.png" class="center"/>
<img src="https://i.imgur.com/A0NVxWF.png" class="center"/>

### Images of "calling the model"

<img src="https://i.imgur.com/wdygLXn.png" class="center"/>

Our API's "call to the ML model" isn't currently working because of the aformentioned status code 500 error, but we hope to get this done very soon.
