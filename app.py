from flask import Flask, render_template, redirect, request, session, url_for
import os
from utils.auth import register_user, validate_user
from modules.crop import get_crop_recommendation
from modules.weather import get_weather_forecast
from modules.market import get_market_prices
from modules.disease import predict_disease
from modules.scanner import process_leaf_image
from werkzeug.utils import secure_filename

# Create the Flask app
app = Flask(__name__)
app.secret_key = "agro_secret_key"  # Keep this secret in production

# Set upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Landing route
@app.route('/')
def index():
    if 'user' in session:
        return redirect('/home')
    return redirect('/login')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.form['username']
        pwd = request.form['password']
        if validate_user(uid, pwd):
            session['user'] = uid
            return redirect('/home')
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uid = request.form['username']
        pwd = request.form['password']
        success, message = register_user(uid, pwd)
        if success:
            return redirect('/login')
        else:
            return render_template('signup.html', error=message)
    return render_template('signup.html')

# Home Page
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('home.html', user=session['user'])

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# Crop Recommendation
@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        season = request.form['season']
        soil = request.form['soil']
        crop = get_crop_recommendation(season, soil)
        return render_template('crop.html', result=crop)
    return render_template('crop.html')

# Weather Forecast
@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        forecast = get_weather_forecast(city)
        return render_template('weather.html', result=forecast)
    return render_template('weather.html')

# Market Prices
@app.route('/market', methods=['GET', 'POST'])
def market():
    if request.method == 'POST':
        crop = request.form['crop']
        prices = get_market_prices(crop)
        return render_template('market.html', result=prices)
    return render_template('market.html')

# Disease Predictor
@app.route('/disease', methods=['GET', 'POST'])
def disease():
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        prediction = predict_disease(symptoms)
        return render_template('disease.html', result=prediction)
    return render_template('disease.html')

# Leaf Scanner
@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('scanner.html', error="No file part.")
        file = request.files['image']
        if file.filename == '':
            return render_template('scanner.html', error="No selected file.")
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        result = process_leaf_image(filepath)
        return render_template('scanner.html', result=result, image=filename)
    return render_template('scanner.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
