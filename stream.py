import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import json

# TITLE AND DESCRIPTION
st.title("YouTube Trending Video Analysis")
st.write("Explore trending YouTube videos using category and date filters."
         "Analyze views, likes, engagement, popular tags, and upload patterns.")  
st.info("Use the filters in the sidebar to explore the dataset.") 
st.divider()

# CREATE A SIDEBAR
st.sidebar.title("Filters")
st.sidebar.write("Use the filter below to explore trending videos by category.")

# LOAD CSV
df = pd.read_csv("CAvideos.csv")

# LOAD JSON
with open("CA_category_id.json","r")as file:
    category_data = json.load(file)

category_dict = {}
for item in category_data["items"]:
    category_dict[item["id"]] = item["snippet"]["title"]

category_dict["29"] = "Nonprofits & Activism"    
df["category_name"] = df["category_id"].astype(str).map(category_dict)  

# ADD ENGAGEMENT RATE
df['engagement_rate'] = ((df['likes'] + df['comment_count']) / df['views']) *100

# ADD LIKE RATE
df['like_rate'] = (df['likes'] / df['views']) *100

# PREPARE UPLOAD TIME DATA
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_day'] = df['publish_time'].dt.day_name()
df['publish_hour'] = df['publish_time'].dt.hour 

# DATE FILTER TO ADD IN THE SIDEBAR
start_date = st.sidebar.date_input("Start Date",df["publish_time"].min().date())
end_date = st.sidebar.date_input("End Date",df["publish_time"].max().date())

# SET THE DAY ORDER
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
df['publish_day'] = pd.Categorical(
    df['publish_day'],
    categories=day_order,
    ordered=True
)

#st.write("Dataset Preview") #Display text
#st.dataframe(df.head())  #Display the data in an interactive table

# CATEGORY FILTER
# SELECTBOX CREATE A DROP DOWN LIST
categories = df["category_name"].dropna().unique()  #To get the catgories name
selected_category = st.sidebar.selectbox( "Select a Category", categories)  #selectbox create a drop down list

# It Show Only Selected Category
filtered_df = df[(df["category_name"] == selected_category) &
                 (df["publish_time"].dt.date >= start_date) &
                 (df["publish_time"].dt.date <= end_date)]

st.write("Videos in Selected Category")
st.dataframe(filtered_df)
st.divider()

# DASHBOARD TABS
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Overview",
    "📈 Performance Analysis",
    "🏷️ Category Analysis",
    "🔥 Trending Videos",
    "⏰ Upload Time",
    "📋 Data"
])

with tab1:
# DASHBOARD METRICS
    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    #Created a Column in the Dashboard
    col1.metric("Total Videos", len(filtered_df))
    col2.metric("Total Views", f"{filtered_df['views'].sum():,}")
    col3.metric("Total Likes", f"{filtered_df['likes'].sum():,}")
    col4.metric("Average Views", f"{filtered_df['views'].mean():,.0f}")
    st.divider()

# ADD THE VIEWS VS LIKES SCATTER PLOT
    st.subheader("Views vs Likes")
    st.scatter_chart(
       filtered_df,
       x="views",
       y="likes"
    )
    st.divider()

# TRENDING VIDEOS
with tab4:
# ADD THE TOP VIDEOS
    st.subheader("Top Videos by Views")
    top_videos = filtered_df.sort_values( "views", ascending=False).head(10)
    st.dataframe(top_videos[["title","views","likes","comment_count"]])
    st.bar_chart(top_videos.set_index("title")["views"])
    st.divider()

    # TO FIND ENGAGEMENT RATE
    st.subheader("Top Engaging Videos")
    top_engagement = filtered_df.sort_values("engagement_rate", ascending=False).head(10)
    st.dataframe(top_engagement[ ["title","views","likes","comment_count","engagement_rate"]]) 
    st.divider()

    #TO FIND LIKE RATE/TOP VIDEOS BY LIKE RATE
    st.subheader("Top Videos by Like Rate")
    top_like_rate = filtered_df.sort_values("like_rate", ascending=False).head(10)
    st.dataframe(top_like_rate[["title","views","likes","like_rate"]]) 
    st.bar_chart(top_like_rate.set_index("title")["like_rate"])
    st.divider()

# PERFORMANCE ANALYSIS
with tab2:

    # CORRELATION ANALYSIS
    st.subheader("Correlation Analysis")

    correlation_data = filtered_df[
        ["views", "likes", "comment_count", "engagement_rate", "like_rate"]
    ]
    correlation_matrix = correlation_data.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f"
    )
    plt.title("Correlation Between Video Metrics")
    st.pyplot(plt)
    st.write(
        "Correlation values close to 1 indicate a strong positive relationship, "
        "while values close to -1 indicate a strong negative relationship."
    )
    st.divider()

    # TIME-SERIES ANALYSIS
    st.subheader("Trending Videos Over Time")
    monthly_videos = (
        filtered_df
        .set_index("publish_time")
        .resample("ME")
        .size()
    )

    st.line_chart(monthly_videos)
    st.write(
        "This chart shows how the number of trending videos changed over time "
        "for the selected category and date range."
    )
    st.divider()

    # MONTHLY PERFORMANCE ANALYSIS
    st.subheader("Monthly Average Performance")

    monthly_performance = (
        filtered_df
        .set_index("publish_time")
        .resample("ME")
        .agg(
            Average_Views=("views", "mean"),
            Average_Likes=("likes", "mean")
        )
    )

    st.line_chart(
        monthly_performance[
            ["Average_Views", "Average_Likes"]
        ]
    )

    st.write(
        "This chart shows how the average views and likes of "
        "trending videos changed over time."
    )
    st.divider()

