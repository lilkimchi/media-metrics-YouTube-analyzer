# Sentiment Analysis on YouTube Comments

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

## YouTube Statistics and Sentiment Analysis
<img src='visualizations/Sentiment.score.png' width=700>

## Tech Stack
Python, pandas, numpy, sklearn, nltk, vadersentiment,TabPy, Tableau (Community edition)
