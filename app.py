from flask import Flask, render_template
from flask import Flask, render_template
app = Flask(__name__)

# Home route
@app.route('/')
def index():
    # Sending data to template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)