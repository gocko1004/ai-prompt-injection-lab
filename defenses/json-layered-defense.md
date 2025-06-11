# 🔐 Defense: JSON Layered Input Sanitization

## 🧠 Summary
This test wraps prompts in a JSON layer to isolate instructions and detect dangerous keys or context leakage.

## ✅ Safe Mode ON

Prompt is blocked due to restricted keywords or patterns.

![JSON Safe Mode ON](../images/defenses/json-form-injection-safe-on.png)

## ❌ Safe Mode OFF

Same prompt gets through and reaches the mock LLM backend.

![JSON Safe Mode OFF](../images/attacks/json-form-injection-safe-off.png)
