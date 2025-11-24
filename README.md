# 🤖ChatBot – Your Intelligent AI Assistant
A fully automated AI chatbot built using Streamlit (frontend) and n8n (backend workflow automation).
SmartBot uses Google Gemini AI, n8n AI Agent, and Simple Memory to deliver conversational, context-aware responses.

**🚀 Features**

**✅ 1. AI-Powered Chatbot**
- Real-time responses using Google Gemini Chat Model
- Intelligent multi-step reasoning via n8n AI Agent
- Supports any type of query

**✅ 2. Memory-Enabled Conversations**
- Uses n8n Simple Memory module
- Stores conversation history
- Provides continuous, natural dialogue

**✅ 3. Streamlit Frontend**
- Clean UI for chatting with the bot
- Dynamic chat bubbles (user & bot)
- Webhook communication with n8n backend

**✅ 4. n8n Backend Workflow**

**Your workflow includes:**

**Component**    -   **Description**
- **Webhook**    --->      Receives message from Streamlit
- **AI Agent**	 --->      Processes user input using Gemini
- **Google Gemini Chat Model** -->	LLM powering the responses
- **Simple Memory** -->	    Saves conversation state
- **Respond to Webhook**  ---> Sends response back to Streamlit

**🏗️ Project Architecture**
<img width="558" height="314" alt="Screenshot 2025-11-24 235732" src="https://github.com/user-attachments/assets/024860ab-275b-4c1f-9ebf-5210921870f9" />

**📸 Screenshots**
- **n8n Workflow**
<img width="1159" height="597" alt="Screenshot 2025-11-24 224213" src="https://github.com/user-attachments/assets/e501c154-c2e3-400e-95cf-66be40bfce41" />

**Streamlit UI**
<img width="1096" height="718" alt="Screenshot 2025-11-24 224838" src="https://github.com/user-attachments/assets/6c84921b-846d-4e7b-b69b-63b8befb2597" />


**⚙️ Backend Setup (n8n)**
**1. Import the n8n workflow**
- Open n8n
- Create a new workflow
- Add:
  - Webhook
  - AI Agent
  - Google Gemini Chat
  - Memory
  - Respond to Webhook
  
**Connect nodes exactly as shown in the screenshot**

**3. Set Webhook URL**
- Copy the Production URL from the Webhook node and paste it into the Streamlit app.

**🖥️ Frontend Setup (Streamlit)**

**4. Install dependencies**
- pip install streamlit requests

**5. Run the app**
- streamlit run app.py

**🧠 How It Works**
- User types a query in Streamlit
- Streamlit sends the message to n8n via POST Webhook
- n8n AI Agent processes it using Gemini
- Memory node keeps track of previous messages
- Response is returned back to Streamlit
- UI displays the chatbot message

**📌 Example Conversation**
- **User: hi** 
- **Bot: Hello! How can I assist you today?**

- **User: how are you** 
- **Bot: I'm doing well! How can I help you today?**

**🧩 Tech Stack**
- Python
- Streamlit
- n8n Automation Engine
- Google Gemini Chat Model
- AI Agent Toolkit
