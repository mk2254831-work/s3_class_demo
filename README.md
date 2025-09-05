# Indian Flights Finder

A web application for finding and comparing flights between major Indian cities. Built with Flask backend and vanilla JavaScript frontend.

## Features

- **Flight Search**: Search for flights between major Indian cities
- **Date Selection**: User-friendly date picker for departure and return dates
- **City Autocomplete**: Predefined list of major Indian cities for easy selection
- **Results Sorting**: Sort results by lowest fare or earliest departure time
- **Indian Airlines Filter**: Automatically filters to show only Indian airline flights
- **Responsive Design**: Clean, modern interface with responsive design

## Supported Cities

- Delhi
- Mumbai
- Bangalore
- Chennai
- Kolkata
- Hyderabad
- Pune
- Jaipur
- Goa
- Ahmedabad

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Google Gemini API Key

## Quick Start

```bash
# Navigate to your project directory
cd /Users/mkumar1/Downloads/Personal/AI/ERA_V4/Training/travel_planner

# Install dependencies
pip install -r requirements.txt

# Get your Gemini API key from https://makersuite.google.com/app/apikey
# Update GEMINI_API_KEY in app.py with your actual API key

# Run the application
python3 app.py

# Open browser to http://127.0.0.1:8080
```

## Installation

1. **Clone or download the project:**
   ```bash
   cd /Users/mkumar1/Downloads/Personal/AI/ERA_V4/Training/travel_planner
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Make sure you have updated your Gemini API key** in `app.py`:
   ```python
   GEMINI_API_KEY = "your-actual-gemini-api-key-here"
   ```

2. **Start the Flask application:**
   ```bash
   python3 app.py
   ```

3. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:8080
   ```

4. **The application should now be running locally!**

## Usage

1. **Search for Flights:**
   - Select departure city from the dropdown
   - Select destination city from the dropdown
   - Choose your departure date using the date picker
   - Choose your return date using the date picker
   - Click "Search Flights"

2. **Sort Results:**
   - Use "Sort by Lowest Fare" to find the cheapest flights
   - Use "Sort by Earliest Departure" to find flights departing soonest

3. **View Results:**
   - Results are displayed in a table showing airline, departure/arrival cities, times, and fares
   - Only flights from Indian airlines are shown
   - Top 5 results are displayed, sorted by fare

## Project Structure

```
travel_planner/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML template
├── static/
│   ├── style.css         # CSS styling
│   └── script.js         # JavaScript functionality
└── README.md             # This file
```

## Technical Details

### Backend (Flask)
- **Framework**: Flask with Python
- **API Integration**: Uses Gemini API for flight data
- **Endpoints**:
  - `GET /` - Serves the main page
  - `POST /search` - Handles flight search requests

### Frontend
- **HTML5** with semantic structure
- **CSS3** for responsive styling
- **Vanilla JavaScript** for interactivity
- **Flatpickr** library for date selection

### Dependencies
- `flask` - Web framework
- `requests` - HTTP library for API calls
- `flatpickr` - Date picker (loaded via CDN)

## API Configuration

The application uses **Google Gemini AI API** to generate intelligent flight recommendations. 

### Getting Your Gemini API Key

1. **Visit the Google AI Studio**:
   - Go to https://makersuite.google.com/app/apikey
   - Sign in with your Google account

2. **Create an API Key**:
   - Click "Create API Key"
   - Select your Google Cloud project (or create a new one)
   - Copy your API key

3. **Update the Configuration** in `app.py`:
   ```python
   GEMINI_API_KEY = "your-actual-gemini-api-key-here"
   ```

### How It Works

- **AI-Powered**: Uses Google Gemini to generate realistic flight recommendations
- **Smart Suggestions**: Creates flight options based on typical Indian domestic routes
- **Fallback System**: Includes sample data generation if the API is unavailable
- **Indian Airlines Focus**: Prioritizes popular Indian carriers (IndiGo, Air India, SpiceJet, Vistara, GoAir)

## Development

To run in development mode with auto-reload:
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python3 app.py
```

## Troubleshooting

**Port Already in Use:**
The app now uses port 8080 to avoid conflicts with macOS AirPlay Receiver (which uses port 5000).
```bash
python3 app.py
# App will run on http://127.0.0.1:8080
```

If you want to disable AirPlay Receiver to use port 5000:
- Go to System Preferences → General → AirDrop & Handoff
- Turn off "AirPlay Receiver"

**Module Not Found:**
```bash
pip install -r requirements.txt
```

**Gemini API Errors:**
- Check your Gemini API key in `app.py`
- Ensure you have internet connectivity
- Verify your Google Cloud project has Generative AI API enabled
- Check API quotas and rate limits in Google Cloud Console
- The app includes fallback data generation if API fails

## Future Enhancements

- [ ] Integration with real flight APIs
- [ ] Hotel and accommodation booking
- [ ] Travel itinerary planning
- [ ] Price alerts and notifications
- [ ] User authentication and saved searches
- [ ] Mobile app development
- [ ] Multi-language support

## License

This project is open source and available under the MIT License.

---

**Happy Travel Planning! ✈️**
