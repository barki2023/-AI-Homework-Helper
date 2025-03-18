import time

def get_answer(question):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    for _ in range(3):  # Try 3 times before failing
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/blenderbot-3B",
            headers=headers,
            json={"inputs": question}
        )
        
        if response.status_code == 503:
            time.sleep(5)  # Wait 5 seconds and retry
            continue
        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code}"

        result = response.json()
        return result[0].get('generated_text', "No valid response received.")

    return "Error: API is unavailable, try again later."
