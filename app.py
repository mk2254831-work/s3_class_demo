from flask import Flask, render_template, request, jsonify
import requests
import json
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Google Gemini API Configuration
GEMINI_API_KEY = "AIzaSyCtljQ1UUPCB8HKYde1wQ7GbYOxaBhU_RU"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    from_city = data.get('from_city')
    to_city = data.get('to_city')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Create a prompt for Gemini to generate flight recommendations
    prompt = f"""
    Generate realistic flight options for a trip from {from_city} to {to_city} on {start_date}.
    Please provide 5 different flight options with the following details in JSON format:
    
    Include only Indian airlines like IndiGo, Air India, SpiceJet, Vistara, GoAir.
    Make the flight times and prices realistic for Indian domestic flights.
    
    Format the response as a JSON array with this structure:
    [
        {{
            "airline_name": "IndiGo",
            "from": "{from_city}",
            "to": "{to_city}",
            "departure": "2024-01-15T08:30:00",
            "arrival": "2024-01-15T10:45:00",
            "fare": "₹4,500"
        }}
    ]
    
    Make sure prices are in Indian Rupees (₹) and times are realistic for {from_city} to {to_city} route.
    Sort them from cheapest to most expensive.
    """

    # Prepare request to Gemini API
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # Make API request to Gemini
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({"error": f"Failed to fetch from Gemini API: {response.status_code}"}), 500

    try:
        gemini_response = response.json()
        
        # Extract the generated text from Gemini response
        generated_text = gemini_response['candidates'][0]['content']['parts'][0]['text']
        
        # Try to extract JSON from the generated text
        import re
        json_match = re.search(r'\[[\s\S]*\]', generated_text)
        
        if json_match:
            flights_json = json_match.group()
            flights = json.loads(flights_json)
        else:
            # If JSON parsing fails, create sample flights as fallback
            flights = generate_sample_flights(from_city, to_city, start_date)
        
        return jsonify(flights[:5])  # Return top 5 results
        
    except Exception as e:
        # Fallback to sample data if API fails
        flights = generate_sample_flights(from_city, to_city, start_date)
        return jsonify(flights)

def generate_sample_flights(from_city, to_city, date):
    """Generate sample flight data as fallback"""
    airlines = ["IndiGo", "Air India", "SpiceJet", "Vistara", "GoAir"]
    
    flights = []
    base_price = random.randint(3000, 8000)
    
    for i, airline in enumerate(airlines):
        departure_hour = random.randint(6, 20)
        flight_duration = random.randint(1, 4)  # 1-4 hours
        
        departure_time = f"{date}T{departure_hour:02d}:{random.randint(0, 59):02d}:00"
        arrival_hour = (departure_hour + flight_duration) % 24
        arrival_time = f"{date}T{arrival_hour:02d}:{random.randint(0, 59):02d}:00"
        
        price = base_price + (i * random.randint(500, 1500))
        
        flight = {
            "airline_name": airline,
            "from": from_city,
            "to": to_city,
            "departure": departure_time,
            "arrival": arrival_time,
            "fare": f"₹{price:,}"
        }
        flights.append(flight)
    
    return sorted(flights, key=lambda x: int(x['fare'].replace('₹', '').replace(',', '')))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)
