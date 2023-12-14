import streamlit as st
import joblib

# Load your pre-trained model
model = joblib.load('linear_regression_model.joblib')

# Define the function to make predictions
def make_prediction(college_name):
    # Preprocess the college name before making predictions
    preprocessed_college_name = preprocess_text(college_name)

    # Use the model to make predictions
    prediction = model.predict([preprocessed_college_name])[0]
    return prediction

def preprocess_text(text):
    processed_text = text.lower()

    return processed_text

def main():
    st.title('College Rating Prediction App')

    # Create a dropdown menu for selecting a college name
    new_college_name = st.selectbox('Select the college name:', [
        'Srinivas Institute of Technology',
        'Sahyadri College of Management',
        'St Joseph Engineering College',
        'BMS College of Engineering',
        'Dayananda Sagar College of Engineering',
        'S K S J T Institute of Engineering',
        'Dr Ambedkar Institute of Technology',
        'R V College of Engineering',
        'M S Ramaiah Institute of Technology',
        'Bangalore Institute of Technology',
        'P E S University',
        'M V J College of Engineering',
        'S J C Institute of Technology',
        'Dr T Timmaiah Institute of Technology',
        'Siddaganga Institute of Technology',
        'Sri Siddartha Institute of Technology',
        'Kalpataru Institute of Technology',
        'J S S Science and Technology University',
        'Malnad College of Engineering',
        'Tontadarya College of Engineering',
        'Maratha Mandal Engineering College',
        'Basaveshwara Engineering College',
        'S D M College of Engineering',
        'P D A College of Engineering',
        'Gurunanak Dev Engineering College',
        'N M A M Institute of Technology',
        'K V G College of Engineering',
        'P A College of Engineering',
        'H M S Institute of Technology',
        'H K B K College of Engineering',
        'Vivekananda College of Engineering',
        'Nagarjuna College of Engineering'
    ])

    # Create a button to make predictions
    if st.button('Predict Rating'):
        # Make prediction
        prediction = make_prediction(new_college_name)

        # Display the prediction
        st.success(f'The predicted rating is: {prediction}')

if __name__ == '__main__':
    main()
