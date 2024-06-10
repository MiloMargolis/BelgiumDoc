---
title: "Blog Post 4"
date: 2024-06-10
draft: false
description: "Blog Post 4 on Phase 4"
slug: "fourth"   # if you use, needs to be different for every post
tags: ["authors", "config", "docs"]
authors:
  - "sydney_schulz"
showAuthorsBadges : false
---
# Blog Post #4

For the final phase of this project we performed the final push to have a functioning site that takes advantage of two brand new machine learning models. For the project my contributions consisted of building the machine learning models and rewriting syntax and functions to make them accessible in the app. We realized that the linear perceptron model created in phase 3 was ineffective so I decided to attempt to make a linear regression that was as effective as possible. Although this model may not be very accurate and may not be the best model type in general to make predictions about the data, I do think that it can give users insight on how the sentiment score of their country is effected. 

One feature that I found really interesting and applicable to what we have been learning in lectures was the source country. I build a Random Forest Classifier to attempt to classify where a piece of text may have come from. This model is also not very effective but it does do what it attempts to do. 

After creating the models, I did a rough implementation of what the functions would look like in the app. I then worked with Nia to improve the cohesiveness of the functions and ensure that it would successfully function in the app and collect the necessary information from the back end.

One thing that I enjoyed about working on this project was being able to apply things that I learned in class into a project that I can physically see run. 

One thing that I did not enjoy about working on this project was that I felt that the time restriction made it so that I could not really think critically about what I was doing and as a result I made errors and failed to identify problems that would have saved me a lot of time and resulted in more effective models in the long run.

## Resume

**Investigating Misinformation in Headlines -** Python                                                          June 2024

- Created a dynamic web application using streamlit, docker and python for sentiment analysis of global news
- Designed and implemented Linear Regression and Random Forest Classifier machine learning models to predict sentiment scores and country of origin for user inputed pieces of text