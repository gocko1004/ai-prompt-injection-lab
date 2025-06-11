from flask import Flask, request, render_template_string
import json

app = Flask(__name__)

template = """
<h2>🧪 JSON-Layered Prompt Injection Lab</h2>
<form method="POST">
  <textarea name="prompt" rows="8" cols="80">{{ prompt }}</textarea><br>
  <button type="submit">Submit</button>
</form>

{% if result %}
<h3>Result:</h3>
<pre>{{ result }}</pre>
{% endif %}
"""

def mock_llm(prompt: str) -> str:
    # This simulates an insecure LLM reading from structured JSON
    try:
        data = json.loads(prompt)
        system_override = data.get("metadata", {}).get("override", "")
        if system_override:
            return system_override  # Simulates instruction override
        return f"Summarizing: {data.get('user_input', '')}"
    except Exception as e:
        return f"[Error parsing JSON] {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ''
    prompt = ''
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        result = mock_llm(prompt)
    return render_template_string(template, prompt=prompt, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
