from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = '3d88dcb4ba9015fa7d8924664dbaf67a'  # Replace with your generated secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        message = request.form['message']
        
        # Send the message to Telegram and handle the response
        success = send_message_to_telegram(f"Name: {name}\nSubject: {subject}\nMessage: {message}")
        
        if success:
            flash('Message sent successfully!', 'success')
        else:
            flash('Failed to send message. Please try again.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

def send_message_to_telegram(message):
    bot_token = '8048902693:AAGv_onoqAQ3ckyzpkpIfx6XzH-DfvFXEmE'
    bot_chat_id = '1124986155'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": bot_chat_id, "text": message}
    response = requests.post(url, data=data)
    return response.status_code == 200

if __name__ == '__main__':
    app.run(debug=True)