import requests
import gradio as gr

# 🔑 Replace this with your actual OpenRouter API key
API_KEY = "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"

# 🧠 This function handles all user inputs and history
def get_deepseek_reply(message, history):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost",  # Replace if deploying on a real domain
        "Content-Type": "application/json"
    }

    # 🧱 Construct OpenAI-style message list
    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})
    messages.append({"role": "user", "content": message})

    data = {
        "model": "deepseek-chat",
        "messages": messages
    }

    # 📡 Send request to OpenRouter API
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    # ✅ Return the assistant's reply or show error
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# 💬 Launch Gradio chatbot interface
gr.ChatInterface(
    fn=get_deepseek_reply,
    title="Buddy AI – Powered by DeepSeek",
    chatbot=gr.Chatbot(type="messages")
).launch(share=True)

