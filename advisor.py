import json
import ollama


def generate_recommendations(data, missing_fields=None):

    prompt = f"""
You are a STRICT financial analysis engine.

CRITICAL RULES:
- Do NOT generate any financial numbers not present in the data
- Do NOT estimate percentages, allocations, or valuations
- Do NOT mention market caps, prices, or external statistics
- Do NOT assume investment amounts
- ONLY use values explicitly provided in the input

You are NOT allowed to use external knowledge.

DATA:
{json.dumps(data, indent=2)}

MISSING FIELDS:
{missing_fields}

OUTPUT FORMAT:

## 💡 Recommendations
- Based ONLY on holdings and risk profile (no numbers)

## ⚠ Risks
- Based ONLY on concentration and asset type

## 📌 Data Gaps
- Only list missing fields
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]