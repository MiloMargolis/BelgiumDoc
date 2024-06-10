---
title: "Wrapping up"
date: 2024-06-09
draft: false
description: "Group post for phase 4"
slug: "phase_4_post"
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
  - "milo_margolis"
  - "sydney_schulz"
  - "paolo_lanaro"
showAuthorsBadges : false
---

# Final Team Blog Post

### *[Link to Presentation](https://www.canva.com/design/DAGHpTTTWaA/A8dmkHP0Ak5TUgpQdA5Nsg/edit?utm_content=DAGHpTTTWaA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Description of the ML models:

### Multiple Linear Regression

For the first machine learning model that we constructed, we used a manual implementation of a linear regression using various different features about articles entered in our local database to predict the sentiment of articles a user may be interested in understanding more about. 

To fully understand this model, we will walk through how a user would interact with the model and what this would trigger throughout the app. 

1. Training the Model: When beginning, a user may enter the app as a System Administrator that allows for each ML model to be trained. When doing so, a user will push a button that says “Train the Model” within the “Train Multiple Linear Regression Model” page. Once this button is clicked, a request to the SQL table containing information about the articles is made. This information is then passed along to a training function found in “api\backend\ml_models\Multiple_Lin_Reg.py” where the raw data from the database is cleaned. In the cleaning process, various features are extracted such as the word count of each article, the safety score of the country it was written from, and a one hot encoding of the country it was written about. The purpose of the one hot encoding is to provide more robust determining factors that allow for more information to predict the final sentiment. Trained against each article’s actual sentiment score, the calculation $(X^TX)^{-1}X^Ty$ determines the coefficients for the general $y=mx+b$ prediction equation.
2. Predicting Sentiment: As a user navigates to act as Katerina’s persona, they have the option to calculate a article’s sentiment score. They must provide the country the article was written in, the country the article was written about, and the text of the article itself. Using the user input, we find the word count and a one hot encoding of the country the article was written from. These features are used to construct an input vector that is multiplied with the weight vector that is stored from above and produce a predicted sentiment score. Along with this calculated sentiment score, we return an actual library’s interpretation of the sentiment score of the provided text for a user to compare their input with. 

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from collections import Counter

X = news_data.drop(columns=['sentiment', 'text', 'queried_country']).values  
y = news_data['sentiment'].values  

# Identify the source country for each row
source_countries = news_data.filter(like='source_country_').idxmax(axis=1)

# Count the occurrences of each source country
source_counts = Counter(source_countries)

# Create a mask for observations that have more than 1 instance
mask = source_countries.map(source_counts) > 1

# Initialize an array for predictions, of appropriate length
y_preds = np.empty(mask.sum())
y_pred_idx = 0

X = add_bias_column(X)

# Loop through the observation and perform LOOCV
for obs in range(len(y) - 1):
    if not mask.iloc[obs]:
        continue
    
    # Exclude the single row/true y belonging to obs
    loocv_trainX = np.concatenate((X[:obs, :], X[obs+1:, :]), axis=0)
    loocv_trainy = np.concatenate((y[:obs], y[obs+1:]), axis=0)
    
    # Initialize and train the linear regression model
    loocv_regress = LinearRegression()
    loocv_regress.fit(loocv_trainX, loocv_trainy)
    
    # getting m
    XtXinv = np.linalg.inv(np.matmul(loocv_trainX.T, loocv_trainX))
    m = np.matmul(XtXinv, np.matmul(loocv_trainX.T, loocv_trainy))

    # Predict the held-out observation and store it
    y_preds[y_pred_idx] = loocv_regress.predict(loocv_trainX[obs].reshape(1, -1))[0]
    y_pred_idx += 1

