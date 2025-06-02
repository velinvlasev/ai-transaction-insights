import openai
import os

# Load your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_transaction(description):
    prompt = f"Classify this bank transaction description into a category like 'Food Delivery', 'Subscription', 'Coffee', 'Tech Services', etc.\n\nTransaction: '{description}'\nCategory:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=20
    )

    return response.choices[0].message.content.strip()