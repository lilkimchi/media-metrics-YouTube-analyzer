#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import pandas as pd

file = ('artede.json')
data = None
with open(file, 'r') as f:
    data = json.load(f)
    
channel_id, stats = data.popitem()  


# In[3]:


print(channel_id)


# In[4]:


channel_stats = stats['channel_statistics']
video_stats = stats['video_data']


# In[5]:


print('views', channel_stats['viewCount'])
print('subscriber', channel_stats['subscriberCount'])
print('videos', channel_stats['videoCount'])


# In[6]:


sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]['viewCount']), reverse=True)
stats = []
for vid in sorted_vids:
    video_id = vid[0]
    title = vid[1]['title']
    views = int(vid[1]['viewCount'])
    likes = int(vid[1]['likeCount'])
    dislikes = int(vid[1]['dislikeCount'])
    comments = int(vid[1]['commentCount'])
    stats.append([title, views, likes, dislikes, comments])


# In[7]:


df = pd.DataFrame(stats, columns = ['title', 'views', 'likes', 'dislikes', 'comments'])
df.head()


# In[8]:


df.to_csv('youtube_analysis_de.csv', index=False)


# ## locate title with the most comments
# 

# In[ ]:


df.sort_values(by=['comments'], ascending=False)


# ## locate top 10 titles with the most views
# 

# In[9]:


df.sort_values(by=['views'], ascending=False)


# In[10]:


ax = df.plot.bar(x='title', y = 'views', figsize=(12,8), fontsize=14)


# In[11]:


top10 = df.head(10)
ax = top10.plot.bar(x='title', y = 'views', figsize=(12,8), fontsize=14)


# In[ ]:


df.iloc[df['comments'].idxmax()]


# In[ ]:


df.loc[df['comments'].idxmax()]


# In[ ]:


bottom10 = df.tail(10)
ax = top10.plot.bar(x='title', y = 'views', figsize=(12,8), fontsize=14)


# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


top_comments= top10['comments'].max()
print('top comments: ', top_comments)


# In[ ]:


df


# In[ ]:


#highest number of comments


# In[ ]:


# list title(row) with the highest number of comments


# In[ ]:


df['comments'].sort_values(ascending=False)
df['comments']


# In[ ]:


# title with most comments
df['comments'].argmax()
df.loc[df['comments'].idxmax()]


# In[ ]:


# locate videoId with most comments


# ## Load JSON file into dataframe

# In[ ]:


import json 

with open('artede.json') as f:
  data = json.load(f)

print(data)


# In[ ]:


yt_df = pd.DataFrame.from_dict(data, orient="columns")


# In[ ]:


yt_df.head(10)


# In[ ]:


ytdf = pd.json_normalize(ytdf['video_data'])


# In[ ]:




