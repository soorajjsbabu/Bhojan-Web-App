# Food Donation Web App

> *"If you can't feed a hundred people, then just feed one."* — Mother Teresa

A web application that makes food donation simple and accessible. People with surplus food after a party or event can submit a donation request from their doorstep — the admin coordinates with a delivery team to get the food to orphanages, old age homes, and people in need.

## About

Built as a final-year B.Sc. Computer Science project at Loyola College (Autonomous), Chennai (2022). Refactored to a modern stack with Docker support.

## Features

**Donors**
- Sign up and log in with email and password (Firebase Authentication — no credentials stored in the database)
- Submit a food donation request with pickup address, food type, and number of people served
- View personal donation history

**Admin**
- View all submitted donations with full details, timestamps, and donor email
- Click column headers to sort
- Access controlled by a designated admin email (set via environment variable)

**Security**
- All API routes require a valid Firebase ID token (Bearer token)
- Admin routes additionally verify the token email matches `ADMIN_EMAIL`
- Rate limiting: 10 donation submissions per hour per IP (global: 200/hour, 60/minute)
- Inline auth modal — unauthenticated users can log in without leaving the page

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vue 3, Vite, Tailwind CSS v4, Heroicons |
| Backend | Python 3, Flask, Flask-SQLAlchemy, Flask-CORS, Flask-Limiter |
| Authentication | Firebase Authentication (email/password) |
| Database | SQLite (via Flask-SQLAlchemy) |
| HTTP Client | Axios (with Firebase token interceptor) |
| Container | Docker + Docker Compose, Nginx |

## Database Schema

**Donation** — `id`, `name`, `phoneNumber`, `addLine1`, `addLine2`, `servedFor`, `foodType`, `dateTime`, `userEmail`

## Project Structure

```
food-donation/
├── backend/
│   ├── __init__.py          # App factory, db, CORS, rate limiter, auth decorators
│   ├── models.py            # SQLAlchemy model (Donation)
│   └── services.py          # API routes
├── src/
│   ├── components/
│   │   ├── AuthModal.vue    # Inline login/signup modal
│   │   ├── NavBar.vue
│   │   └── SideDrawer.vue
│   ├── views/
│   │   ├── HomePage.vue     # Landing page with donation form toggle
│   │   ├── LoginPage.vue
│   │   ├── SignupPage.vue
│   │   ├── DonateForm.vue
│   │   ├── HistoryPage.vue
│   │   └── AdminPage.vue
│   ├── stores/auth.js       # Reactive auth state (Firebase-backed)
│   ├── api.js               # Axios instance with token interceptor
│   ├── firebase.js          # Firebase app init
│   └── router/index.js
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── run.py                   # Flask entry point (creates tables on first run)
├── Pipfile
├── .env.example
└── .gitignore
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/add_donation` | User | Submit a donation request |
| GET | `/userDonations` | User | Get the current user's donations |
| GET | `/donations` | Admin | Get all donations |

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- A [Firebase project](https://console.firebase.google.com/) with **Email/Password** sign-in enabled

### Firebase setup

1. Go to Firebase Console → Project Settings → Your Apps → Web app → copy config values
2. Go to Project Settings → Service Accounts → Generate new private key → save as `firebase-service-account.json` in the project root
3. In Firebase Console → Authentication → Sign-in method → enable **Email/Password**
4. Create one user manually in Firebase Console → Authentication → Users — this will be your admin account

### Environment variables

Copy `.env.example` to `.env` and fill in your values:

```env
VITE_FIREBASE_API_KEY=AIzaSy...
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_ADMIN_EMAIL=admin@yourdomain.com

FIREBASE_SERVICE_ACCOUNT_PATH=service-account.json
ADMIN_EMAIL=admin@yourdomain.com
```

### Run with Docker

```bash
docker compose up --build
```

- Frontend: http://localhost
- Backend API: http://localhost:5000

### Run locally (without Docker)

**Backend:**

```bash
pipenv install
pipenv shell
python run.py
```

**Frontend:**

```bash
npm install
npm run dev
```

## Future Enhancements

- Monthly email summary sent to donors
- About page describing the cause
- Push notifications when a donation is picked up

## License

This project is licensed under the [MIT License](LICENSE).
