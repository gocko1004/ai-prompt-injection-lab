# 🧪 AI Prompt Injection Lab — 2025 Portfolio Project

This lab demonstrates modern, real-world prompt injection vulnerabilities and defenses, with hands-on examples using LLMs and Flask.

---

## ✅ Completed Modules (so far)

### 🔹 Setup
- [x] Kali Linux environment with Python virtualenv
- [x] Flask app running locally
- [x] Basic OpenAI API config prepared (GPT-4 tested)

### 🔹 Attacks Implemented
- ✅ HTML comment injection (`<!-- ignore rules -->`)
  - ![Demo](images/attacks/html-comment-injection-demo.png)
- ✅ JSON-form bypass attempt (Safe Mode OFF)
  - ![Demo](images/attacks/json-form-injection-safe-off.png)

### 🔹 Defenses Tested
- ✅ JSON input filtering with Safe Mode ON
  - ![Blocked](images/defenses/json-form-injection-safe-on.png)

---

## 📷 Image-Backed Reports

All attacks and defenses have dedicated `.md` reports with screenshots in:

- `/attacks/`
- `/defenses/`
- `/images/`

---

## 🔄 Next Phase (In Progress)
- Live API test with OpenAI GPT-4
- Memory context leakage exploration
- Detection and alerting mechanisms (AI firewall)
