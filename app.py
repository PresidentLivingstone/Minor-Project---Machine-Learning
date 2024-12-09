from flask import Flask, request, render_template
import numpy as np
import pickle
import requests


# Load model and scaler
Model = pickle.load(open('GaussianNB_Classification_Model.pkl', 'rb'))
MinMaxScaler = pickle.load(open('MinMaxScaler.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)


def fetch_random_image(crop_name):
    """Fetch a random image URL for a given crop name from Unsplash API."""
    api_url = f"https://api.unsplash.com/search/photos?query={crop_name}&client_id=4FtxD6-mTiqC0SWpX7AZEVLGZ21YBwnoU8QnVW4_XZ8"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        
        # Parse the JSON response
        data = response.json()
        
        # Check if any images are found
        if data['results']:
            return data['results'][0]['urls']['regular']
        else:
            print(f"No images found for {crop_name}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
    
    return None


@app.route('/')
def predict_page():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def predict():
    try:
        # Retrieve form data
        feature_list = [
            float(request.form['Nitrogen']),
            float(request.form['Phosphorus']),
            float(request.form['Potassium']),
            float(request.form['Temperature']),
            float(request.form['Humidity']),
            float(request.form['Ph']),
            float(request.form['Rainfall'])
        ]

        # Preprocess and predict
        scaled_features = MinMaxScaler.transform(np.array(feature_list).reshape(1, -1))
        prediction = Model.predict(scaled_features)[0]

        # Map prediction to crop name
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
            6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon",
            11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate",
            15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction, None)
        if crop:
            result = f"{crop} is the best crop to be cultivated right there."
            image_url = fetch_random_image(crop)
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
            image_url = None

        return render_template('index.html', result=result, image_url=image_url)
    except Exception as e:
        print(f"Error in prediction: {e}")
        return render_template('index.html', result="An error occurred during prediction.", image_url=None)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0' ,port=5000)
