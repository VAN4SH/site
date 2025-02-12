from flask import Flask, render_template, request, redirect, flash
#from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
#app.config['MAIL_PASSWORD'] = 'your_email_password'

#mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/specialization')
def specialization():
    return render_template('specialization.html')

@app.route('/reviews')
def news():
    return render_template('reviews.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/consultation')
def about():
    return render_template('consultation.html')

@app.route('/avto')
def avto():
    return render_template('avto.html')

@app.route('/administrativnie')
def administrativnie():
    return render_template('administrativnie.html')

@app.route('/arbitr')
def arb():
    return render_template('arbitr.html')

@app.route('/citizens')
def cit():
    return render_template('citizens.html')

@app.route('/consumers')
def con():
    return render_template('consumers.html')


@app.route('/criminal')
def crim():
    return render_template('criminal.html')

@app.route('/family')
def fam():
    return render_template('family.html')

@app.route('/housing')
def hous():
    return render_template('housing.html')

@app.route('/inheritance')
def inher():
    return render_template('inheritance.html')

@app.route('/labor')
def lab():
    return render_template('labor.html')

@app.route('/military')
def milit():
    return render_template('military.html')

@app.route('/tax')
def tax():
    return render_template('tax.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    message_content = request.form['message']
    msg = Message('Обращение с сайта Legal Guard', 
                  sender=app.config['MAIL_USERNAME'], 
                  recipients=['your_email@gmail.com'])
    msg.body = f"Сообщение от: {email}\n\n{message_content}"
    
    try:
        mail.send(msg)
        flash('Ваше сообщение отправлено. Мы свяжемся с вами в ближайшее время!', 'success')
    except:
        flash('Ошибка при отправке сообщения. Попробуйте снова!', 'danger')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
