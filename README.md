# 🤖 LiveKit AI Car Call Centre
# AI Car Service Center Voice Assistant

## Overview

This project implements an AI-powered voice assistant tailored for a car service center. It allows users to interact with an intelligent agent through a browser using real-time audio and multimodal LLM responses capable of handling typical service-related tasks: retrieving car information via VIN, creating new vehicle profiles, and even initiating appointment scheduling. The assistant is built using Python and LiveKit's real-time agent infrastructure and is connected to a custom React frontend.

## ✨Features

* Real-time two-way voice and text based communication 🔊
* LLM-powered voice agent for car help 💡
* Vehicle profile lookup and creation 🔎
* Persistent data storage in SQLite🗄️
* Clean React UI with modal-based voice interface 🎨
* LiveKit Agent integration with event-based control flow 🖥️

---

## 🛠️Tech Stack

### Backend:

* **Python 3.12**
* **🎤LiveKit Agents SDK (Voice Rooms, WebRTC)**
* **🧠OpenAI LLM via livekit-plugins-openai**
* **🌐FastAPI for backend API (for future expansion/token issuing)**
* **🎛️ Python Async Agent Workers**    
* **🗄️SQLite (lightweight DB)**
* **🧪 dotenv for environment configuration**

### Frontend:

* **React (Vite)**
* **LiveKit React Components**
* **Custom CSS**

---

## 🚀 How to Run

### Architecture Diagram

```
User <--> Frontend (React + LiveKit Components)
     <--> LiveKit Cloud (WebRTC Audio Streaming)
     <--> Backend Agent (Python, OpenAI Model + Tools)
                         |
                         +-- SQLite Database
```

1. User clicks "Talk to an agent" on the frontend and provides their name.
2. The frontend connects to LiveKit using a token and opens an audio room.
3. The backend LiveKit agent joins the room and begins listening.
4. The assistant responds with a welcome prompt and either:

   * Prompts the user for their VIN to look up a vehicle
   * Guides them through creating a new vehicle profile
5. Vehicle details are stored/retrieved in SQLite
6. The assistant continues to answer queries or trigger backend logic (e.g., schedule appointments).

---

## 🧠Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd LiveKit-AI-Car-Call-Centre-main
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv ai
source ai/Scripts/activate  # Windows
# OR
source ai/bin/activate     # macOS/Linux
```

### 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file:

```
LIVEKIT_WS_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
OPENAI_API_KEY=your_openai_api_key
```
### 5. Start FastAPI Token Server

```
python -m uvicorn server:app --reload --port=5001
```

### 6. Run Backend Agent

```bash
cd backend
python agent.py dev
```

### 7. Run Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

Visit: `http://localhost:5173`

---

## File Structure

```
LiveKit-AI-Car-Call-Centre-main/
├── backend/
│   ├── agent.py             # Main LiveKit agent logic
│   ├── api.py               # LLM callable tools (create/lookup vehicles)
│   ├── database_driver.py   # SQLite interaction layer
│   ├── prompts.py           # Prompt templates
│   ├── server.py            # Optional: FastAPI backend server
│   └── .env                 # Environment variables
├── frontend/
│   ├── App.jsx              # Main UI layout
│   ├── components/          # LiveKit modal + assistant UI
│   ├── app.css              # Custom styles
│   └── index.css
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🗃️ Database Testing

```

To verify that agent interactions are saved:

Check the logs inside assistant_fnc.py where user queries are processed.

You can add print/log statements or connect a database (e.g., SQLite/PostgreSQL).

If using a DB, ensure you observe entries with timestamps and user conten

```


## Key Learnings / Why Each Step Was Done

1. **LiveKit Cloud + Agents**: For ultra-low-latency real-time communication (used by OpenAI itself).
2. **RealtimeModel from OpenAI Plugin**: Enabled fast response time and multimodal support.
3. **JobContext Pattern**: Used to connect agents to rooms on LiveKit and monitor session events.
4. **LLM Callable Tools**: Added custom logic to lookup cars or create profiles using SQLite.
5. **Event Hooks**: Used `user_speech_committed` to conditionally branch logic (e.g., has car or not).
6. **SQLite**: Lightweight local DB to simulate realistic car service record lookup.
7. **React + LiveKit Components**: Provides clean, responsive UI for engaging with the assistant.

---

## Hosting / Demo (Optional)

If hosted online:

```
Currently runs locally. Hosting requires:

Deploying FastAPI on Render/Vercel

Linking LiveKit cloud instance

Hosting Vite frontend on Netlify
```

---