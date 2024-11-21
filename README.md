# CropRecommendationSystem


# Description
The Crop Recommendation System is an application based on machine learning that advises appropriate crop choices, keeping in mind a variety of environmental and soil parameters. It mainly aims to assist farmers and agricultural specialists in making informed decisions concerning crop cultivation, which may help increase yields and also enhance profitability.

It will take into consideration soil composition, climatic conditions, precipitation, temperature, humidity, and pH levels to determine which crops are best suited to a specific geographical location. It uses predictive modeling techniques to analyze historical datasets, offering recommendations tailored to the conditions of a farm or an agricultural region.



# Major Traits
Data Acquisition: The system allows the user to input relevant information, such as soil characteristics, climatic data, and geographical positioning.
Data Preprocessing: The raw data set is first preprocessed to handle missing values, scale or normalize features, and transform categorical variables.
Machine learning models: A mix of several machine learning algorithms is applied, including decision trees, random forests, support vector machines (SVM), and gradient boosting for building the predictive models.
The models are trained using historical data and then evaluated through applicable performance metrics to ensure both accuracy and reliability.

Crop Recommendation: The system suggesting the best crops corresponding to the specified input parameters through the models developed.
User-Centric Interface: The system offers an interface that is user-accessible. It allows users to easily input their information, view suggestions, and explore additional information.



# Technologies Used
Python is the programming language of the model development, data preprocessings, and web applications development.
Scikit-learn: Machine learning library used for model training, evaluation, and prediction.
Pandas: Library is used for preprocessing and analysis of data.
NumPy: Library for numerical computing used to deal with arrays and mathematical operations.
Flask- web framework to write web application that builds an interface and handle HTTP requests.
HTML/CSS: A markup and styling language to design a web interface.
JavaScript is the script language for client-side interaction and advanced user interface.
Matplotlib is used for visualations of data distrubitions before training the Model


# Deployment
The Crop Recommendation System is deployed on Render, a cloud platform for hosting web applications. It is hosted on the free tier, which may cause the application to take a few seconds to load initially due to the "sleep mode" feature. The web app is accessible via the following URL: [🔗 Live Demo](https://croprecommendationsystem-hx1h.onrender.com/)


### Deployment Steps:

Uploaded the project files, including app.py, the machine learning model (all pkl files), and supporting files, to a GitHub repository.
Linked the GitHub repository to Render.
Configured the build environment to install dependencies from requirements.txt and run the application using Gunicorn (gunicorn app:app).
Set up environment variables (if required) for seamless integration.


# How to Run Application on local server 

Navigate to the project directory

Install the required dependencies: pip install -r requirements.txt

Run the app: Python app.py

Open the web browser and access the application at http://localhost:5000 


# Acknowledgements

Recognition I want to thank Kaggle, the agricultural research community, farmers, and various other organizations for providing me with significant insights, data, and specific knowledge that helped me shape this Crop Recommendation System.

# Contact
For any inquiries or questions, please contact me@
mazvoverelivingstone@gmail.com