# CATEGORY ANALYSIS
with tab3:

    # TO COUNT THE VIDEO CATEGORY-WISE
    st.subheader("Videos by Category")
    category_count = df["category_name"].value_counts()
    st.bar_chart(category_count)
    st.divider()

    # CATEGORY PERFORMANCE ANALYSIS
    st.subheader("Category Performance")

    date_filtered_df = df[
        (df["publish_time"].dt.date >= start_date) &
        (df["publish_time"].dt.date <= end_date)
    ]

    category_performance = (
        date_filtered_df
        .groupby("category_name")
        .agg(
            Average_Views=("views", "mean"),
            Average_Likes=("likes", "mean"),
            Average_Comments=("comment_count", "mean"),
            Average_Engagement=("engagement_rate", "mean")
        )
        .sort_values("Average_Views", ascending=False)
    )

    st.dataframe(
        category_performance.style.format({
            "Average_Views": "{:,.0f}",
            "Average_Likes": "{:,.0f}",
            "Average_Comments": "{:,.0f}",
            "Average_Engagement": "{:.2f}%"
        })
    )

    st.bar_chart(category_performance["Average_Views"])
    st.divider()

    # DATA SCIENCE INSIGHTS
    st.subheader("Key Insights")

    highest_views_category = category_performance[
        "Average_Views"
    ].idxmax()

    highest_engagement_category = category_performance[
        "Average_Engagement"
    ].idxmax()

    most_viewed_video = filtered_df.loc[
        filtered_df["views"].idxmax(), "title"
    ]

    most_engaging_video = filtered_df.loc[
        filtered_df["engagement_rate"].idxmax(), "title"
    ]

    st.write(
        f"📌 **Highest Average Views Category:** "
        f"{highest_views_category}"
    )

    st.write(
        f"📌 **Highest Average Engagement Category:** "
        f"{highest_engagement_category}"
    )

    st.write(
        f"🔥 **Most Viewed Video in Selected Category:** "
        f"{most_viewed_video}"
    )

    st.write(
        f"💡 **Most Engaging Video in Selected Category:** "
        f"{most_engaging_video}"
    )
    st.divider()

# DATA
with tab6:

    # DOWNLOAD CSV BUTTON
    st.subheader("Download Dataset")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="youtube_trending_videos.csv",
        mime="text/csv"
    )
    st.divider()

    # TRENDING VIDEO TAGS
    st.subheader("Trending Video Tags")
    # Get Tags From The Selected Category
    tags = filtered_df["tags"].dropna().astype(str)
    # Remove Empty And Invalid Tag Values
    tags = tags[
        (tags != "[none]") &
        (tags != "[None]") &
        (tags.str.strip() != "")
    ]

    if not tags.empty:
        # Replace | between tags with spaces
        text = " ".join(
            tags.str.replace("|", " ", regex=False)
        )

        if text.strip():

            # CREATE WORDCLOUD
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color="white"
            ).generate(text)

            # DISPLAY WORDCLOUD
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            ax.set_title("Most Common Trending Video Tags")
            st.pyplot(fig)
            plt.close(fig)

        else:
            st.warning("No usable tags found for the selected category.")

    else:
        st.warning("No tags are available for the selected category.")

    st.divider()


# UPLOAD TIME ANALYSIS
with tab5:

    # UPLOAD TIME HEATMAP
    heatmap_data = pd.crosstab(
        filtered_df["publish_day"],
        filtered_df["publish_hour"]
    )

    st.subheader("Upload Time Heatmap")

    plt.figure(figsize=(15, 7))
    sns.heatmap(heatmap_data)
    plt.title("YouTube Video Upload Time")
    plt.xlabel("Hour of Day")
    plt.ylabel("Day of Week")
    st.pyplot(plt)

    st.divider()

    # UPLOAD TIME INSIGHTS
    st.subheader("Upload Time Insights")

    most_common_day = (
        filtered_df["publish_day"].value_counts().idxmax()
    )

    most_common_hour = (
        filtered_df["publish_hour"].value_counts().idxmax()
    )

    day_hour_counts = filtered_df.groupby(
        ["publish_day", "publish_hour"]
    ).size()

    most_common_day_hour = day_hour_counts.idxmax()
    highest_upload_count = day_hour_counts.max()

    st.write(
        f"📅 **Most Common Upload Day:** {most_common_day}"
    )

    st.write(
        f"🕐 **Most Common Upload Hour:** {most_common_hour}:00"
    )

    st.write(
        f"🔥 **Most Common Day & Hour:** "
        f"{most_common_day_hour[0]} at "
        f"{most_common_day_hour[1]}:00 "
        f"({highest_upload_count} videos)"
    )
    st.divider()

# TO ADD FOOTER
st.markdown("<p style='text-align:center;'><b>Youtube Trending Video Analysis | Built With Python, Pandas and Streamlit</b></p>",unsafe_allow_html=True)
