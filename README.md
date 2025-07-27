# FastNotes - FastAPI Notes Web App

FastNotes is a simple yet powerful **Notes management web application** built with **FastAPI** and **MongoDB**.  
It allows you to **create, edit, and delete notes** with a clean and modern web interface.
<img width="1896" height="864" alt="image" src="https://github.com/user-attachments/assets/d0b6cea6-bd3e-4ea6-863d-b39eddc72783" />

---

## 🚀 Features
- Add new notes with a title and description.
- View all notes with timestamps (IST timezone).
- Edit and update existing notes.
- Delete notes.
- Mark notes as **important**.
- Responsive, AI-designed UI using Jinja2 templates.
- Deployed-ready setup with Uvicorn.

---

## 🏗 Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** MongoDB (via PyMongo)
- **Frontend:** HTML, CSS, Jinja2 Templates
- **Deployment:** Uvicorn + Render
- **Other Tools:** Pydantic, datetime with IST timezone

---

## 📂 Project Structure
<pre>
FastAPI/
├── config/
│ └── db.py # MongoDB connection config
│
├── models/
│ └── note.py # Pydantic data model
│
├── routes/
│ └── note.py # CRUD routes for notes
│
├── schemas/
│ └── note.py # MongoDB to dict serialization
│
├── static/ # Static assets (CSS/JS/images)
│
├── templates/ # Frontend HTML templates
│ ├── index.html
│ ├── edit_note.html
│ └── file.html
│
├── index.py # Main FastAPI app
├── requirements.txt # Dependencies
├── .env # Environment variables (Mongo URI, etc.)
└── README.md
</pre>
---

## ⚙️ Installation & Setup
Follow these steps to run the project locally:

### 1. Clone the Repository
    git clone https://github.com/Akshatswami610/Notes-app-using-FastAPI.git
    cd Notes-app-using-FastAPI
### 2. Create Virtual Environment
    python -m venv venv
    source venv/bin/activate   # For Linux/Mac
    venv\Scripts\activate      # For Windows
    
### 3. Install Dependencies
    pip install -r requirements.txt
    
### 4. Configure MongoDB
Create a .env file in the project root and add your MongoDB URI:

    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>
    
### 5. Run the App
    uvicorn index:app --reload

The app will run on: http://127.0.0.1:8000/

---

## 🌍 Live Demo- https://notes-app-dpz8.onrender.com/

## 📝 License
This project is licensed under the MIT License.
Feel free to use and modify it.

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to add features or fix issues:

1. Fork this repo.

2. Create a new branch (feature-new).

3. Commit changes.

4. Create a PR.
