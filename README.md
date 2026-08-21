YouTube Trending Video Analysis

📌 Project Overview

The **YouTube Trending Video Analysis** project is a data analysis and visualization project built using Python. The purpose of this project is to explore YouTube trending videos and understand what makes videos perform well in terms of views, likes, comments, engagement, and other factors.

An interactive **Streamlit dashboard** was created to make the analysis easier to understand and explore. Users can select different categories and date ranges and view the results through metrics, tables, and visualizations.

🎯 Main Objectives of the Project
The main objectives of this project are:

- Analyze YouTube trending video data.
- Clean and prepare the dataset for analysis.
- Understand video performance using views, likes, and comments.
- Calculate engagement rate and like rate.
- Analyze the distribution of videos across categories.
- Identify top-performing and highly engaging videos.
- Explore frequently used video tags.
- Analyze video upload patterns by day and hour.
- Build an interactive dashboard using Streamlit.
- Present the analysis in a simple and user-friendly way.

🔎 What This Project Does
This project takes a YouTube trending video dataset and performs data cleaning, preparation, analysis, and visualization.
The project creates additional features such as:

- **Engagement Rate**
- **Like Rate**
- **Publish Day**
- **Publish Hour**

The processed data is then used to create an interactive Streamlit dashboard.
Users can select a category and date range and explore how the data changes through different metrics, tables, charts, a Word Cloud, and an Upload Time Heatmap.


🛠️ Technologies Used
The project was developed using the following technologies and libraries:

- **Python** — Programming and data analysis
- **Pandas** — Data cleaning and data manipulation
- **Matplotlib** — Data visualization
- **Seaborn** — Heatmap and visualization
- **WordCloud** — Visualization of trending video tags
- **Streamlit** — Interactive dashboard
- **JSON** — YouTube category information

📁 Project Structure
```text
YouTube-Trending-Video-Analysis/
│
├── stream.py
├── CAvideos.csv
├── CA_category_id.json
├── requirements.txt
├── README.md
└── .gitignore

📄 What Each File Does
stream.py: This is the main Streamlit application. It contains the code for:

Loading the dataset
Preparing the data
Creating filters
Calculating metrics
Creating tables
Creating charts
Creating the Word Cloud
Creating the Upload Time Heatmap
Providing the dataset download option
Displaying the dashboard

CAvideos.csv: This is the main YouTube trending video dataset used for the analysis.
The dataset is large, so it may be kept locally instead of being uploaded to GitHub.

CA_category_id.json: This JSON file contains YouTube video category information and category IDs.

requirements.txt: This file contains the Python libraries required to run the project.

README.md: This file provides information about the project, its purpose, features, technologies, and instructions for running it.

.gitignore: This file tells Git which files or folders should not be uploaded to the repository, such as the large dataset and Python environment files.


📊 Dashboard Features
The Streamlit dashboard contains several sections that allow users to interact with and understand the YouTube trending data.

🔎 1. Category Filter
A category dropdown is available in the sidebar.
Users can select a category and the dashboard updates the relevant data according to the selected category.

📅 2. Date Filter
A date range filter allows users to select a specific time period for analysis.
The dashboard updates according to the selected dates.

⭐ Main Features

📈 3. Views vs Likes
A scatter plot is used to explore the relationship between:
Views
Likes
This helps understand whether videos with more views also tend to receive more likes.

🏆 4. Top Videos by Views
The dashboard displays the top videos based on the number of views.
The table includes:
Video title
Views
Likes
Comment count

🔥 5. Top Engaging Videos
Videos are sorted according to their calculated engagement rate.
This helps identify videos that receive a high level of interaction compared with their number of views.
Engagement Rate
Engagement Rate = ((Likes + Comments) / Views) × 100

👍 6. Top Videos by Like Rate
The dashboard displays videos with the highest like rate.
Like Rate
Like Rate = (Likes / Views) × 100
This helps compare the number of likes with the number of views.


📊 Charts and Visualizations
The project includes several visualizations:
Views vs Likes Scatter Plot:
Shows the relationship between views and likes.

Videos by Category:
A bar chart shows how many videos are available in each category.

Trending Video Tags Word Cloud:
A Word Cloud shows frequently appearing tags from trending videos.
The Word Cloud changes according to the selected category.

Upload Time Heatmap:
The heatmap shows the number of videos uploaded according to:
Day of the week
Hour of the day
The days are arranged from Monday to Sunday.
The heatmap uses the filtered data, so it changes when the category or date range is changed.

📌 Key Metrics
The dashboard displays four important metrics:

Total Videos:Shows the total number of videos available after applying the selected filters.

Total Views:Shows the total number of views for the filtered videos.

Total Likes:Shows the total number of likes for the filtered videos.

Average Views:Shows the average number of views per video.
These metrics update dynamically when the user changes the filters.


📥 Download Filtered Data
The dashboard includes a Download CSV button.
Users can download the processed dataset directly from the dashboard.
This makes it easier to save and use the analyzed data for further work.

🧹 Data Cleaning and Preparation
Before creating the dashboard, the dataset was explored and prepared for analysis.
The data preparation process included:

Checking the dataset structure.
Checking the number of rows and columns.
Checking missing values.
Checking duplicate records.
Removing duplicate records where required.
Converting publish_time into datetime format.
Extracting the publishing day.
Extracting the publishing hour.
Ordering the days from Monday to Sunday.
Working with category IDs and category information.

Additional analytical columns were created for better analysis:

engagement_rate
like_rate
publish_day
publish_hour


▶️ How to Run the Project
Step 1 — Install Python
Make sure Python is installed on your computer.

Step 2 — Install Required Libraries
Open the terminal in the project folder and run:
pip install -r requirements.txt

Step 3 — Keep the Dataset in the Project Folder
Make sure the following files are available:

stream.py
CAvideos.csv
CA_category_id.json
The CAvideos.csv file should be in the same folder as stream.py.

Step 4 — Run the Streamlit Dashboard
Run:streamlit run stream.py
The Streamlit dashboard will open in your web browser.

📚 What I Learned
While working on this project, I learned how to:

Work with a real-world dataset.
Use Pandas for data cleaning and analysis.
Handle missing and duplicate data.
Convert and work with datetime data.
Create new analytical features.
Calculate engagement and like rates.
Use Matplotlib and Seaborn for visualization.
Create a Word Cloud from text data.
Build interactive dashboards using Streamlit.
Add filters to a dashboard.
Display metrics and interactive tables.
Work with JSON category data.
Create a requirements file for a Python project.
Write project documentation using README.
Organize a data analysis project.

🎯 Project Goal
The main goal of this project is to turn raw YouTube trending video data into meaningful information through data analysis and interactive visualization.
The Streamlit dashboard makes it possible to explore video performance and discover patterns in categories, engagement, likes, views, tags, and upload times in an easy and interactive way.

🚀 Future Improvements
Some possible improvements for the project include:

Adding more advanced filters.
Adding more category-based comparisons.
Adding monthly and yearly trend analysis.
Adding additional interactive visualizations.
Connecting the project to live YouTube data using the YouTube API.
Deploying the Streamlit dashboard online.

👩‍💻 Author
Suman
YouTube Trending Video Analysis Built with Python, Pandas, Matplotlib, Seaborn, WordCloud, and Streamlit.

⭐ Thank you for checking out this project!