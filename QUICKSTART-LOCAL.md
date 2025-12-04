# RUN MAAREEYE LOCALLY - COMPLETE GUIDE

## System Requirements

- **Python**: 3.8 or higher (Check: `python --version`)
- **pip**: Comes with Python
- **Git**: For cloning the repository
- **Terminal/Command Prompt**: For running commands

---

## STEP 1: Download the Code

Open your terminal/command prompt and run:

```bash
git clone https://github.com/GEEDDIGA/Maareeye.git
cd Maareeye
```

If you don't have Git, download the ZIP instead:
1. Go to: https://github.com/GEEDDIGA/Maareeye
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder

---

## STEP 2: Create Virtual Environment

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

---

## STEP 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Django, Gunicorn, and all required packages.

---

## STEP 4: Run Database Migrations

```bash
python manage.py migrate
```

This creates the database and tables.

---

## STEP 5: Create Admin Account (Optional)

To access the admin dashboard:

```bash
python manage.py createsuperuser
```

Follow the prompts to create username and password.

---

## STEP 6: Start the Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

---

## STEP 7: Access the Application

Open your browser and go to:

- **Application**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/ (if you created superuser)

---

## Troubleshooting

### Issue: "python" command not found
**Solution**: Use `python3` instead
```bash
python3 manage.py runserver
```

### Issue: "Permission denied" on activation
**Solution**: On Windows, try:
```bash
venv\Scripts\activate.bat
```

### Issue: Port 8000 already in use
**Solution**: Use a different port:
```bash
python manage.py runserver 8001
```
Then access: http://localhost:8001/

### Issue: "ModuleNotFoundError"
**Solution**: Make sure virtual environment is activated
You should see `(venv)` before your command prompt.

---

## Quick Commands Reference

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver

# Deactivate virtual environment
deactivate
```

---

## What's Inside

- **hospital/**: Main Django application
- **maareeye/**: Project settings
- **templates/**: HTML templates
- **manage.py**: Django command utility
- **requirements.txt**: Python dependencies

---

## Support

- Repository: https://github.com/GEEDDIGA/Maareeye
- Online Version: https://web-production-fb7ce.up.railway.app/
- Backup: https://maareeye.onrender.com/

---

**Status**: Ready to run locally! 🚀
