Here’s a complete **Django Setup Manual** in Markdown format, designed to help you set up Django from scratch on Windows. You can keep this for future reference:

---

# Django Setup Manual (Windows)

## 1. **Install Prerequisites**

### 1.1 **Install Python**
   - Download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
   - During installation, ensure **"Add Python to PATH"** is checked.

### 1.2 **Install Visual Studio Code (VS Code)**
   - Download and install [VS Code](https://code.visualstudio.com/Download).
   - Install the **Python extension** in VS Code:
     - Go to Extensions (left sidebar).
     - Search for **Python** and install the one by Microsoft.

---

## 2. **Setting Up Django Project**

### 2.1 **Create a New Project Folder**
   - Create a folder for your Django project. You can do this manually or via terminal:
     ```bash
     mkdir my_django_project
     cd my_django_project
     ```

### 2.2 **Create and Activate a Virtual Environment**
   - In VS Code terminal, run:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **For Command Prompt**:
       ```bash
       venv\Scripts\activate
       ```
     - **For PowerShell**:
       ```bash
       .\venv\Scripts\Activate
       ```
   - Your terminal should show `(venv)` at the beginning, indicating that the virtual environment is activated.

### 2.3 **Install Django**
   - Once the virtual environment is activated, install Django:
     ```bash
     pip install django
     ```

### 2.4 **Verify Django Installation**
   - Ensure Django is installed properly by checking its version:
     ```bash
     python -m django --version
     ```

---

## 3. **Creating and Configuring Your Django Project**

### 3.1 **Create Django Project**
   - Create your first Django project by running:
     ```bash
     django-admin startproject myproject
     cd myproject
     ```

### 3.2 **Run Development Server**
   - Start the development server:
     ```bash
     python manage.py runserver
     ```
   - Open your browser and visit `http://127.0.0.1:8000/` to see the Django welcome page.

---

## 4. **Setting Up Static Files and Templates**

### 4.1 **Create Static Directory**
   - Inside your project folder (next to `manage.py`), create a `static` directory to store your static files (CSS, JS, images):
     ```bash
     mkdir static
     ```
   - In the settings file (`myproject/settings.py`), add the following line:
     ```python
     STATIC_URL = '/static/'
     STATICFILES_DIRS = [BASE_DIR / "static"]
     ```

### 4.2 **Create Templates Directory**
   - Inside your project folder, create a `templates` directory to store your HTML files:
     ```bash
     mkdir templates
     ```
   - In `settings.py`, add this line:
     ```python
     TEMPLATES[0]['DIRS'] = [BASE_DIR / "templates"]
     ```

---

## 5. **Create a Django App**

### 5.1 **Create a New App**
   - To create an app, run:
     ```bash
     python manage.py startapp myapp
     ```
   - Add the app to your project by including it in the `INSTALLED_APPS` section of `settings.py`:
     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'myapp',  # Add this line
     ]
     ```

---

## 6. **Create and Configure Superuser**

### 6.1 **Create a Superuser**
   - To create a superuser for accessing the Django admin panel, run:
     ```bash
     python manage.py createsuperuser
     ```
   - Follow the prompts to set the username, email, and password.

### 6.2 **Access Django Admin**
   - After the superuser is created, you can access the Django admin panel by visiting:
     ```http
     http://127.0.0.1:8000/admin
     ```
   - Log in with the credentials of the superuser you just created.

---

## 7. **Version Control with Git**

### 7.1 **Initialize Git Repository**
   - In the root of your project (where `manage.py` is located), initialize a Git repository:
     ```bash
     git init
     ```

### 7.2 **Create .gitignore File**
   - Create a `.gitignore` file in your project’s root directory to avoid committing unnecessary files like the virtual environment. Add the following:
     ```bash
     venv/
     __pycache__/
     *.pyc
     *.pyo
     *.pyd
     db.sqlite3
     ```

### 7.3 **Stage and Commit Files**
   - Add all files to Git:
     ```bash
     git add .
     ```
   - Commit your changes:
     ```bash
     git commit -m "Initial commit"
     ```

### 7.4 **Push to GitHub**
   - Create a new repository on GitHub.
   - Copy the repository URL (e.g., `https://github.com/username/my_django_project.git`).
   - Link the remote repository:
     ```bash
     git remote add origin https://github.com/username/my_django_project.git
     ```
   - Push the local changes to GitHub:
     ```bash
     git push -u origin master
     ```

---

## 8. **Final Steps**

### 8.1 **Migrate Database**
   - Run migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

### 8.2 **Create a Superuser**
   - Run this to create the Django superuser (if not done earlier):
     ```bash
     python manage.py createsuperuser
     ```

### 8.3 **Run the Server**
   - Run the development server again to see changes:
     ```bash
     python manage.py runserver
     ```
   - Visit `http://127.0.0.1:8000` to check your site.

---

## 9. **Optional: Adding Custom Apps**

### 9.1 **Create New App**
   - To create a new app within your Django project, run:
     ```bash
     python manage.py startapp app_name
     ```

### 9.2 **Register App in settings.py**
   - Add the new app to `INSTALLED_APPS` in `settings.py`:
     ```python
     INSTALLED_APPS = [
         ...
         'app_name',
     ]
     ```

---

This manual covers the basic setup for a Django project on Windows. Keep it handy for future reference. If you need any more detailed explanations or help with any specific part of the setup, let me know!