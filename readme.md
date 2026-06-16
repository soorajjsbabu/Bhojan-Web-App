# 🍱 Bhojan — Food Donation Web App

> *"If you can't feed a hundred people, then just feed one."* — Mother Teresa

Bhojan is a web application that makes food donation simple and accessible. People with surplus food after a party or event can donate it from their doorstep — the admin coordinates with a delivery team to get the food to orphanages, old age homes, and people in need.

## About

Built as a final-year B.Sc. Computer Science project at Loyola College (Autonomous), Chennai (2022).

## Features

**User**
- Register and log in via phone number and password
- Submit a food donation form with pickup address and food details
- View donation history with date and time
- View and edit profile
- Connect via LinkedIn and email links in the footer

**Admin**
- View all submitted donations with full details and timestamps
- View, edit, and delete registered users
- Accessible via hardcoded phone number `12345`

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vue.js 2, Buefy, Bulma |
| Backend | Python 3, Flask, Flask-SQLAlchemy, Flask-CORS |
| Database | SQLite3 |
| HTTP Client | Axios |
| Environment | Pipenv |
| IDE | Visual Studio Code |

> All frontend dependencies (Vue, Buefy, Bulma, Axios, FontAwesome) are bundled locally under `lib/` — no internet connection required to run the app.

## Database Schema

**Donations** — `id`, `name`, `phone_number`, `address_line_1`, `address_line_2`, `served_for`, `food_type`, `date_time`, `user_phone` (FK)

**User** — `phone_number` (PK), `name`, `email`

**Registry** — `phone_number` (PK), `password`

## Project Structure

```
Bhojan-Web-App/
├── backend/
│   ├── __init__.py       # App factory, db init, CORS
│   ├── models.py         # SQLAlchemy models (User, Donation, Registry)
│   ├── services.py       # Flask routes / API endpoints
│   └── database.db       # SQLite database (created on first run)
├── lib/                  # Bundled frontend dependencies (offline)
│   ├── css/              # Buefy, Bulma, Material Design Icons
│   ├── js/               # Vue.js, Buefy, Axios
│   └── fontawesome/
├── index.html            # Single-page frontend (Vue.js)
├── Pipfile
└── Pipfile.lock
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/signup` | Register a new user |
| POST | `/login` | Authenticate user |
| POST | `/add_user_profile` | Create user profile |
| PUT | `/update_user` | Update user profile |
| GET | `/userProfile/<phoneNumber>` | Get user profile |
| DELETE | `/delete_user/<phoneNumber>` | Delete a user |
| GET | `/users` | Get all users (admin) |
| POST | `/add_donation/<userPhoneNumber>` | Submit a donation |
| GET | `/userDonations/<userPhoneNumber>` | Get donations by user |
| GET | `/donations` | Get all donations (admin) |

## Getting Started

### Prerequisites

```bash
sudo apt install python3-pip pipenv sqlite3
```

### Installation

```bash
git clone https://github.com/soorajjsbabu/Bhojan-Web-App.git
cd Bhojan-Web-App
pipenv install flask flask-sqlalchemy flask-cors
```

### Initialize the Database

Run once inside the pipenv shell:

```bash
pipenv shell
python3
```

```python
from backend.models import Donation, User
from backend import db, create_app
db.create_all(app=create_app())
```

### Run the App

```bash
pipenv shell
export FLASK_APP=backend
export FLASK_DEBUG=1
flask run
```

Then open `index.html` in your browser. The Flask API runs at `http://localhost:5000`.

To free port 5000 if needed:

```bash
sudo fuser -k 5000/tcp
```

To inspect the database directly:

```bash
sqlite3
sqlite> .open backend/database.db
```

## Future Enhancements

- OTP-based login *(deferred — requires internet connectivity)*
- Monthly email summary sent to donors
- About page describing the cause

## License

This project is licensed under the [MIT License](LICENSE).