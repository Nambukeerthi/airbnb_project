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

Video Link: [Linked-IN Video](https://www.linkedin.com/posts/keerthi-r-9b8839283_project-name-airbnb-analysis-project-website-activity-7296602704175321088-TPVE?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEUARVwBltI0ri4ApeK7YzcbHxGViaHfWEM)

Portfolio: [Nambu Keerthi](https://portfolio-b5zieg8xn5nhwau5b4bhp8.streamlit.app/)

## Introduction 
This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends in the Airbnb marketplace.

*Domain:* Travel Industry, Property Management and Tourism

## Technologies Applied
* Python
* Streamlit 
* Pymongo 
* Plotly
* MySQL


## Project Setup
1. Firstly install all the required extensions in the requirements.txt
```
pip install -r requirements.txt
```

2. Now one need setup a Google Cloud Project on Google Cloud Console, and then enable the Youtube API v3, after that generate the credentials and copy the api_key. Now below is the Python code to use that API.
```
youtube = build('youtube', 'v3', developerKey="your api_key goes here")
```

3. After that one need to create a MySQL Database in there local system. Now below is the Python code to connect to that SQL Database
```
hostname = "your host name goes here"
database = "your database name goes here"
username = "your username goes here"
pwd = "your password goes here"

mydb = sql.connect(host=hostname, user=username, password=pwd, database=database)
                   
cursor1 = mydb.cursor()
```

4. To run the application
```
streamlit run main.py
```

   
## Project Methodology

1. First click the "Create DB" button after that the database will created

2. Enter a YouTube channel ID in the input field and click the "Details" button. The channel details will then be displayed. After that, click the "Upload" button to upload channel details such as Channel ID, Channel Name, Playlist ID, Subscribers, Views, Total Videos, 
   Description, and more, to the SQL database.

3. Now from the sidebar select the Task Menu and Select the required statement.

3. According to the selected statement the data will be queried from the SQL Database and will be displayed here on the screen in the streamlit application

4. through the click the "Drob DB" button the created database and details will droped.