```

### Random Forest Classifier

Our second machine learning model that we implemented was the Random Forest Classifier. The goal of this classifier is to predict the source country, the country where an article was written from, based on text and country of question. Based on the text, we can grab the word count and sentiment score and use those features in our model. 

Using a Random Forest Classifier is preferable for this data as it allows us to be able to classify what country a piece of text may have come from based on numerical and non-numerical coded features. A Random Forest Classifier allows us to take advantage of the simplicity of decision tress while also limiting overfitting which is a consequence of decision trees.

Decision trees have a flowchart like structure where each branch of the tree represents the outcome of each decision made. In order to determine which attribute is best to split on, a metric called the Gini impurity score is used. 

$G = 1 - \sum_{i=1}^{J} p_i^2$ 

The Gini impurity measures the likelihood of an incorrect classification of a randomly chosen element based on the number of elements in a dataset.

The random forest classifier uses a set of varying decision trees in order to classify the source country. To determine the decision trees to be used in the random forest classifier, bootstrap aggregating, or bagging,  is used.

By implementing bagging, the model is able to train multiple models on slightly different subsets. In a random forest model, the predictions are combined and the variance of the resulting ensemble model is reduced, leading to better generalization performance.

After implementing this random forest model, a consequence that resulted was the vast majority of predictions were for the United States as the Unites States made up the majority of the data samples in the training data. 

Because of this, we tested different Random Forest models that prioritized the unpopular values to try to force the model to select other countries as the predicted country. Unfortunately, the two models that we tested overcompensated and returned the US very few times. In order to prioritize the accuracy of the model, we decided to use the first random forest classier.

```python
# read in data
news_data = pd.read_csv('Data News Sources.csv')

# drop the columns im not using
news_data.drop(['Unnamed: 0', 'date', 'url', 'Safety Index'], axis=1, inplace=True)
news_data.dropna(axis=0, inplace=True)

# adding word count
news_data['word_count'] = news_data['text'].apply(lambda x: len(x.split()))

# drop the columns im not using
news_data.drop(['text'], axis=1, inplace=True)
news_data.dropna(axis=0, inplace=True)

# one hot encoding
news_data = pd.get_dummies(news_data, columns=['queried_country'], drop_first=True)

# X and y
X = news_data.drop(columns=['source_country']) 
y = news_data['source_country']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# implement the random forest regressor
rf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

# fit the model
rf.fit(X_train, y_train)

# Making predictions on the data
predictions = rf.predict(X_train)
```

### General Model Impl in Software Architecture and Database Design:

![Untitled](Final%20Team%20Blog%20Post%200887f307d2264b56b5455dcbc8dbf560/Untitled.png)

On the frontend, our software architecture is broken down into four primary user personas: a foreign policy advisor, a PR specialist, a traveler, and a system administrator. Each persona interacts with the web app in a unique manner. At the initial rendering of the site, the user arrives on the home page where they can select which persona they would like. Each user persona stores its first name, role, and unique user ID in the Streamlit session state. This persona information is used throughout the app, both for a more meaningful UI and to seamlessly integrate data into the DDL. The frontend also includes a general information page which provides an overview of the purpose of our web app and a pinboard map which visualizes the location of all the articles in our database.

### Software Architecture Diagram:

This diagram provides a general overview of our codebase architecture 

```python
diplomatic-data
├── api # contains the majority of the routes and ml models
│   └── backend
│       ├── activity # info about users interacting with the articles is pushed to the databases
│       ├── article_data # article retrival and storage along with info about trending articles
│       ├── assets
│       │   └── utils # useful routes retriving lists of countries for users to choose when inputting info
│       ├── db_connection # inializing a dictionary based database cursor
│       ├── ml_models # implementations of both the Multiple Linear Regression and Random Forest Classifier
│       ├── models # routes where users can input prediction preferences and storing training info
│       └── social # user's interactions with liking / saving / recently viewed articles
				# also contains dockerfiles that allow for container to be setup
├── app
│   └── src # the frontent portion
│       ├── assets # various imagery and csvs used for loading databases
│       ├── modules # introductory pages for the home and navigation between other pages
│       └── pages # each user persona's pages along with the system admin 
				# holds the config.toml file allowing for configuration of themes
