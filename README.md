# Fruit and Vegetable Shelf Life Predictor 🍎🥕

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains a Streamlit app that predicts the **category** and **freshness** of fruits and vegetables using a pre-trained CNN model. The app allows users to either **upload a photo** or **take a picture using their camera** for prediction.

## Features
- **Upload a Photo**: Upload an image of a fruit or vegetable for prediction.
- **Take a Picture**: Use your camera to capture an image for prediction.
- **Category and Freshness Prediction**: The app predicts the category (e.g., apple, banana) and freshness (e.g., Fresh, Expired) of the input image.

## Dataset Description
The dataset used to train the CNN model is available on Kaggle and can be found at the following link: [Fruit and Vegetable Dataset for Shelf Life](https://www.kaggle.com/datasets/your-dataset-link).

The dataset is organized into categories, with each category representing a different type of fruit or vegetable. Each category further contains subdirectories for fresh and expired items. The dataset is structured as follows:

dataset/
    ├── category_1/
    │   ├── Fresh/
    │   │   ├── image1.jpg
    │   │   ├── image2.jpg
    │   │   └── ...
    │   ├── Expired/
    │   │   ├── image1.jpg
    │   │   ├── image2.jpg
    │   │   └── ...
    ├── category_2/
    │   ├── Fresh/
    │   │   ├── image1.jpg
    │   │   ├── image2.jpg
    │   │   └── ...
    │   ├── Expired/
    │   │   ├── image1.jpg
    │   │   ├── image2.jpg
    │   │   └── ...
    ├── ...

## Pre-trained Model
The repository includes a pre-trained CNN model for classifying fresh and expired fruits and vegetables:
- **cnnmodel.h5**: A pre-trained CNN model trained on the provided dataset.

## How to Run the App Locally

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/FOOD_EXPIRY_PREDICTOR.git
   ```
2. Navigate to the project folder:
    ```bash
    cd FOOD_EXPIRY_PREDICTOR
    ```
3. Create a virtual environment:
    ```bash
    python -m venv myenv
    ```
4. Activate the virtual environment:
    Windows:
    ```bash
    myenv\Scripts\activate
    ```
    macOS/Linux:
    ```bash
    source myenv/bin/activate
    ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## License

This project is licensed under the Apache License.
