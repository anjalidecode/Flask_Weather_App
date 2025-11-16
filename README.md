🌦️ Flask Weather App

A simple weather app using Flask, SQLite, and OpenWeatherMap API. Users can check current weather for any city, add/remove city weather cards, and view saved cities on the home page.

🚀 Features
- Clean HTML/CSS/JS frontend
- Add/remove multiple weather cards
- Live weather data via API
- Flask backend with REST endpoints
- SQLite stores saved cities
- Handles errors and invalid input

🗂️ Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: SQLite
- API: OpenWeatherMap
- Tools: VS Code, venv

📁 Project Structure
Flask_Weather_App/
├── app.py
├── requirements.txt
├── weather.db
├── static/
│   ├── styles.css
└── templates/
    └── index.html

⚙️ Setup
1. Clone:  
   git clone https://github.com/anjalidecode/Flask_Weather_App.git  
   cd Flask_Weather_App
2. Create and activate venv, then install dependencies:  
   python3 -m venv venv  
   source venv/bin/activate (Linux/Mac) / venv\Scripts\activate (Win)  
   pip install -r requirements.txt
3. Add your API key to .env:  
   API_KEY=your_api_key
4. (Optional) Init DB:  
   python  
   from app import init_db  
   init_db()
5. Run:  
   python app.py

🔌 API
- POST /get_weather  — Get weather for a city
- DELETE /delete_city/<city_name>  — Remove city

💾 Database
Table: cities  
- id (int, primary key)  
- name (text, unique)

🤝 Contributions welcome!  
📜 MIT License
