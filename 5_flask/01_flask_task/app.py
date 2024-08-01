from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"user_job": "회사원", "name": "강과장"},
        {"user_job": "사진사", "name": "송포토"},
        {"user_job": "프로그래머", "name": "김코딩"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)