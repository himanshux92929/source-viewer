from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    source_code = None
    target_url = ''
    error = None

    if request.method == 'POST':
        target_url = request.form.get('url')
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
        
        try:
            # We use a User-Agent header so websites think we are a standard browser
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(target_url, headers=headers, timeout=10)
            
            # Get the text content
            source_code = response.text
        except requests.exceptions.RequestException as e:
            error = f"Could not fetch {target_url}. Error: {str(e)}"

    return render_template('index.html', source_code=source_code, url=target_url, error=error)

if __name__ == '__main__':
    app.run(debug=True)
