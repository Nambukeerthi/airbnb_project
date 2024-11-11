import pandas as pd
import streamlit at st
import json

# READ CSV DATA FILE
df_csv = pd.read_csv("airbnbdata/airbnb.csv")
df1_copy=pd.DataFrame(df_csv)

# IMAGE COLUME CORRECTION
# Step 1: Replace single quotes with double quotes (only if the entry is a string)
df1_copy["images"] = df1_copy["images"].apply(lambda x: x.replace("'", '"') if isinstance(x, str) else x)
# Step 2: Parse the corrected string into a dictionary using json.loads()
df1_copy["images"] = df1_copy["images"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
# Step 3: Access the 'picture_url' key from the parsed dictionary
df1_copy["images"] = df1_copy["images"].apply(lambda x: x.get("picture_url", "No URL") if isinstance(x, dict) else "No URL")

# REVIEW SCORE COLUME CORRECTION
# Step 1: Replace single quotes with double quotes (only if the entry is a string)
df1_copy["review_scores"] = df1_copy["review_scores"].apply(lambda x: x.replace("'", '"') if isinstance(x, str) else x)
# Step 2: Parse the corrected string into a dictionary using json.loads()
df1_copy["review_scores"] = df1_copy["review_scores"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
# Step 3: Access the 'picture_url' key from the parsed dictionary
df1_copy["review_scores"] = df1_copy["review_scores"].apply(lambda x: x.get("review_scores_rating", 0) if isinstance(x, dict) else 0)

# HANDLING NULL VALUES
# df1_copy.isnull().sum() to know null values
# bedrooms, beds, bathrooms, cleaning_fee
df1_copy["bedrooms"] = df1_copy["bedrooms"].fillna(0)
df1_copy["beds"] = df1_copy["beds"].fillna(0)
df1_copy["bathrooms"] = df1_copy["bathrooms"].fillna(0) 
df1_copy["cleaning_fee"] = df1_copy["cleaning_fee"].fillna(0)
