# live_api_app.py – Updated for OpenAI >= 1.0.0 API syntax

from flask import Flask, request, render_template_string
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")

client = openai.OpenAI(api_key=api_key)

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Live GPT Prompt Injection Test</title>
</head>
<body>
    <h1>🔐 Live GPT Prompt Injection Test</h1>
    <form method="post">
        <textarea name="prompt" rows="6" cols="60">{{ prompt }}</textarea><br>
        <input type="submit" value="Submit">
    </form>
    {% if result %}
    <h3>LLM Response:</h3>
    <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    prompt = ""
    if request.method == 'POST':
        prompt = request.form['prompt']

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content
        except Exception as e:
            result = f"[ERROR] {str(e)}"

    return render_template_string(html_template, result=result, prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
