<h1> Airbnb_Analysis</h1>


<h1 align="center">
  <br>
  <a href=""><img src="airbnbdata/Airbnblogo.png" alt="Airbnb Analysis" width="200"></a>
  <br>
 
  <br>
</h1>


<p align="center">
  <a href="#Introduction"></a>
  <a href="#Technologies Applied"></a>  
</p>

Video Link: [Linked-IN Video](https://www.linkedin.com/posts/nambu-keerthi-r-9b8839283_project-name-airbnb-analysis-project-website-activity-7296602704175321088-_W57?utm_source=share&utm_medium=member_android&rcm=ACoAABMFg5wB3AA0b9CHRbG1E_77kFaZB8cVz7c)

Portfolio: [Nambu Keerthi](https://portfolio-b5zieg8xn5nhwau5b4bhp8.streamlit.app/)

## Introduction 
This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends in the Airbnb marketplace.

**Domain** : *Travel Industry, Property Management and Tourism*

## Technologies Applied
* Python
* Streamlit 
* Pymongo 
* Plotly
* Pandas


## Project Setup
1. Firstly install all the required extensions in the requirements.txt
```
pip install -r requirements.txt
```

2. Now one need to create mangoDB account for get data from that.
```
mongodb+srv://nambu935:<db_password>@keerthi.i2brs.mongodb.net/?retryWrites=true&w=majority&appName=Keerthi
```

3. After that we need to connect mangoDB in there local system. Now below is the Python code to connect to that mangodb
```
client = pymongo.MongoClient("mongodb+srv://nambu935:nambukeerthi@keerthi.i2brs.mongodb.net/?retryWrites=true&w=majority&appName=Keerthi")
db = client["sample_airbnb"]
coll = db["listingsAndReviews"]

```
4. After getting that all dataset, we need to cleaning and preprocessing that. the next step is merge from all dataset to one single dataset.  
```
df_merge_1 = pd.merge(df1_copy,df_host_2, on = "_id")
df_merge_2 = pd.merge(df_merge_1,df_address_1, on = "_id")
df_merge_3 = pd.merge(df_merge_2,df_available_1, on = "_id")
df_merge_4 = pd.merge(df_merge_3,df_amenities, on = "_id")
```
5. The next step is create barchat, pie chat for easy visualization and quick understanding by using python code.

 
6. Create streamlit app. And run it 
```
streamlit run airbnb.py
```

   
## Project Methodology

1. Create a connection to the MongoDB Atlas database and initiate the process of retrieving the Airbnb dataset from it.

2. Prepare the Airbnb dataset for exploratory data analysis (EDA) and visualization tasks by first addressing missing values, eliminating duplicates, and making appropriate data type transformations

3. This critical data preprocessing step is essential for maintaining data integrity and consistency, ensuring that the dataset is in an optimal state for further analysis.

4. Create a web application using Streamlit that harnesses geospatial information from the Airbnb dataset to generate interactive maps, allowing users to explore and engage with location-based data related to Airbnb listings and properties.

5. This application will empower users to visualize and interact with the geographical aspects of Airbnb data, enhancing their understanding of property distribution, pricing trends, and other relevant insights within a map-centric interface.

6. Utilize the refined dataset to conduct an analysis and generate visual representations showcasing the fluctuations in prices across various geographical locations, types of properties, and seasons.

7. Develop interactive graphs and charts that empower users to investigate pricing trends, identify outliers, and discern correlations with other factors.

   
