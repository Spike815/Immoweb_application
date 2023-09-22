from dotenv import load_dotenv
import os
import pandas as pd
import boto3
import joblib
from io import BytesIO
import xgboost
from pathlib import Path


env_path = Path().cwd() / "ml_model/.env"
load_dotenv(env_path)


access = os.getenv('ACCESS_KEY')
secret = os.getenv('SECRET_KEY')
def s3_obj():
    s3 = boto3.client(
        service_name='s3',
        region_name='eu-west-3',
        aws_access_key_id=access,
        aws_secret_access_key=secret
    )
    return s3

def get_model():
    s3=s3_obj()
    with BytesIO() as f:
            s3.download_fileobj(Bucket="immostudy-temp", Key="ml_model/XGB.joblib", Fileobj=f)
            f.seek(0)
            file = joblib.load(f)
    return file

#get the cleaned csv file for visualization from s3 bucket
def get_data():
     s3=s3_obj()
     s3_csv_obj = s3.get_object(Bucket='immostudy-temp', Key="csv_files/cleaned_data.csv")["Body"]
     return s3_csv_obj
     
def preprocess_new_data(input):
    """this function takes the input and returns a dataframe object which fits the machine learning model"""
  # convert the input to a dictionary
    df = pd.DataFrame([input])
    X=df.to_numpy()
    return X

def predict_new_data(X,model):
    y_pred = model.predict(X)
    number =int(y_pred[0])
    return f"The property you are looking for worthes :{number} euro."


# test_dict={
#   "type_of_property": "HOUSE",
#   "number_of_bedrooms": 2,
#   "living_area": 100,
#   "furnished": 1,
#   "terrace": 1,
#   "terrace_area": 0,
#   "garden": 1,
#   "garden_area": 0,
#   "total_property_area": 0,
#   "total_land_area": 0,
#   "number_of_facades": 0,
#   "swimming_pool": 1,
#   "state_of_the_building": "GOOD",
#   "province": "West-Vlaanderen",
#   "kitchen": "Hyper equipped",
#   "digit": 0
# }