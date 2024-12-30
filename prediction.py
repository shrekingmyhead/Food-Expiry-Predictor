import cv2
import numpy as np
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('food-expiry-predictor\cnnmodel.h5')

# Define the categories (fruits and vegetables)
categories = ['apples', 'banana', 'orange', 'carrot', 'tomato', 'strawberry', 'potato', 'bellpepper', 'cucumber','mango']
# Function to preprocess the input image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Unable to read image: {image_path}")
        return None
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    return image

# Function to make predictions
def predict_image(image_path):
    image = preprocess_image(image_path)
    if image is None:
        return None
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0]
    predicted_label = np.argmax(prediction)
    predicted_category = categories[predicted_label // 2]
    if predicted_label % 2 == 0:
        freshness = 'Fresh'
    else:
        freshness = 'Expired'
    return predicted_category, freshness

def fetch_current_price(predicted_category):
    # Use the API to fetch the current price
    # Replace this with your actual API call
    api_url = "https://data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi"
    params = {
        "q": produce_name,
        "format": "json"
    }
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Extract relevant price information from the API response
        current_price = data[0]['max_price']
        return current_price
    else:
        return None

# Example usage
image_path = r"C:\Users\S Sri Hari\mithack\image.png"
prediction = predict_image(image_path)
if prediction is not None:
    predicted_category, freshness = prediction
    print(f"Predicted category: {predicted_category}")
    print(f"Freshness: {freshness}")
