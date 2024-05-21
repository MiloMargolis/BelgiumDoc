---
title: "Our initial thoughts"
date: 2024-05-20
draft: false
description: "Our initial brainstorming process"
slug: "phase1post"
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
  - "milo_margolis"
  - "sydney_schulz"
  - "paolo_lanaro"
showAuthorsBadges : false
---

# Overview (Phase 1 Deliverable below)

#### We started out this "checkpoint" by thinking about apps that we would be interested in, especially some app idea that would be useful during our studies abroad.

### Initial Thoughts

The app idea we started to think about was an app that resembled 'Google Maps' or 'Yelp' in terms of getting good food recommendations for travellers. The very obvious problem with this idea is that both of those apps already exist. Taking this idea and combining it with that of small businesses, we thought about making an app that would predict the success of a restaurant in a city or general area. This app would combine Google Maps (Yelp, etc.) data of nearby restaurants including reviews, comments (with sentiment analysis), and other data points for the prediction. As we worked with this idea more (and talked to both Dr. Fontenot, and Dr. Gerber), we realized that this still wasn't answering the main project question, "'change someone's world'". Sure, we were changing the world of some small business owners with their future decisions, but it didn't relate to international politics at large. This was the start to our second phase, the slightly delirious brainstorming eve of the 21st.

### Shifting Topics

We began thinking about globalizing the very general concept of "food" (again, after the insight of Dr. Fontenot and Dr. Gerber). Food insecurity and scarcity was a natural choice as it affect people all over the world every day. As we started discussing this topic and researching databanks and API's we got led into the topics of education and lack thereof. This eventually led us to what we'll be planning our project around, the general politics and sentiment towards people of some origin when they go travelling.

# Phase 1 Deliverable:

## Project Description 
For our project, we plan on creating an application that can indicate the general global perception of a certain country based on how the country is perceived through news articles. By determining the sentiment of articles that are related to a nation, we can determine how news sources perceive these nations. Many journalists and news organizations have biases towards specific nations and being able to quantify these biases will allow for further understanding about how these biases affect global perceptions. We hope to be able to implement sentiment analysis and linear regression to help gather insights for a variety of different stakeholders. We foresee these insights will allow for benefits on an international/local government scale and on a smaller scale with individual citizens. 
  
On a smaller scale, if individuals understand how their nation is perceived, they will have a better idea of what to expect when traveling. When interacting with individuals from other nations, they will have a general understanding about attitudes and stereotypes and may be able to have more success in informing others about their home nation.

This understanding of perception is also incredibly relevant on a larger governmental scale both locally and broader. Politicians and nation leaders must have an understanding of the preconceived biases and impressions that other nations have on them to pursue effective diplomacy and create a successful impression when talking to the media.

We hope to use the article search API from the NYT that allows us to search and grab articles by keyword. The information that we get is the title and a short excerpt from the article that we will do our analysis on. In addition to this, we hope to be able to implement an API for a separate news source so that the users will be able to compare how different news sources with different leanings perceive their nation. 

## User Personas
- ### Persona #1: Anton Müller, the Policy Maker

  - **Overview:**  
    - Age: 53
    - Occupation: Foreign Policy Advisor at the EU
    - Location: Berlin, Germany

  - **Background:**
    - Education: MS in international politics from London School of Economics
    - Experience: 15 years working in international relations and foreign policy 
    - Role Description: Advising EU policymakers on foreign policy decisions by analyzing geopolitical data and trends

  - **Goals and Motivations:**
    - Supporting the development of foreign policies within the EU using data-driven insights
    - Enhancing the EU’s diplomatic relations by identifying areas of political frustration through social media
    - Wants to make a tactical impact on the shaping of foreign policies based on general public sentiment within various regions

  - **Challenges:**
    - Struggles to process and analyze the massive amounts of political information through news sources and social media
    - Needs to stay updated on the rapidly changing geopolitical sentiments  
    - Feels that even on individual news platforms, the degree of information that is published each day is more than he can keep up with, and frustrations across various political issues blend together

  - **General use case:**
    - Logins into the mobile app
    - Sets a filter to the location, timeframe, and subjects
    - Reviews sentiment analysis data on the news sources within that time frame, examining the trends and significant changes in correspondence to recent events
    - Utilizes these insights to create reports highlighting these key sentiment shifts and presents his findings to the senior policymakers at the EU

  - **Anton’s User Stories:**
    - As a foreign policy advisor I want to identify areas of political frustration through news sources so I can provide accurate and insightful insights to EU policy makers. 
    - As a professional with a challenging information overload, I want to be able to filter and prioritize the rapidly changing geopolitical sentiments in a streamlined and digestible manner
    - As a father I want to be able to more effectively explain how certain events affect geopolitical sentiments with examples and stories so that my children can understand 


