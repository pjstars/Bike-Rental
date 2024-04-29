from bottle import Bottle, run, request, template, static_file

app = Bottle()

# Serve static files (CSS, images, etc.)
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

# Home page route
@app.route('/')
def home():
    return template('home.html')

# Login page route
@app.route('/login')
def login():
    return template('login.html')

# Login form submission route
@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    # Validate username and password
    # Perform login logic
    # Redirect to bike inventory page if login successful
    return '<p>Login successful! Redirecting...</p><script>window.location.href = "/bike_inventory";</script>'

# Bike inventory page route
@app.route('/bike_inventory')
def bike_inventory():
    return template('bike_inventory.html')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
