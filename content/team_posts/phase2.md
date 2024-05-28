---
title: "Phase 2!"
date: 2024-05-28
draft: false
description: "Group post for phase 2"
slug: "phase_2_post"
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
  - "milo_margolis"
  - "sydney_schulz"
  - "paolo_lanaro"
showAuthorsBadges : false
---
# Phase 2!

For this phase of the project, we found ourselves in an exciting spot for setup. This allowed us to figure out how to best increment progress on our sentiment analysis of different global perceptions of countries.

### Updates to Phase I

One large change that we made since phase I was that we decided to use a different API in order to obtain our data. While we initially planned to focus on the New York Times API and use an additional news API to support it, we now are focusing solely on a new API, the World News API. We decided to transition to this API because the sentiment analysis for the article is included as one of the features. This means that we did not have to do the sentiment analysis ourselves and instead could focus on effective data cleaning, analysis, and ML models.

### Data Visualization and Contextualization

For the first visualization we wanted to have a general understanding of what the semantic scores were for each country. We created a bar plot that showed the median sentiment for each country and also shows what the maximum and minimum values were. Belgium had the highest sentiment score and the United States had the lowest sentiment score. Interestingly, Belgium had the lowest number of articles written about them while the United States had the most. It will be interesting to see if this trend continues when we collect data about more countries.

For the second visualization, we wanted to explore the connections between the country that the article was published in and the queried country. The heat map shows not only that most of the articles came from the US. One interesting insight was that the US writes almost the same amount about itself as it does about China. In the future, it may be interesting to see how the sentiment score could be affected by what country is writing about it. 

For the third and fourth visualizations, we wanted to how sentiment scores changed over time. The third visualization shows the general trend while the fourth visualization breaks up the change over time by country. The third visualization shows that there may be a slight upward trend in the overall sentiment of articles written over the past few years. Reflections in world politics are also reflected in the line chart such as a decrease in sentiment in articles about Russia after the war in Ukraine started and the sentiment increased after the US 2020 elections.

### Preliminary ML Models and Data Cleaning

For this phase, we used the World News API (WNA). After establishing an initial connection, there was lots of cleaning and structuring necessary. This required extensive filtering and organizing to ensure easy access to each feature of different articles. Using the WNA, we were able to represent different articles by the date they were published, the country of interest and what was searched for, the country of origin for the article, the text of the article, and, using an additional API to obtain the safety score associated with living in each country.

After this, we implemented a very simple linear regression algorithm that utilizes the power of linear algebra to represent difficult to capture relationships in a linear format. This was done through a few functions. After doing a few of these basic calculations, we came to the conclusion that there is ample room for improvement in this model as the relationships we predicted to be relatively related were in fact not very related at all. 

This begs the question for the approach that will be taken for future steps and iterations of these predictive models. After seeing the poor correlations, we’ve decided that it will be necessary to refine and edit the features required to the answers to each driving question. Furthermore, we plan on incorporating additional countries to the dataset and beginning the implementation of a linear perceptron or some other classification algorithm to assist in an overarching global sentiment score of a user’s indicated country.

Please check the assets folder of our repository for more information regarding this data extraction, cleaning, and linear regression.

### **Database Design Update**

On the CS3200 end, we utilized our user personas to create detailed ER diagrams focused on user entities and their relationships. We developed three local ER diagrams, each representing different user interactions within the app. By combining these local diagrams, we created a comprehensive global ER diagram that includes all three user entities and the relevant entities for user data collection and news source data collection. We also drafted an SQL DDL for all relevant tables and created a mockup of a wireframe proof of concept.

### SQL DDL
https://github.com/PaoloLanaro/phase2_sql-ddl/blob/sql-ddl/AppSchema.sql

### The following are the three localized ER Diagrams:

<img src="https://i.imgur.com/73AsKPn.png" class="center"/>
<img src="https://i.imgur.com/dTQVP7w.png" class="center"/>
<img src="https://i.imgur.com/ThogIut.png" class="center"/>

### This is the global data model:

<img src="https://i.imgur.com/EOvQHQg.png" class="center"/>

### This is the proof of concept wireframe for our application:

### Wireframe POC
<img src="https://i.imgur.com/iFdaiJR.png" class="center"/>
