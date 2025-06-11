import os
import openai
from flask import Flask, request, render_template_string

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

HTML = """
<!doctype html>
<title>LLM Prompt Test</title>
<h1>🧠 Test the AI</h1>
<form method=post>
  <textarea name=prompt rows=6 cols=60 placeholder="Enter your prompt here..."></textarea><br>
  <input type=submit value=Submit>
</form>
<h2>🧾 Response:</h2>
<pre>{{ result }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content
        except Exception as e:
            result = f"[ERROR] {str(e)}"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
