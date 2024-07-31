from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user')
def index():
    users = [
        {"user_job": "traveler", "name": "Alex"},
        {"user_job": "photographer", "name": "Sam"},
        {"user_job": "gourmet", "name": "Chris"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)