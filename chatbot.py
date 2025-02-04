import json
import requests
from datetime import datetime
import openai

# OpenAI API Key (Replace with your key)
openai.api_key = "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"


# Load responses from JSON
def load_responses(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        responses = {entry['question'].lower(): entry['answer'] for entry in data['questions_answers']}
    return responses


# Function to get response
def get_response(translQuery, responses):
    translQuery = translQuery.lower()

    # Check if question is in JSON
    if translQuery in responses:
        response = responses[translQuery]

        # Replace placeholders with dynamic values
        if "{time}" in response:
            response = response.replace("{time}", datetime.now().strftime("%H:%M"))
        elif "{date}" in response:
            response = response.replace("{date}", datetime.now().strftime("%d/%m/%Y"))
        return response

    # If question is not in JSON, search online
    else:
        return fetch_online_response(translQuery)


# Function to fetch online response (using DuckDuckGo API)
def fetch_online_response(translQuery):
    url = f"https://api.duckduckgo.com/?q={translQuery}&format=json"
    try:
        response = requests.get(url, timeout=5)  # Set a timeout to prevent hanging
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()

        print("DuckDuckGo Response:", data)  # Debugging line

        if "Abstract" in data and data["Abstract"]:
            return data["Abstract"]
        elif "RelatedTopics" in data and data["RelatedTopics"]:
            return data["RelatedTopics"][0]["Text"]  # Return the first related topic
        else:
            return chat_with_ai(translQuery)  # Fall back to AI response
    except requests.exceptions.RequestException as e:
        return f"Error fetching online data: {e}"



# Function to fetch AI-generated response (OpenAI API)
import openai

# Initialize the OpenAI client
client = openai.OpenAI(api_key="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")

def chat_with_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error fetching AI response: {e}"

