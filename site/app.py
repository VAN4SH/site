from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'


#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
#app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/specialization')
def specialization():
    return render_template('specialization.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

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
