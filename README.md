# YouTube Trending Video Analysis

## 📌 Project Overview

The **YouTube Trending Video Analysis** project is a Data Science project built using Python. The purpose of this project is to explore YouTube trending videos and understand their performance in terms of views, likes, comments, engagement, categories, tags, and upload patterns.

The project includes a **Jupyter Notebook** for data analysis and an interactive **Streamlit dashboard** for exploring the results.

Users can select different categories and date ranges in the dashboard and analyze the data through metrics, tables, charts, a Word Cloud, and an Upload Time Heatmap.
---

## 🎯 Main Objectives
The main objectives of this project are:

* Analyze YouTube trending video data.
* Clean and prepare the dataset for analysis.
* Understand video performance using views, likes, and comments.
* Calculate engagement rate and like rate.
* Analyze the distribution of trending videos across categories.
* Identify top-performing and highly engaging videos.
* Analyze frequently used video tags.
* Explore video upload patterns by day and hour.
* Analyze relationships between different video metrics.
* Analyze trending videos over time.
* Compare monthly average video performance.
* Build an interactive dashboard using Streamlit.
* Present the analysis in a simple and user-friendly way.
---

## 🔎 What This Project Does
The project takes a YouTube trending video dataset and performs data cleaning, preprocessing, exploratory data analysis, feature creation, and visualization.

Additional analytical features are created, including:
* **Engagement Rate**
* **Like Rate**
* **Publish Day**
* **Publish Hour**

The project then uses the processed data to create visualizations and an interactive Streamlit dashboard.
---

## 🛠️ Technologies Used

* **Python** — Programming and data analysis
* **Pandas** — Data cleaning and data manipulation
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization and heatmaps
* **WordCloud** — Visualization of trending video tags
* **Streamlit** — Interactive dashboard
* **JSON** — YouTube category information
* **Jupyter Notebook** — Data analysis and exploration
---

## 📁 Project Structure

```text
YouTube-Trending-Video-Analysis/
│
├── stream.py
├── yt_analysis.ipynb
├── CAvideos.csv
├── CA_category_id.json
├── requirements.txt
├── README.md
└── .gitignore
```

### 📄 File Description

**`stream.py`**
The main Streamlit application. It contains the dashboard, filters, metrics, tables, charts, Word Cloud, Upload Time Heatmap, and dataset download functionality.

**`yt_analysis.ipynb`**
The Jupyter Notebook containing the Data Science analysis, including data cleaning, preprocessing, exploratory analysis, feature engineering, statistical analysis, and visualizations.

**`CAvideos.csv`**
The YouTube trending video dataset used for the analysis.

The dataset is large, so it may be kept locally and excluded from the GitHub repository using `.gitignore`.

**`CA_category_id.json`**
Contains YouTube category IDs and their corresponding category names.

**`requirements.txt`**
Contains the Python libraries required to run the project.

**`README.md`**
Project documentation containing information about the project, technologies, features, and setup instructions.

**`.gitignore`**
Specifies files and folders that should not be uploaded to GitHub, such as large datasets and Python virtual environments.
---

# 📊 Data Science Analysis
The Jupyter Notebook contains the following analysis:

### 🧹 1. Data Cleaning and Preparation

* Dataset inspection
* Shape and column analysis
* Missing-value checking
* Duplicate checking and removal
* Datetime conversion
* Category mapping
* Publish day extraction
* Publish hour extraction

### 📈 2. Descriptive Statistics
Basic statistical analysis is performed on:

* Views
* Likes
* Dislikes
* Comments
* Like Rate
* Engagement Rate

### 🏆 3. Top Trending Videos
The notebook identifies videos with high numbers of:

* Views
* Likes
* Comments
* Engagement Rate
* Like Rate

### 🏷️ 4. Category Analysis
The number of trending videos in different YouTube categories is analyzed and visualized.

### 📺 5. Channel Analysis
The notebook identifies channels with a high number of trending videos.

### 👍 6. Views vs Likes Analysis
A scatter plot is used to explore the relationship between video views and likes.

### 📊 7. Engagement Rate
The engagement rate is calculated using:

```text
Engagement Rate = ((Likes + Comments) / Views) × 100
```

### ❤️ 8. Like Rate
The like rate is calculated using:

```text
Like Rate = (Likes / Views) × 100
```

