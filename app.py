import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.sav', 'rb'))
st.sidebar.header('Please fill this section: ')

def user_report():
    area = st.sidebar.text_input('Area SqFt', 3500)
    bedrooms = st.sidebar.slider('Bedrooms', 1, 5, 1)
    bathrooms = st.sidebar.slider('Bathrooms', 1, 5, 1)
    
    guestroom_index = st.sidebar.selectbox('Guestroom', options=['No', 'Yes'])
    guestroom = 1 if guestroom_index == 'Yes' else 0
    
    basement_index = st.sidebar.selectbox('Basement', options=['No', 'Yes'])
    basement = 1 if basement_index == 'Yes' else 0
    
    waterheating_index = st.sidebar.selectbox('Hot Water Heating', options=['No', 'Yes'])
    hotwaterheating = 1 if waterheating_index == 'Yes' else 0
    
    airconditioning_index = st.sidebar.selectbox('Air Conditioning', options=['No', 'Yes'])
    airconditioning = 1 if airconditioning_index == 'Yes' else 0
    
    furnishing_index = st.sidebar.selectbox('Furnishing Status', options=['Unfurnished', 'Semi-Furnished', 'Furnished'])
    if furnishing_index == 'Furnished':
        furnishingstatus = 0
    elif furnishing_index == 'Semi-Furnished':
        furnishingstatus = 1
    else:
        furnishingstatus = 2
    
    user_report_data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotwaterheating,
        'airconditioning': airconditioning,
        'furnishingstatus': furnishingstatus
    }
    
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()

st.write(''' 
## House Price Prediction

This web for predict your dream house price :D
''')
st.header('House data')
st.write(user_data)

if st.button('Predict'):
    house_price = model.predict(user_data)

    formatted_price = '${:,.2f}'.format(house_price[0])
    st.subheader('Your predicted house price')
    st.write(formatted_price)