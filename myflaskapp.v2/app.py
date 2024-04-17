from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., send an email, save to database)
        # For demonstration purposes, we'll just print the data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return redirect(url_for('contact'))  # Redirect to the same page after form submission
    else:
        return render_template('contact.html', email='contact@example.com')

if __name__ == '__main__':
    app.run(debug=True)
