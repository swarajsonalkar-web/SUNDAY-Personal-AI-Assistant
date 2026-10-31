# SUNDAY — Personal AI Assistant

A local-first personal assistant dashboard designed to help manage everyday tasks, capture ideas, and organize personal productivity.

**Built by Swaraj Sonalkar**

## Overview

SUNDAY is a personal AI assistant project focused on creating a centralized digital workspace. It combines task management, note-taking, and an assistant interface in a clean, modern dashboard.

The current version provides a local demonstration assistant with persistent data storage using SQLite.

## Features

- Task creation and management
- Mark tasks as completed
- Delete existing tasks
- Personal notes management
- Assistant chat interface
- SQLite database integration
- REST API architecture
- Responsive dashboard interface

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API |
| SQLite | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Frontend functionality |

## Project Structure

```text
SUNDAY/
├── app.py
├── sunday.db
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/swarajsonalkar-web/SUNDAY.git
cd SUNDAY
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment**

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Start the server**

```bash
uvicorn app:app --reload --port 8001
```

Open: http://127.0.0.1:8001

## Future Improvements

- Integration with a generative AI model
- Voice input and output
- Wake-word activation
- Advanced long-term memory
- Android application integration
- Smart productivity modes
- Secure authentication

## Developer

**Swaraj Sonalkar**

- GitHub: https://github.com/swarajsonalkar-web
- LinkedIn: https://github.com/swarajsonalkar-web
- Email: swarajsonalkar99@gmail.com

---

*Building a personal digital assistant, one feature at a time.*
