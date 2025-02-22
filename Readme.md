# GenAI - AI-Powered Poetry Generator

**GenAI** is an AI-powered poetry generator that leverages **LangChain**, **FastAPI**, and **Streamlit** to generate 100-word poems on any given topic using **LLAMA2** via `langchain_ollama`. This project showcases how generative AI models can be used to create creative content and provides a simple interface for users to interact with an AI-driven poetry engine.

## **Project Overview**
### **Use Cases**
- 📜 **Creative Writing**: Generate AI-assisted poetry for writers, bloggers, or hobbyists.
- 🎓 **Educational Tool**: Help students learn about poetry structures and styles.
- 🎭 **Entertainment & Fun**: Get unique AI-generated poems on any topic instantly.
- 📝 **Content Inspiration**: Writers can use AI-generated poems for brainstorming ideas.

### **What This Project Uses**
- **FastAPI** - Backend API for handling user requests.
- **LangChain** - Framework for building AI-driven applications.
- **LLAMA2 (via langchain_ollama)** - LLM used for generating poems.
- **Streamlit** - Frontend UI to interact with the model.
- **Uvicorn** - ASGI server for running FastAPI applications.
- **dotenv** - Loads environment variables for API key management.

---

## **Installation & Setup**

### **1. Clone the Repository**
```bash
cd /your/project/directory
```

### **2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Environment Variables**
Create a `.env` file in the project directory and add:
```env
LANGCHAIN_API_KEY=your_actual_api_key_here
```
Alternatively, set it manually in the terminal:
```bash
export LANGCHAIN_API_KEY=your_actual_api_key_here  # Mac/Linux
set LANGCHAIN_API_KEY=your_actual_api_key_here  # Windows
```

---

## **How to Run the Application**

### **Step 1: Start the FastAPI Server**
```bash
python app.py
```

You should see:
```
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```

Test the API:
```bash
curl -X 'POST' \
  'http://localhost:8000/poem/invoke' \
  -H 'Content-Type: application/json' \
  -d '{"input": {"topic": "nature"}}'
```
If successful, the API will return a **100-word poem**.

### **Step 2: Start the Streamlit Frontend**
```bash
streamlit run client.py
```

Then, open the browser and go to:
```
http://localhost:8501
```
Enter a topic, and the app will generate a poem using the FastAPI backend.

---

## **Troubleshooting**

### **1. FastAPI Not Running?**
- Ensure **port 8000 is free**:
  ```bash
  lsof -i :8000  # Mac/Linux
  ```
  If another process is using port 8000, kill it:
  ```bash
  kill -9 <PID>
  ```
- Try running FastAPI on another port:
  ```python
  uvicorn.run(app, host="localhost", port=8001)
  ```

### **2. API Call Fails with 'Connection Refused'?**
- Restart FastAPI and check logs:
  ```bash
  python app.py
  ```
- Ensure FastAPI is running before launching Streamlit.

### **3. Streamlit Page is Blank?**
- Run Streamlit in debug mode:
  ```bash
  streamlit run client.py --logger.level=debug
  ```
- Check for errors in the **browser console (F12 → Console Tab)**.
- Try running on a different port:
  ```bash
  streamlit run client.py --server.port 8502
  ```

---

## **Next Steps**
✅ **Enhance the AI Model** by fine-tuning prompts for better poetry generation.
✅ **Add More Features** like different poetry styles, rhyming schemes, or multilingual support.
✅ **Deploy to Cloud** using Render, Railway, or AWS Lambda for global access.

---

### **Author**
Developed by **Sowmya Buruju**.

---

Enjoy using **GenAI**! 🚀

