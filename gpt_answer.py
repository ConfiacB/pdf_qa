from openai import OpenAI

def get_answer_from_context(question, context, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Only answer using the document. If not found, say 'Not available'."
            },
            {
                "role": "user",
                "content": f"Document: {context}\n\nQuestion: {question}"
            }
        ]
    )
    return response.choices[0].message.content.strip()
