# Immoweb_application
## Description
In this project, I designed the interactive applicationa to help users visualize and predict property prices in Belgium, specifically focusing on real estate properties listed on [Immoweb](https://www.immoweb.be/en). Below are some key points about this project: 


### -Data Collection and Processing

Prior to designing this web app, we implemented a data collection and processing pipeline using Apache Airflow. This pipeline scrapes real estate property listings from immoweb.be, cleans the data, and prepares it for visualization and machine learning modeling. All processed data files are stored in an Amazon S3 bucket with automatic versioning, ensuring data integrity and reproducibility.


### -Scheduled Data Updates

The data collection and processing task is scheduled to run daily. This ensures that the property listings remain up to date, providing users with the most current information on property prices.


### -Property Price Visualization

The web app takes the cleaned and processed data to display property prices on an interactive map. Users can easily explore property prices in different regions, helping them make informed decisions about buying real estate.


### -Custom API for Price Inquiries

In addition to the web application, we have developed a custom API that allows users to query property prices based on their specific preferences. Users can input their criteria, such as location, property type, and features, to obtain price estimates for properties they are interested in purchasing.

This project combines data engineering, machine learning, and web development to provide a comprehensive solution for real estate property price prediction and visualization. I hope this repository proves useful and informative for anyone interested in real estate market analysis in Belgium.


## Usage
Simply go the the web app deployed on stremlit [immo app](https://immoweb-price-predict.streamlit.app/), and give the input for your dream property. I will calculate for you!


## 🚀 About Me
This project is done by Bo Cao, Junior Data Engineer in Becode, Gent. Here below you can find the contact:

<a href = 'https://www.linkedin.com/in/bo-cao-313ab244'> Linkedin </a>
