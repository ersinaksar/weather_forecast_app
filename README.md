# Weather Forecast App 🌦️

Welcome to the Weather Forecast App! This application provides real-time weather forecasts using the OpenWeatherMap API.
It allows you to fetch weather data, view charts, and store data in a local database for quick access.

### Features ✨

- **Real-Time Weather Data**: Fetch current, minutely, hourly, and daily weather forecasts.
- **Interactive Map**: Select a location on the map to get weather data.
- **Weather Charts**: Visualize hourly and daily weather data with interactive charts.
- **Local Storage**: Store weather data in a local SQLite database to reduce API calls.
- **Time-Sensitive Data**: Automatically update weather data if it's older than 10 minutes.
- **Admin Panel**: Manage and view stored weather data through Django's admin interface.

### Technologies Used 🛠️

- **Django**: The web framework used to build the application.
- **Django REST Framework**: For building the API endpoints.
- **OpenWeatherMap API**: To fetch real-time weather data.
- **Plotly**: For creating interactive weather charts.
- **Google Maps API**: For the interactive map to select locations.
- **SQLite**: The database used to store weather data locally.

### Installation Guide 🚀

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables** Create a .env file in the project root and add your 

   OpenWeatherMap API key:
   ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key
   
5. **Run Migrations**
   ```bash
   python manage.py migrate

6. **Start the Development Server**
   ```bash
   python manage.py runserver

### Usage 📝

1. **Access the Application**

   Open your browser and go to `http://127.0.0.1:8000/`.


2. **Get Weather Data**
- Click on the map to select a location.
- Fill in the latitude, longitude, and data type (current, minutely, hourly, daily).
- Click "Get Weather" to fetch and display the weather data.

3. **View Weather Charts**
- Fill in the latitude, longitude, and select hourly or daily forecast.
- Click "Get Weather Chart" to generate and view the interactive weather chart.

### API Endpoints 📡
- **Get Weather Data**
   ```bash
  GET /api/weather/?lat={lat}&lon={lon}&data_type={data_type}
- **Get Weather Chart**
   ```bash
   GET /chart/?lat={lat}&lon={lon}&data_type={data_type}

### Admin Panel 🛠️
1. **Access the Admin Panel**

   Go to `http://127.0.0.1:8000/admin/ and log in with your admin credentials.


2. **Manage Weather Data**
- View and manage stored weather data.
- Check timestamps and data types to ensure the data is up-to-date.

### Contributing 🤝
We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request with a detailed description of your changes.

### License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact 📧
If you have any questions or need assistance, feel free to contact me at [ersinaksar@yandex.com](mailto:ersinaksar@yandex.com).

Thank you for using the Weather Forecast App! We hope you find it useful. 🌤️🌧️☀️ 