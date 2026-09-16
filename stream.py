import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import json

#Title and Description
st.title("YouTube Trending Video Analysis")
st.write("Explore trending YouTube videos using category and date filters."
         "Analyze views, likes, engagement, popular tags, and upload patterns.")  
st.info("Use the filters in the sidebar to explore the dataset.") 
st.divider()

#Create a sidebar
st.sidebar.title("Filters")
st.sidebar.write("Use the filter below to explore trending videos by category.")

#Load CSV
df = pd.read_csv("CAvideos.csv")
#Load json
with open("CA_category_id.json","r")as file:
    category_data = json.load(file)

category_dict = {}
for item in category_data["items"]:
    category_dict[item["id"]] = item["snippet"]["title"]

category_dict["29"] = "Nonprofits & Activism"    
df["category_name"] = df["category_id"].astype(str).map(category_dict)  

#Add engagement rate
df['engagement_rate'] = ((df['likes'] + df['comment_count']) / df['views']) *100

#Add like rate
df['like_rate'] = (df['likes'] / df['views']) *100

# Prepare Upload-time data
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_day'] = df['publish_time'].dt.day_name()
df['publish_hour'] = df['publish_time'].dt.hour 

#Date filter to add in the sidebar
start_date = st.sidebar.date_input("Start Date",df["publish_time"].min().date())
end_date = st.sidebar.date_input("End Date",df["publish_time"].max().date())

#Set the day order
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
df['publish_day'] = pd.Categorical(
    df['publish_day'],
    categories=day_order,
    ordered=True
)

#st.write("Dataset Preview") #Display text
#st.dataframe(df.head())  #Display the data in an interactive table

#Category filter
#selectbox create a drop down list
categories = df["category_name"].dropna().unique()  #To get the catgories name
selected_category = st.sidebar.selectbox( "Select a Category", categories)  #selectbox create a drop down list
#It show only selected category
filtered_df = df[(df["category_name"] == selected_category) &
                 (df["publish_time"].dt.date >= start_date) &
                 (df["publish_time"].dt.date <= end_date)]

st.write("Videos in Selected Category")
st.dataframe(filtered_df)
st.divider()

#Dashboard Metrics
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
#Created a column in the dashboard
col1.metric("Total Videos", len(filtered_df))
col2.metric("Total Views", f"{filtered_df['views'].sum():,}")
col3.metric("Total Likes", f"{filtered_df['likes'].sum():,}")
col4.metric("Average Views", f"{filtered_df['views'].mean():,.0f}")
st.divider()

#Add the views vs likes scatter plot
st.subheader("Views vs Likes")
st.scatter_chart(
    filtered_df,
    x="views",
    y="likes"
)
st.divider()

#Add the top videos
st.subheader("Top Videos by Views")
top_videos = filtered_df.sort_values( "views", ascending=False).head(10)
st.dataframe(top_videos[["title","views","likes","comment_count"]])
st.bar_chart(top_videos.set_index("title")["views"])
st.divider()

# To find Engagement rate
st.subheader("Top Engaging Videos")
top_engagement = filtered_df.sort_values("engagement_rate", ascending=False).head(10)
st.dataframe(top_engagement[ ["title","views","likes","comment_count","engagement_rate"]]) 
st.divider()

#To find like rate/top videos by like rate
st.subheader("Top Videos by Like Rate")
top_like_rate = filtered_df.sort_values("like_rate", ascending=False).head(10)
st.dataframe(top_like_rate[["title","views","likes","like_rate"]]) 
st.bar_chart(top_like_rate.set_index("title")["like_rate"])
st.divider()

#To count  the video category_wise
st.subheader("Videos by Category")
category_count = df["category_name"].value_counts()
st.bar_chart(category_count)
st.divider()

#Download CSV button
st.subheader("Download Dataset")
csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="youtube_trending_videos.csv",
    mime="text/csv"
)

#Create the worldcloud
st.subheader("Trending Video Tags")

tags = filtered_df['tags'].dropna().str.replace('|',' ', regex=False)
text = ' '.join(tags)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(text) 

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt) # to print in the streamlit dashboard
st.divider()

#upload and display heatmap of time
heatmap_data = pd.crosstab(  
   filtered_df['publish_day'],
   filtered_df['publish_hour']
) 

st.subheader("Upload Time Heatmap")
plt.figure(figsize=(15,7))
sns.heatmap(heatmap_data)
plt.title("Youtube Video Upload Time")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
st.pyplot(plt)


#To add Footer
st.divider()
st.markdown("<p style='text-align:center;'><b><Youtube Trending Video Analysis | Built With Python, Pandas and Streamlit</b></p>",unsafe_allow_html=True)
