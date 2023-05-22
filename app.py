from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    url = request.args.get('url', '/')
    if 'script' in url or 'onload' in url:
        return render_template('403.html'), 403
    return render_template('logout.html', url=url)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
