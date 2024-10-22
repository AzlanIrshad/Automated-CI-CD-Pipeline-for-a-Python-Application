from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for contacts
contacts = []

# Route for homepage - display all contacts
@app.route('/')
def home():
    return render_template('index.html', contacts=contacts)

# Route to add a new contact
@app.route('/new', methods=['GET', 'POST'])
def new_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        contacts.append({'name': name, 'phone': phone})
        return redirect(url_for('home'))
    return render_template('new_contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
