# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello from DevOps!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            color: #333;
            padding: 40px;
            text-align: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            display: inline-block;
        }
        h1 {
            color: #007acc;
        }
        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Flask App</h1>
        <p>Welcome to a live demo of Continuous Integration and Deployment!</p>
        <p>This Flask app is deployed via <strong>GitHub Actions</strong> and <strong>Docker</strong>.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
