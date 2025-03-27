# 📄 **README: Flask Chatbot with Twilio and Azure OpenAI**

This project implements a **Flask-based chatbot** that integrates with **Twilio** for receiving and responding to **WhatsApp/SMS messages**, and uses **Azure OpenAI** to generate dynamic responses.

---

## 📌 **Project Structure**
```
.
├── main.py          # Main Flask application
└── README.md        # Documentation
```

---

## 📚 **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **Flask** (`pip install Flask`)
- **Twilio** (`pip install twilio`)
- **Azure OpenAI SDK** (`pip install openai`)
- **ngrok** (for local development webhook)

---

## ⚙️ **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone https://github.com/HimanshuChelani27/chatbot-azureopnai-whatsapp.git
cd your-repo
```

### 2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure Azure OpenAI and Twilio**
1. **Azure OpenAI Configuration:**
   - Sign up for **Azure OpenAI**: https://azure.microsoft.com/en-us/products/cognitive-services/openai-service
   - Get your:
     - `api_key`
     - `api_version`
     - `azure_endpoint`
   - Update these details in the `gpt_client` initialization in `main.py`.

2. **Twilio Configuration:**
   - Sign up for **Twilio**: https://www.twilio.com/try-twilio
   - Set up a **WhatsApp Sandbox** (for testing): https://www.twilio.com/docs/whatsapp/sandbox
   - Ensure your Twilio account is ready to handle webhooks.

---

## ▶️ **Run the Flask App**
```bash
python main.py
```
By default, Flask will run on:  
`http://localhost:5000`

---

## 🌐 **Expose Flask App to the Internet Using ngrok**
1. **Install ngrok** (if not installed):
   - Download from: https://ngrok.com/download
2. **Start ngrok**:
   ```bash
   ngrok http 5000
   ```
3. **Copy the Forwarding URL**:
   You’ll see output like:
   ```
   Forwarding    https://your-ngrok-url.ngrok.io -> http://localhost:5000
   ```
   Use the `https://your-ngrok-url.ngrok.io` URL for the next step.

---

## 🔔 **Set Up Twilio Webhook**
1. Go to the [Twilio Console](https://console.twilio.com).
2. Navigate to:
   **Messaging** → **WhatsApp Sandbox** (or your messaging service).
3. In the **Webhook URL** field:
   - Enter: `https://your-ngrok-url.ngrok.io/webhook`
4. Ensure you select **HTTP POST** as the method.

---

## 📱 **Test the Chatbot**
1. Send a WhatsApp or SMS message to your **Twilio number**.
2. If the message contains **"hello"**, you will get a custom response.
3. For other messages, the **Azure OpenAI** model will respond dynamically.

---

## 🛠️ **Customize the Chatbot**
Modify the logic inside:
```python
if 'hello' in incoming_msg:
    msg.body('Hi there! How can I help you today?')
else:
    msg.body(response)
```
- Add new conditions for different keywords.
- Improve the **Azure OpenAI** prompt to adjust the assistant's tone.

---

## 📊 **Example Interaction**
1. **User:** `"hello"`
   - **Bot:** `"Hi there! How can I help you today?"`
   
2. **User:** `"Tell me a joke"`
   - **Bot:** `"Why don’t skeletons fight each other? They don’t have the guts!"`

---

## 📌 **Troubleshooting**
1. **ngrok Not Working?**
   Ensure `ngrok` is running and the **webhook URL** is updated in Twilio.
   
2. **Azure OpenAI Errors?**
   - Verify your **API key**, **endpoint**, and **deployment name**.
   - Ensure you have access to **gpt-4o** or the model you’re using.

3. **No Response in WhatsApp?**
   - Check Flask logs for errors.
   - Ensure your Twilio webhook is correctly set and points to `/webhook`.

---

## 🧹 **Stopping the Services**
- Stop Flask using `CTRL+C`.
- Close ngrok with `CTRL+C`.

---

## 📜 **License**
This project is licensed under the **MIT License**.