- ### Persona #2: Katerina Stepanov, the Corporate Businesswoman
  - **Overview:**
    - Age: 37
    - Occupation: PR Specialist at Gazprom Oil 
    - Location: Moscow, Russia

  - **Background:**
    - Education: BS in Communications from St. Petersburg Polytechnic University
    - Experience: 5 years post-grad at Ventra Go for media relations, 10 years at Gazprom
    - Role Description: Handles perception of association with Russia to expand and welcome global clientele

  - **Goals and Motivations:**
    - Further the reach of Gazprom’s clientele by expanding the global reach of their engagement
    - Mitigate negative media stigma surrounding Russian behavior, specifically regarding economic aggression
    - Use easily digestible data and visuals to assist briefings about perceptions with senior communications experts at Gazprom

  - **Challenges:**
    - Effectively conveying information to senior board members regarding public perception
    - Negating and disassociating from negative Russian stigma
    - Geopolitical competition with the US and Saudi Arabia
    - Maintaining professional relationships amidst negative views of the Russian government by many major world partners such as EU and US

  - **General use case:**
    - Creates an account with the app
    - Filters through the locations and provides an optional timeframe, saving this filter if she does so please
    - View and interact with the sentiment analysis, results of linear regression, visual outputs, and other forms of results
    - Reframe strategy for future press releases in response to constantly changing global perceptions
    - Understand how certain markets may be viewed less negatively and report to sales team as a potential client

  - **Katerina’s User Stories:**
    - As a PR specialist, I want to understand the global perception of the country my company is in so that I can combat any negative views about Russia.
    - As a member of the corporate workforce, I want to have fast access to easily digestible data and information so that I can improve my ability to increase productivity.
    - As a member of a business, I want to capitalize on information about the perception of competitors so that I can strategize tactics that would increase marketability and sales.


- ### Persona #3: Monika José, the Traveler
  - **Overview:**
    - Age: 18
    - Occupation: Unemployed
    - Location: Grew up in Texas

  - **Background:**
    - Education: High school
    - Experience: General neighborhood work (raking leaves, cutting grass). Part time cashier from 17-18
    - Role Description: N/A currently unemployed, taking a gap year before university

  - **Goals and Motivations:**
    - Wants to travel the world and experience different cultures during her gap year
    - Stay safe and be well-prepared by understanding the perception of Americans and America in general in various countries

  - **Challenges:**
    - She has never traveled outside the country.
    - Monika wants to feel welcomed during her travels.
    - Needs reliable, easily accessible information to make quick travel decisions

  - **General use case:**
    - Creates an account on the app
    - Sets filters for specific countries or regions she plans to visit
    - Reviews perceptions and trends for the chosen locations to understand the general attitude towards Americans
    - Uses the insights to plan her travel itinerary, choosing destinations where Americans are perceived positively

  - **Monika’s User Stories:**
    - As a traveler, I want to understand the general perception of Americans in different countries so that I can plan my trips to places where I will feel welcomed and safe.
    - As a young and inexperienced traveler, I want to have access to easy-to-understand data about global perceptions so that I can quickly make informed decisions about my travel destinations.
    - As a user, I want to be able to filter and save preferences in the app so that I can easily access information about the countries I plan to visit.


## Major Questions
  - How are the semantic scores of the articles different for each region? Is the region or continent associated with the semantic score?
    - It is to be expected that many biases that exist about nations exist because of the region that they exist in. If users have an understanding about the sentiment of their nation in addition to the country themselves, they can have a stronger understanding about outside perspectives. 
  - Is the number of articles written about each country associated with the semantic scores of the articles?
    - The number of articles written about each country is expected to be drastically different. For example, France definitely has more articles written about it than Belarus. By identifying the relationships between the number of articles and the semantic score, users of the app can have a better understanding about the reliability of the score and what factors may have influenced it.
  - How do the semantic scores of a country's article change depending on the news source and the political leaning of the news source?
    - Different news sources obviously have different perspectives and biases towards countries so having more than one news source semantic score delivered will give a broader and more realistic perspective. In addition, by identifying the political leanings of a news source, it can provide a political context to the semantic score and can be an insightful resource to the users of the site.


## Potential Sources / APIs

- <a href="https://newsapi.org/docs/get-started">NewsApi</a>
- <a href="https://developer.nytimes.com/docs/archive-product/1/overview">NYT API</a>
- <a href="https://api.ap.org/media/v/docs/#t=Getting_Started_API.htm">AP</a>
