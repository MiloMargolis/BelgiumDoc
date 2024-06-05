---
title: "Individual Contributions 3"
date: 2024-06-5
draft: false
description: "Final contributions to the third phase."
slug: "fourth"   # if you use, needs to be different for every post
tags: ["authors", "config", "docs"]
authors:
  - "nia_quinn"
showAuthorsBadges : true
---

# Fancy seeing you here! Welcome back.

For this phase of the project I found myself working in collaboration with my teammates on various parts of the Diplomatic Data implementation. Between various attempts at extracting additional data, to implementing the linear perceptron, to working on the StreamLit integration, I had the opportunity to contribute to these facets. 

To begin one of the main things I focused on was retrieving more data from the same World News API to create a more robust data set for our model to be trained on. The same error as last time, using too many requests for one account, didn’t allow us to access the data that we needed to. 

After many futile attempts, I transitioned to checking the validity of the initial linear regression. This included calculating the $R^2$ value, which with a value of 0.0009931428505206563, left lots to be desired. From this, Sydney and I concluded that we would take different approaches to the implementation of the ML models. Sydney worked to integrate a Random Forest Decision Tree with our collected data and I implemented a simple Linear Perceptron from the base model we did in class. Using the base linear algebra functions, I trained a model to be able to predict a country’s sentiment score as being either +/- 1 based on its safety score. 

This .ipynb implementation was translated into a .py file found as diplomatic-data\api\backend\ml_models\Linear_Perceptron.py. From here, I broke up each component to functions like ‘predict’.

From here, I assisted Milo with the integration of the datasets and weight vectors into the data structures that he and Paolo had written. This allowed me to see the backend component of the app and helped me understand how each part interacted. Together, we connected a ‘GET’ route from the StreamLit UI that allowed a user to specify their desired country of interest, from which the route connecting through the REST API would make a request back to the ‘predict’ function in the Linear_Perceptron.py file. 

After figuring out how to make these components interact properly, we all collaborated on the Team Blog and individual blog posts to create the report you’re reading now!