import streamlit as st

st.set_page_config(page_title="Pediatric BOPS Calculator", 
                   page_icon="💉", 
                   layout='centered')

def calculate_BOPS(crying, facial_expression, verbal_response, body_movement):
    score = crying + facial_expression + verbal_response + body_movement
    return score

st.title('Pediatric BOPS Calculator')
st.write("""
This application calculates the Behavioral Observational Pain Scale (BOPS) for post-operative pediatric pain. 
It assists health professionals in assessing pain levels based on four observable behaviors: crying, facial 
expression, verbal response, and body movement. The resulting score helps guide pain management strategies.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    crying = st.sidebar.slider('Crying', 0, 2, 0)
    facial_expression = st.sidebar.slider('Facial Expression', 0, 2, 0)
    verbal_response = st.sidebar.slider('Verbal Response', 0, 2, 0)
    body_movement = st.sidebar.slider('Body Movement', 0, 2, 0)
    data = {'Crying': crying,
            'Facial Expression': facial_expression,
            'Verbal Response': verbal_response,
            'Body Movement': body_movement}
    return data

user_input = user_input_features()

st.subheader('User Input parameters')
st.write(user_input)

BOPS_score = calculate_BOPS(user_input['Crying'], user_input['Facial Expression'], 
                            user_input['Verbal Response'], user_input['Body Movement'])

st.subheader('Calculated BOPS Score')
st.write(BOPS_score)
