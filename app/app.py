from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

#Additional routes can be defined here

@app.route('/characters')
def characters():
    # Logic to retrieve a list of book characters from the database or any other data source
    characters = ['Harry Potter', 'Katniss Everdeen', 'Frodo Baggins']

    # Render a template with the list of characters
    return render_template('characters.html', characters=characters)

@app.route('/profile/<username>')
def profile(username):
    # Logic to retrieve user information from the database or any other data source based on the provided username
    user = get_user(username)

    # Render a template with the user information
    return render_template('profile.html', user=user)


if __name__ == '__main__':
    app.run()
