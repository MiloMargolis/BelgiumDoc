---
title: "Individual Contributions 2"
date: 2024-05-28
draft: false
description: "Final contributions to the second phase."
slug: "third"   # if you use, needs to be different for every post
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
showAuthorsBadges : true
---

# Happy to have you again, here's what I've been working on.

For this phase of the project, I collaborated with my teammates to create and implement a more substantial form of our project. Below I will elaborate on what I was able to contribute to this phase of the project.

Before beginning any sort of ML model implementation, I made an intial API request to a few different sources. These included the [Associated Press Media API](https://developer.ap.org/ap-media-api/) and the [World News API](https://worldnewsapi.com/). After an initial pull from the AP’s API, I realized that there was much left to be desired as the API requires access to a full, paid account with the AP so I was able to have access to images and to brief headlines. 

From there, I transitioned to exploring the WNA. After using their well documented website, I found that this API pulled articles from hundreds of international sources and allowed me to essentially pool of of this data through one simple API call. In addition to the article text, headlines, and all sorts of other information, a sentiment score in the range of [-1, 1] was attached to each article. After some rather tedious data cleaning and merging another API’s information with Sydney, we were able to add an additional data point quantifying a country’s safety score as another metric for analysis. An issue that we ran into while performing these API calls was the amount of time that it takes to actually get all of the data! Even for just 5 countries it took around 10 minutes of waiting for all of the proper information.

After all of this data scraping and cleaning, I implemented a rather quick and dirty linear regression. Using information from Sydney’s EDA, we used Russia as a test country to see how using a country’s sentiment score could predict it’s safety score. This proved to be a rather weak relationship, at least for Russia, and we plan to flesh these features out more in the future.

In this phase I learned that we likely will need to implement more complex forms of ML models to assist in identifying relationships evident in the data and that will be more useful to our users. One of these models will likely be a linear perceptron that will help users figure out if a country is safe to go to!