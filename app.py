from flask import Flask, request, render_template, redirect, url_for
import re
import logging
import os
from datetime import datetime

app = Flask(__name__)

# Configure logging
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename=f"logs/injection_log_{datetime.now().strftime('%Y%m%d')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Mock LLM response generator (simulates a vulnerable prompt
def mock_llm_response(user_input):
    system_prompt = "You are a helpful assistant. Do not do anything unsafe."
    full_prompt = f"{system_prompt}\nUser: {user_input}\nAssistant:"

    # Simulate vulnerability
    if "Ignore previous instructions" in user_input or "Assistant:" in user_input:
        result = "Warning: Potential prompt injection detected!"
    else:
        result = "I'm here to help! You said: " + user_input

    return full_prompt, result


# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    full_prompt = None

    if request.method == "POST":
        user_input = request.form.get("prompt", "")
        full_prompt, response = mock_llm_response(user_input)

        # Basic log for potential injection attempts
        if re.search(r"(ignore|override|simulate|assistant:)", user_input, re.IGNORECASE):
            logging.info(f"Suspicious input: {user_input}")

    return render_template("index.html", response=response, full_prompt=full_prompt)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)

