#  Movie Recommendation System
![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/edbf5143-185d-444d-8985-1c6dbca8d0f3)![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/681440ad-acfb-41c9-b8d3-10362041948a)


##  Project Overview

Welcome to our Movie Recommendation System, where movie suggestions go beyond the ordinary. This intelligent application blends advanced recommendation strategies, including Collaborative Filtering, Content-Based Recommendation, and Non-Personalized Approaches, to curate a personalized and engaging movie-watching experience.

##  Problem Statement

Finding the perfect movie can be a challenge, especially for new users. Our system addresses this by seamlessly transitioning from non-personalized recommendations to advanced models. Whether you're a seasoned critic or a first-time viewer, our system adapts to your preferences.


##  Recommendation Approaches

### A) Simple Recommender System - Average Weight

The Simple Recommender system offers universal movie suggestions by considering overall popularity and occasional genre preferences. This model prioritizes movies with higher popularity and critical acclaim, assuming they are more likely to be appreciated by the average audience.

**Implementation:**
- Movies are sorted based on ratings and popularity.
- Top movies from this sorted list are presented.
- Users can specify a genre for personalized recommendations.

**Mathematical Model (IMDB's Weighted Rating Formula):**

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/b64fa18a-f02a-4a75-9be8-d860a8b0d520)

- **v:** Number of votes for the movie
- **m:** Minimum votes required to be listed in the chart (set at the 85th percentile)
- **R:** Average rating of the movie
- **C:** Mean vote across the entire dataset

**Functionality:**
- Create Top 250 movies chart.
- Develop charts tailored to specific genres.

### B) Content-Based Recommendation System

Enhance the personalization of recommendations with a Content-Based Recommendation engine. This engine calculates similarities between movies using specific criteria, suggesting movies that closely resemble a particular film enjoyed by the user.

**Focus Areas:**
- Movie Overviews
- Movie Cast
- Director
- Keywords
- Genre

**Working Mechanism:**
- Content-Based Recommendation focuses on intrinsic movie features, such as Movie Cast,Director and genres.
- Understand your preferences through the genres, favourtive cast and the director you enjoy.
- Predict and suggest movies with similar content, adding a layer of personalization based on thematic elements.


##  Key Aspects and Features
- **Content-Based Recommendation:** Discover movies similar to your favorites using advanced natural language processing and cosine similarity.
- **Popularity-Based Recommendation:** Explore trending movies based on overall popularity and user ratings.
- **Data Analysis:** Dive into insightful visualizations exploring the world of movies, genres, and more.
- **Streamlit Web App:** Explore movie recommendations interactively through our Streamlit web app. Tailor your preferences, and witness the system craft a unique movie playlist just for you.

##  Technologies and Techniques Used:
-  Python
-  Pandas, NumPy, Matplotlib, Seaborn
-  Natural Language Processing with NLTK
-  Machine Learning with Scikit-Learn
-  Streamlit for Web App Development
-  Requests for HTTP Handling



##  Usage Instructions
**Get Started:**
1. **Clone the repository:**
   

2. **Install dependencies:**
   

3. **Deployment:**
   
   Feel free to explore, contribute, and enhance the movie recommendation experience. Your movie night starts here! 
   
5. **Open the web browser and go to the local host1to explore the Movie Recommendation System.**

##  Data Exploration and Analysis :

### Step 1: Loading Data

- Open the Jupyter Notebook (`Movie_Recommendation_System.ipynb`) to initiate the exploration and analysis of the movie dataset.
- Follow the step-by-step instructions to load the movie data from (`tmdb_5000_movies.csv`) and proceed with the analysis.

### Step 2: Selecting Key Features
- Identify and select key features for the analysis, including genres, id, keywords, overview, popularity, release_date, title, vote_average, vote_count, cast, and crew.

### Step 3: Cleaning Data
- Clean the data, especially focusing on columns like genres, keywords, cast, and crew, which are in dictionary format.
- Utilize the Abstract Syntax Trees (`.ast`) module in Python to convert dictionary literals into objects.


## A) Recommendation System Based on Average Weight

### Step 4: Calculate Weighted Rating Components
- Implement the calculation of all components of the weighted rating, incorporating factors like vote count, average rating, and overall popularity.

### Step 5: Recommendation Based on Average
- For the recommendation system based on average, focus on specific columns: genre, popularity, release_date, vote_average, vote_count, and weighted_average.

### Step 6: Popularity-Based Recommendation
- Arrange movies in descending order based on popularity to check for popular recommendations.
1704/recomend_movie/assets/140384850/c4c03d17-34d0-42cb-b784-e0ba5e3cefca)


### Step 7: Combined Recommendation System
- Create a new recommendation system that considers both weighted average and popularity with a 50-50 priority, forming a new column as a scorecard.


### Step 8: Genre-Specific Recommendations
- Explore recommendations based on particular genres.



## B) Content-Based Recommendation System

### Step 9: Selecting Features for Content-Based Recommendation
- Choose key features for the Content-Based Recommendation System, including id, title, genres, keywords, overview, cast, and director.

### Step 10: Preprocessing Overview
- Split words in the overview into individual tags and create a collection of tags from columns like genres, overview, keywords, cast, and director.



### Step 11: Building Recommendation System
- Convert each tag of a particular movie into a set of arrays and form a matrix.
- Build a recommendation system based on the similarity of arrays by calculating the minimum distance between two pairs.


### Step 12: Customizing Recommendations
- Replace 'particular movie' with the desired movie title to tailor recommendations according to user preferences.





Explore the notebook for a detailed walkthrough of these steps and gain insights into the world of movie recommendations!

##  Deployment Using Streamlit Web App

### Step 1: Opening the Streamlit Web App Interface

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/f25c8fa0-768b-4c2b-9f3e-bdaa9597b6ad)

- Open the Streamlit web app interface by running the provided command in the terminal.
- The initial screen presents a clean and user-friendly interface.

### Step 2: Choosing Recommendation Approaches

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/40d40823-690d-4635-addc-bbeee76f080c)

- Select the recommendation approaches you would like to explore.

### Step 3(a): Popularity-Based Recommendation System

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/912d1696-1422-459c-ae5f-c494729f58c5)

- Navigate to the popularity-based recommendation system.
- A new interface appears with the same heading.

### Step 4: Choosing Genres for Recommendations
![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/621e1d65-b6f7-408c-9d4b-3558eabdf66b)


- Choose the genres of your interest.
- The system will suggest 250 movies with their posters in descending order of the scorecard within the selected genres.
 ### Popularity-based recommendation system.

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/99168239-6f77-4e5a-add2-7daf529d71f6)

### Step 3(b): Content-Based Recommendation System
![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/79855b2f-91ac-4c7a-a1cf-965deb3fd068)


- Switch to the content-based recommendation system in the select box.

### Step 5: Typing Movie Title for Recommendations

- Type the title of a movie, and the system will show 5 similar movie names with their posters.

![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/7315e6ce-dcc6-4061-84a8-811ed0265168)

### Content-based recommendation system.
  ![image](https://github.com/Tanwar-12/MOVIE-RECOMMENDATION-SYSTEM/assets/110081008/c0c7b94f-0415-4053-a965-acdfab4ec8dc)










