---
title: "Blog Post #3"
date: 2024-06-05
draft: false
description: "Third post!"
# slug: "first"
tags: ["authors", "config", "docs"]:
authors:
  - "milo_margolis"
showAuthorsBadges : false
---

Discussion/description of individual contributions to Phase III results
### Overview
This week, I dedicated nearly half of my time to working on the initial structure for the front end pages. I made 4 pages that were either related or semi-related to the user personas. Each persona has their own button option on the homepage (Anton, Katerina, and Monika). Anton’s page directs the user to a new page where they can view their personal profile information, such as recently viewed articles, liked articles, saved articles, and shared articles. The page also has a section dedicated to trending articles and trending sentiments based on user in-app activity. Katerina’s page contains two links, the first one allows the user to select a country from the country API list and view the given country’s sentiment score. This sentiment score button is connected to the REST API with a “GET” route which makes a call to the data science team’s ML model. The second link on Katerina’s page allows the user to view an article in depth (placeholder article for now), with a title, published date, sentiment score, source, and description. Monika’s page contains a link that allows the user to configure their preferences based on their preferred timeline, country of interest, and article provider of interest. Finally, I created the main page which provides a basic overview of the purpose of the app with a description of our project.

Moving onto the REST API design, I built a GET route which connects to the data science team’s ML model. The goal of this route is to display a country’s sentiment score based off the user’s input. I also worked with Paolo to design the remaining API routes using GET, PUT, POST, and DELETE. This week was a ton of new learning for me, and I’m excited to continue learning about REST API’s, databases,  and Streamlit frontend designs. 


### Personal Work Addendum for Week #3
- Created 8 front end pages in Streamlit (individual)
- Created a REST API GET route for the ML model (individual)
- Debugged the ML model route (teamwork)
- Created several other routes for various forms of in-app activity/usage (teamwork) 
