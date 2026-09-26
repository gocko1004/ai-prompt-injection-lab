# ai-prompt-injection-lab

My first prompt injection lab, from June 2025. I built small Flask apps, threw injection payloads at them, and kept the screenshots and short notes. It is a personal learning lab.

## What it shows

| File | What it does |
|---|---|
| `app.py` | A mock "LLM" page. It builds a prompt from a system line plus user input, answers with a warning when it sees "Ignore previous instructions" or "Assistant:", and logs suspicious words (ignore, override, simulate, assistant:) to `logs/`. |
| `live_api_app.py` | The same test against a real model: the OpenAI API (`gpt-4`) behind a one-line system prompt. |
| `labs/json-layered/app.py` | A mock that reads a JSON payload and obeys a hidden `metadata.override` field, to show that structured input is not the same as safe input. |
| `attacks/`, `defenses/`, `reports/` | Notes on HTML comment injection, JSON layered injection and a pirate persona takeover. |
| `images/` | Screenshots of the attempts, successful and blocked, including a role override through Markdown. |

![HTML comment injection against a different build of the mock app, with Safe Mode off](images/attacks/html-comment-injection-demo.png)

## Why it matters

Any app that pastes user text, web pages or JSON into a prompt gives that text a say in what the model does. These tests are the simplest version of that problem, which is a good place to start.

## Stack

Python, Flask, the OpenAI Python SDK (v1 syntax), python-dotenv. Screenshots were taken on Kali Linux.

## How to run

```bash
git clone https://github.com/gocko1004/ai-prompt-injection-lab.git
cd ai-prompt-injection-lab
python3 -m venv venv
source venv/bin/activate
pip install flask openai python-dotenv

python3 app.py                     # mock app, http://127.0.0.1:5000
python3 labs/json-layered/app.py   # JSON lab, http://127.0.0.1:5002
python3 live_api_app.py            # live model, needs OPENAI_API_KEY in a .env file
```

`requirements.txt` only lists Flask, so install the other two packages by hand. `live_api_app.py` and the JSON lab start in debug mode on `0.0.0.0`, which exposes the Flask debugger to your network. Change the host to `127.0.0.1` before running them anywhere but a throwaway VM.

## Known gaps

- Most tests run against a mock function, not a model. Only `live_api_app.py` calls a real one.
- Some screenshots, including the one above, show a "Safe Mode" toggle. That build is not in this repo. The `app.py` here answers two exact phrases with a warning and logs suspicious words. It has no Safe Mode.

## What I learned

- A word filter is a weak defense. Blocking "ignore" stops the textbook payload, but the same intent can be reworded, nested in JSON or hidden in an HTML comment.
- Structured input needs the same distrust as free text. The JSON lab shows a single hidden field taking over the reply.
- Mock tests teach the idea, not how a real model behaves. My later lab, [damn-vulnerable-llm-app](https://github.com/gocko1004/damn-vulnerable-llm-app), tests a real model with retrieval and dated write-ups.

## Personal lab note

Built on my own machine to learn. Not production work and not a client engagement.

More about my IT and security learning: [gocepetrov.com/security-and-it](https://www.gocepetrov.com/security-and-it)
