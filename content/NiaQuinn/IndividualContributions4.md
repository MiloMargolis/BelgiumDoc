---
title: "Individual Blog Post 4"
date: 2024-06-10
draft: false
description: "Rushed concluded thoughts after a lot of python."
slug: "fourth"   # if you use, needs to be different for every post
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
showAuthorsBadges : false
---
# And for the last time, welcome back! Glad to see you again.

This phase of the project has proven to be the most challenging and tedious by far. As we transitioned to implementing both of the ML models into the app, integrated the models with various features of streamlit for easy user access, and further understood the complexity of implantation with local databases, this phase of the project was by far the most tricky, but also the most rewarding. 

My main area of focus for this portion of the project was implementing both the Multiple Linear Regression model and the Random Forest Classification model into the app. This required tedious cleaning and accessing of data from SQL queries and then breaking apart models to more readily segmented features that allowed for users to train and then predict output in the main app. 

As an individual, I implemented the Multiple Linear Regression model in the app while assisting and augmenting the development of the routes that retrieve this data from the locally saved databases. After Sydney did the initial conversion from the Juptyer Notebook to the app, I refined the implementation and made sure that there was well documented and efficient code that would make the integration as easy as possible in the front-end.

To assist Paolo and Milo with some of their work, I lightened their load by writing a few of the ML model routes that would take in user input, query the SQL databases, and then send that information back to the model. We all together worked to improve the general quality of the app!

Here's my resume excerpt:
Diplomatic Data | Python, StreamLit, Docker, NumPy | May – June 2024
• Researched and implemented Multiple Linear Regression model using NumPy using features of articles to predict
sentiment
• Integrated MLR model with StreamLit based web application via Flask API routes
• Harness power of StreamLit UI features to create user friendly application