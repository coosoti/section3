from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    email = 'contact@example.com'  # Default email
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_content = request.form['message']
        # Create a new Message object and add it to the database
        new_message = Message(name=name, email=email, message=message_content)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('contact'))  # Redirect to the same page after form submission
    else:
        return render_template('contact.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)
