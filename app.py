from src.webserver import create_app
app=create_app("weather.db")
app.run(debug=True)
