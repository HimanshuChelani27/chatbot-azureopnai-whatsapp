from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# import openai
from openai import AzureOpenAI

gpt_client = AzureOpenAI(
    api_key="",
    api_version="",
    azure_endpoint=""
)
def ask_openai(prompt):
    try:
        response = gpt_client.chat.completions.create(
            model="gpt-4o",  # Replace with your deployment name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    response = ask_openai(incoming_msg)
    print(response)


    # Implement your logic here
    if 'hello' in incoming_msg:

        msg.body('Hi there! How can I help you today?')
    else:
        msg.body(response)
    # msg.body(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
