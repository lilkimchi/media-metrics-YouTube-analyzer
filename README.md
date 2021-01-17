# Sentiment Analysis on YouTube Comments
<img src='visualizations/Title.png' width=700>

## Description
Create a business intelligence dashboard with multi-channel metrics to compare KPIs. Analyze YouTube comments using sentiment analysis

## Inspiration
This was inspired by a project I was working on for ARTE as an analyst and consultant. I wanted to automate tasks to tidy data, unify it into one stakeholder reporting tool, and use data sources available to analyze content performance. I extracted channel and video statistics with the help of the YT Data API and performed sentiment analysis to find how viewers felt about videos and content.

## Features
1. Compare channel KPIs such as video count, views, duration, un-/clickable link count and video tags and show visualizations<br/>
2. Analyse video comments and sentiments 

## Installation and Requirements
You need the YouTube API key for this (I don't include mine)<br/>
https://developers.google.com/youtube/v3/getting-started <br/>
https://console.developers.google.com/

## Viewer Metrics Dashboard
<img src='visualizations/TV_metrics.png' width=700>

## Sentiment Analysis on YouTube Comments
Bigram to count the frequencies of 2 consecutive words in comments
<img src='visualizations/Bigram_Frequency.png' width=700>

Weighted words in video comments
<img src='visualizations/Sentiment_score.png' width=500>

## Tech Stack
Python, pandas, numpy, sklearn, nltk, vadersentiment,TabPy, Tableau Public
