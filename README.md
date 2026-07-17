# Smart Crop Recommendation System

A machine learning based web application that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions.

The application uses a trained Random Forest model to analyze agricultural parameters and provide crop recommendations instantly through an interactive Streamlit interface.

## Live Demo

https://crop-recommendation-system-7hk8.onrender.com/

## Features

* Predicts the most suitable crop based on user input.
* Supports 22 different crop categories.
* Displays crop names in both English and Bangla.
* Shows prediction confidence score.
* Provides recommendation explanations in both Bangla and English.
* Modern and responsive Streamlit user interface.
* Feature importance visualization.
* Real-time prediction results.

## Input Parameters

The model uses the following agricultural parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

## Machine Learning Model

* Algorithm: Random Forest Classifier
* Number of Features: 7
* Number of Crop Classes: 22

## Technology Stack

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* Matplotlib
* Joblib

## Project Structure

```text
Crop-recommendation-system/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/prethul/Crop-recommendation-system.git
```

Move into the project directory:

```bash
cd Crop-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Future Improvements

* Weather API integration
* Fertilizer recommendation system
* Soil health analysis
* Crop yield prediction
* Multilingual support
* Historical crop analytics

## Author

Dipto Howlader Prethul

CSE Undergraduate Student
Uttara University

## License

This project is developed for educational and portfolio purposes.
