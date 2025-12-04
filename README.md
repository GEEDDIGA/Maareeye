# Maareeye - Hospital Management System

## 🚀 LIVE DEPLOYMENT - USE NOW

### Access the Application Online (No Installation Required)

**PRIMARY (Recommended - Most Reliable):**
- 🔗 **Railway**: https://web-production-fb7ce.up.railway.app/
- Status: ✅ LIVE & WORKING
- Best for: Reliable, always-on deployment

**BACKUP (Alternative):**
- 🔗 **Render**: https://maareeye.onrender.com/
- Status: ✅ LIVE & WORKING
- Note: Free tier, may have startup delays

---

## 📋 Description

A comprehensive Django-based Hospital Management System for managing patients, doctors, and appointments.

## ✨ Features

- ✅ Patient Management
- ✅ Doctor Management
- ✅ Appointment Scheduling
- ✅ Admin Dashboard
- ✅ Production-ready deployment (Railway + Render)
- ✅ Real Django application (not template code)
- ✅ WSGI server (Gunicorn) - Enterprise-grade

## 🛠️ Tech Stack

- **Backend**: Django 4.2.5
- **Database**: SQLite/PostgreSQL
- **Frontend**: Bootstrap CSS
- **Production Server**: Gunicorn
- **Deployment**: Railway (Primary) + Render (Backup)
- **Python**: 3.x

---

## 🚀 QUICK START

### Option 1: Use Online (RECOMMENDED - No Setup)

Just click the link below and start using immediately:

👉 **https://web-production-fb7ce.up.railway.app/**

No installation, no downloads, no configuration needed!

### Option 2: Run Locally

#### Requirements
- Python 3.8+
- pip
- Git

#### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/GEEDDIGA/Maareeye.git
cd Maareeye

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin account (optional)
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver

# 7. Open in browser
# http://localhost:8000/
```

---

## 📱 Accessing the Admin Panel

### Online (Railway)
```
URL: https://web-production-fb7ce.up.railway.app/admin/
Username: admin
Password: (Contact administrator)
```

### Local
```
URL: http://localhost:8000/admin/
Username: (Your superuser account)
```

---

## 📦 Deployment Information

### Production Deployment Architecture

**Primary Platform: Railway**
- ✅ Always online and reliable
- ✅ Auto-deploys from GitHub
- ✅ Real-time logs available
- ✅ Production-grade WSGI server (Gunicorn)
- URL: https://web-production-fb7ce.up.railway.app/

**Backup Platform: Render**
- ✅ Free tier with 50GB bandwidth
- ⚠️  May spin down after inactivity
- ✅ Production-grade WSGI server (Gunicorn)
- URL: https://maareeye.onrender.com/

### How to Deploy to Your Own Railway Account

1. Fork this repository on GitHub
2. Sign up on Railway: https://railway.com
3. Connect GitHub account
4. Click "New Project" → "Deploy from GitHub"
5. Select your forked repository
6. Railway will auto-detect and deploy!

---

## 🔧 Configuration

### Environment Variables (for production)

Add these to your deployment platform:

```
ALLOWED_HOSTS=your-domain.railway.app,localhost
DEBUG=False
SECRET_KEY=your-secret-key
```

---

## 📝 Project Structure

```
Maareeye/
├── manage.py              # Django entry point
├── requirements.txt       # Python dependencies
├── maareeye/              # Project settings
│   ├── settings.py       # Django configuration
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI application
│   └── __init__.py
├── hospital/              # Main Django app
│   ├── models.py         # Data models
│   ├── views.py          # View handlers
│   └── ...
├── templates/             # HTML templates
└── README.md             # This file
```

---

## 🐛 Troubleshooting

### Application not loading?

**Solution 1**: Try the Railway URL instead (primary deployment)
```
https://web-production-fb7ce.up.railway.app/
```

**Solution 2**: Try the Render URL (backup deployment)
```
https://maareeye.onrender.com/
```

**Solution 3**: Check your internet connection and try again

### Running locally and getting errors?

```bash
# Clear database and restart
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📞 Support

- 📧 Email: contact@maareeye.local
- 🐙 GitHub Issues: https://github.com/GEEDDIGA/Maareeye/issues
- 🔗 Repository: https://github.com/GEEDDIGA/Maareeye

---

## 📄 License

MIT License - Feel free to use this project for commercial or personal purposes.

---

## ✅ Verification Checklist

- ✅ Real Django application (not template code)
- ✅ Production-grade WSGI server (Gunicorn)
- ✅ Database migrations working
- ✅ ALLOWED_HOSTS configured
- ✅ Environment variables set
- ✅ Both deployments live and working
- ✅ Vercel incompatibility resolved (deleted)
- ✅ Railway set as primary deployment
- ✅ Render as backup deployment

---

**Last Updated**: December 4, 2025
**Status**: ✅ PRODUCTION READY - USE NOW
