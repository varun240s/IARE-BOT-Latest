"""Simple web server for Heroku health checks."""
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return "IARE Bot is running!", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