### 🔗 9. Correlation Analysis
A correlation matrix is used to examine relationships between:

* Views
* Likes
* Comments
* Engagement Rate
* Like Rate

### 📈 10. Time-Series Analysis
The project analyzes how the number of trending videos changes over time.

### 📅 11. Monthly Performance Analysis
Monthly average views and likes are analyzed to understand changes in video performance over time.

### ⏰ 12. Upload-Time Analysis
Video publishing patterns are analyzed using:

* Day of the week
* Hour of the day

### ☁️ 13. Trending Video Tags
A Word Cloud is created to visualize frequently appearing video tags.
---

# 🖥️ Streamlit Dashboard
The project includes an interactive Streamlit dashboard with six main sections.

### 📊 Overview
Contains:

* Total Videos
* Total Views
* Total Likes
* Average Views
* Views vs Likes scatter plot

### 📈 Performance Analysis
Contains:

* Correlation Analysis
* Trending Videos Over Time
* Monthly Average Performance

### 🏷️ Category Analysis
Contains:

* Videos by Category
* Category Performance
* Key Data Science Insights

### 🔥 Trending Videos
Contains:

* Top Videos by Views
* Top Engaging Videos
* Top Videos by Like Rate

### ⏰ Upload Time
Contains:

* Upload Time Heatmap
* Upload Time Insights

### 📋 Data
Contains:

* Filtered Dataset Download
* Trending Video Tags Word Cloud
---

# 🔎 Interactive Filters
The dashboard provides sidebar filters for:

### Category
Users can select a specific YouTube category.

### Date Range
Users can select a start date and end date.

The dashboard updates the displayed data and visualizations according to the selected filters.
---

# 📌 Key Metrics
The dashboard displays four important metrics:

* **Total Videos** — Number of videos after applying the selected filters.
* **Total Views** — Total views of the filtered videos.
* **Total Likes** — Total likes of the filtered videos.
* **Average Views** — Average views per video.
---

# 📥 Download Filtered Data
The dashboard provides a CSV download option.

Users can download the processed data displayed by the dashboard for further analysis.
---


# ▶️ How to Run the Project

## Step 1 — Install Python

Make sure Python is installed on your computer.

## Step 2 — Install Required Libraries

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

## Step 3 — Keep Required Files Together
Make sure these files are available in the project folder:

```text
stream.py
CAvideos.csv
CA_category_id.json
```
The `CAvideos.csv` file should be in the same folder as `stream.py`.

## Step 4 — Run the Streamlit Dashboard

Run:

```bash
streamlit run stream.py
```
The Streamlit dashboard will open in your web browser.

## Step 5 — Run the Jupyter Notebook

Open:

```text
yt_analysis.ipynb
```

in Jupyter Notebook or VS Code and run the cells to reproduce the Data Science analysis.
---

# 📚 What I Learned
Through this project, I learned how to:

* Work with a real-world dataset.
* Use Pandas for data cleaning and analysis.
* Handle missing and duplicate data.
* Work with datetime data.
* Create analytical features.
* Calculate engagement and like rates.
* Perform exploratory data analysis.
* Analyze correlations between variables.
* Perform time-series analysis.
* Analyze category performance.
* Analyze upload-time patterns.
* Create visualizations using Matplotlib and Seaborn.
* Create a Word Cloud from text data.
* Work with JSON data.
* Build interactive dashboards using Streamlit.
* Add filters and metrics to a dashboard.
* Provide downloadable data from a dashboard.
* Organize and document a Data Science project.
---

# 🎯 Project Goal

The main goal of this project is to transform raw YouTube trending video data into meaningful information through **data cleaning, analysis, visualization, and interactive exploration**.

The combination of the Jupyter Notebook and Streamlit dashboard demonstrates the complete flow from raw data to an interactive Data Science application.
---

# 🚀 Future Improvements
Possible future improvements include:

* Adding more interactive filters.
* Adding additional category comparisons.
* Adding more advanced visualizations.
* Connecting the dashboard to live YouTube data using the YouTube API.
* Deploying the Streamlit dashboard online.
---

# 👩‍💻 Author

**Suman**

**YouTube Trending Video Analysis**
Built with Python, Pandas, Matplotlib, Seaborn, WordCloud, Streamlit, and Jupyter Notebook.

⭐ Thank you for checking out this project!