├── database # the sql databases, tables, and insertion files
└── fake_data # mockaroo fake data
```

### Persona #1 Foreign Policy Advisor:

The first user persona (foreign policy advisor) redirects to a page with four buttons: a profile view, an add article page, a view article page, and a random forest ML model page. The profile view shows three dropdowns listing the user’s recently viewed articles, likes, and saves. Each dropdown uses a GET route to retrieve the views, likes, or saves table. These tables update automatically according to the foreign policy advisor’s in-app activity. The profile view also shows the most trending article of the week, filtered by the unique number of views in the past month. The add article page allows the foreign policy advisor to manually add articles to our database. The user is able to add the article date, time, content, country written about, country written from, and URL. The app dynamically calculates a sentiment score based on the text and then adds the article to the database. The view article page allows the user to randomly view an article from the database. The user can like, save, or move on to the next article. Recent views, likes, and saves are all added to the database. Once again, the user can access their recently viewed articles, likes, and saves on the profile view page. Finally, on the random forest page, the user can provide the text of an article they are interested in and the country the article is being written about. From there, the ML model predicts which country the article is most likely being written from using a Random Forest Classifier (RFC). The RFC is trained on various features of articles from an extensive database. As Anton, a user can input the country of interest that the article is intended to be written about as well as the text of the article. This information is sent to the RFC, where the trained model can use the sentiment score of the provided text, the word count, and intended country of interest to have each decision node vote on the most likely output candidate. This is then all combined to determine the country the provided article was most likely written from.

### Persona #2 PR Specialist:

The second user persona (PR specialist) redirects to a page with two buttons: a view country sentiment score page and a view article page. The country sentiment score page allows the user to input some article text, the country the article was written from, and the country the article was written about. The user can then click on a calculate sentiment button to dynamically trigger this information being sent to the Multi-Linear Regression Model. When the model receives the user-provided features of article text, the country the article was written from, and the article’s intended subject country, this data is processed. During this cleaning and preparation, the safety score of the intended subject country and word count of the provided article are used, along with a one-hot encoding of the country being written from, to allow for a robust input vector that accounts for various features. From here, the dot product of this input vector is taken with the weight vector for a complex y = mx+b prediction of the sentiment score. This score is then returned to the user along with an additional sentiment score, calculated using the TextBlob sentiment library, which provides the user the ability to compare and contrast these two scores.

The view article page is implemented identically to the view article page on the foreign policy advisors route. The user randomly views an article from the database, can like, share and move into the next article. 

### Persona #3 Traveler:

The third user persona (an unemployed traveler) redirects to a page with two buttons: a user preferences page and an article search page. The user preferences page allows the user to input their preferred travel timeline, the country they are traveling to, and the country they are traveling from. This page is very much POC because although the user preferences are updated in the filters table of the database, these preferences are not used in personalized article matching. We hope to implement this as a feature in the future. The article search page allows the user to enter keywords in the textbox and search for articles within the database. The page uses a GET route to access articles in the database. A user can search for articles that were initialized in the database as well as articles that have been added manually by users.

### Persona #4 System Admin:

The fourth user persona (a system administrator) redirects to a page with two buttons: a model 1 maintenance page and a model 2 maintenance page. The model 1 maintenance page allows the user to train the linear regression model, and the model 2 maintenance page allows the user to train the random forest classifier. When a user clicks the “Train Multiple Linear Regression Model” button, they will be redirected to another page where they can then press a button that will formally train the model on the currently existing data in the initial article database. Behind the scenes, the model will pull the current training data, perform the necessary data cleaning, and compute the weight vector through the infamous $(X^TX)^{-1}X^Ty$ calculation that determines the weight coefficients. This weight vector will be returned to the user so that they can see exactly how the weights of the sentiment score for their input are calculated. When a user clicks the “Train Random Forest Classifier Model” button on the Model Admin Page, they trigger a query to the articles database that allows for various features of the training data to be pulled. For each article, this includes the content, its sentiment, the country it was written in, and the country the article was written about. Along with the word count, the RFC is trained on this cleaned data where the first few elements of the input training values and output training values are returned for users to see.

### Diplomatic Data Schema:

This diagram visualizes all the tables within our Diplomatic Data schema (DDL)

<img src="https://i.imgur.com/L0yPMPs.png" class="center"/>

### Frontend Architecture Connectivity Diagram

This diagram visualizes the connections between all frontend pages in our web-app.

<img src="https://i.imgur.com/SREB2qr.png" class="center"/>

