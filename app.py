from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# === MOCK LLM RESPONSE FUNCTION ===
def mock_llm(prompt):
    if "ignore previous" in prompt.lower():
        return "[WARNING] Prompt injection detected in mock response."
    return f"[MOCK LLM RESPONSE]: Summary of: {prompt[:100]}..."

# === BASIC INPUT SANITIZATION ===
def sanitize_input(user_input):
    cleaned = re.sub(r'(ignore|delete|override|system message|inject)', '[BLOCKED]', user_input, flags=re.I)
    return cleaned

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    result = None
    safe_mode = request.args.get("safe", "0") == "1"

    if request.method == 'POST':
        user_input = request.form['user_input']
        prompt = sanitize_input(user_input) if safe_mode else user_input
        result = mock_llm(prompt)

    return render_template_string('''
        <h1>🛡️ AI Web App Prompt Injection Lab</h1>
        <form method="post">
            <textarea name="user_input" rows="5" cols="60" placeholder="Enter text for LLM to summarize..."></textarea><br>
            <input type="submit" value="Send to AI">
        </form>
        <p><a href="/?safe={{ '0' if safe_mode else '1' }}">
        Toggle Safe Mode: {{ 'ON' if safe_mode else 'OFF' }}</a></p>
        {% if result %}<h3>Result:</h3><pre>{{ result }}</pre>{% endif %}
    ''', result=result, safe_mode=safe_mode)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

