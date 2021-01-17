<img src='visualizations/Title.png' width=700>

## Description
* A business intelligence dashboard using Tableau<br/> 
* A YouTube video metrics analyzer<br/>
  * Channel KPIs such as video count, views, duration, un-/clickable link count and video tags<br/>
* NLP sentiment analysis on YouTube comments<br/> 

## Introduction
This was inspired by a project I had previously worked on for a German-French media company as an analyst and consultant to help them make more data-informed decisions. This time, I wanted to take the data possibilities further with the power of Python and machine learning!

I used Python to automate tasks to tidy data, unify it into one stakeholder reporting tool, and to use the data sources available to analyze content performance. I extracted channel and video statistics with the help of the YouTube Data API and performed sentiment analysis to find how viewers felt about videos and content.

### Question
What makes a program a success?

To go beyond just the number of views, be a broadcast company that goes beyond broadcasting and listen to what your viewers are saying. Machine learning can add value to improve content and uncover viewer sentiment. Natural language processing reveals positive, negative, or neutral attributes.

## Installation and Requirements
You need the YouTube API key for this (I don't include mine)<br/>
https://developers.google.com/youtube/v3/getting-started <br/>
https://console.developers.google.com/

## Viewer Metrics Dashboard
<img src='visualizations/TV_metrics.png' width=700>
(dashboard data is omitted here to maintain confidentiality)

<img src='visualizations/views.gif' width=700>

## Sentiment Analysis on YouTube Comments
Bigram to count the frequencies of 2 consecutive words in comments<br/>
<img src='visualizations/Bigram_Frequency.png' width=500>

## Weighted words in video comments
<img src='visualizations/Sentiment_score.png' width=600>

### Tech Stack
Python, pandas, numpy, sklearn, nltk, vadersentiment,TabPy, Tableau 
