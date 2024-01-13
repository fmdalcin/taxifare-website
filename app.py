import streamlit as st
import requests

'''
# Use this page to predicte your NYC Fare
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

'''
Enter your ride details below
'''
user_datetime = st.text_input('Enter the pickup time:','2024-01-13 12:00:00')
user_pickup_longitude = st.text_input('Enter the pickup longitude:', '-73.988448')
user_pickup_latitude = st.text_input('Enter the pickup latitude:', '40.743259')
user_dropoff_longitude = st.text_input('Enter the dropoff longitude:','-73.978967')
user_dropoff_latitude = st.text_input('Enter the dropoff latitude:','40.767081')
user_passenger_count = st.text_input("Enter the number of passengers:", '1')



# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...



# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
data = {
        "pickup_latitude": float(user_pickup_latitude),
        "pickup_longitude": float(user_pickup_longitude),
        "dropoff_latitude": float(user_dropoff_latitude),
        "dropoff_longitude": float(user_dropoff_longitude),
        "passenger_count": int(user_passenger_count),
        "pickup_datetime": user_datetime
      }
query = []

if st.button('Check Fare'):
    response = requests.get(url, data)
    if response.status_code == 200:
        # Parse the JSON response
        json_response = response.json()
        st.write("Your predicted fare is ", round(json_response['fare'],2))
    else:
        st.write(f"Request failed with status code {response.status_code}")
