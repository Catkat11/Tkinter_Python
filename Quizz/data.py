# Importing the requests module
import requests

# Defining parameters for the API request
parameters = {
    "amount": 10,         # Specifying the number of questions
    "type": "boolean"     # Specifying the type of questions (boolean)
}

# Sending a GET request to the API with the specified parameters
response = requests.get("https://opentdb.com/api.php",  params=parameters)

# Checking the response status - if it's not 200 (OK), raise an exception
response.raise_for_status()

# Getting data from the response in JSON format
question_data = response.json()["results"]
