# **Pinterest Clone (Django)**  
This project is a **Pinterest clone coding** aimed at **learning Django** and **enhancing development skills**.  
During development, **AWS and Docker** were utilized to set up the deployment environment.  

### ▶ [Watch Demo](https://1drv.ms/v/c/699aeea76de52c4e/EWZu_ZqWucFKtWJSf0jS9uoBv1XVUpB_uvg6pFARIHmf7g?e=8m2tOK)

## **📌 Key Features**  
- **User Account Management** (Sign-up, Login, Logout, Profile Management)  
- **Post Management** (Image Upload, Edit, Delete)  
- **Comment Feature** (Write and Delete Comments on Posts)  
- **Project System** (Link Posts to Specific Projects)  
- **Subscription Feature** (Subscribe to Projects and View Posts from Subscribed Projects)  

---

## **⚠️ Current Issues & Areas for Improvement**  
This project was developed for learning purposes and requires the following improvements:  

1. **Issue: Users can write posts without logging in**  
   - Currently, users can access the post creation page without logging in.  
   - However, when submitting a post, the writer field is left empty, causing an error and preventing the post from being saved correctly.  

2. **Issue: Users are redirected to the previous page after login**  
   - For example, after signing up and logging in, the user is redirected back to the sign-up page instead of the expected destination.  

---

## **🚀 How to Run the Project**  
### **1️⃣ Set Up the Environment**  
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # (For Windows: venv\Scripts\activate)

# Install required packages
pip install -r requirements.txt
```

### **2️⃣ Configure Environment Variables**  
Create a `.env` file in the project root and add the following:  
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### **3️⃣ Run Database Migrations**  
```bash
python manage.py migrate
```

### **4️⃣ Start the Server**  
```bash
python manage.py runserver
```
- Open `http://127.0.0.1:8000/` in your browser.  

---

## **📂 Project Directory Structure**  
```
PinterestClone/
│   manage.py
│   Dockerfile
│   requirements.txt
│   .env
│
├── accountapp/        # User account-related app
├── articleapp/        # Post management app
├── commentapp/        # Comment feature app
├── profileapp/        # Profile management app
├── projectapp/        # Project management app
├── subscribeapp/      # Subscription feature app
│
├── templates/         # HTML template files
│   ├── base.html      # Base layout
│   ├── header.html    # Header UI
│   ├── footer.html    # Footer UI
│   └── snippets/      # Common UI components
│
├── static/            # Static files (CSS, JS, Fonts)
├── media/             # Uploaded image storage
│
└── Pinterest/         # Django project settings
    ├── settings/
    │   ├── base.py    # Common settings
    │   ├── local.py   # Development environment settings
    │   ├── deploy.py  # Deployment environment settings
    ├── urls.py        # URL routing
    ├── wsgi.py        # WSGI settings
    └── asgi.py        # ASGI settings
```

---

## **🛠 Tech Stack**  
- **Backend:** Django, Python  
- **Database:** SQLite (Development) / MySQL (Production)  
- **Frontend:** Bootstrap, MediumEditor  
- **Deployment & Environment:** Docker, AWS  

---

## **📝 API & URL Structure**  
| App | Feature | URL |
|----|------|-----|
| **Account** | Login | `/accounts/login/` |
| | Logout | `/accounts/logout/` |
| | Sign-up | `/accounts/create/` |
| | Edit Profile | `/accounts/update/<int:pk>/` |
| | Delete Account | `/accounts/delete/<int:pk>/` |
| **Article** | Post List | `/articles/list/` |
| | Create Post | `/articles/create/` |
| | View Post | `/articles/detail/<int:pk>/` |
| | Edit Post | `/articles/update/<int:pk>/` |
| | Delete Post | `/articles/delete/<int:pk>/` |
| **Comment** | Write Comment | `/comments/create/` |
| | Delete Comment | `/comments/delete/<int:pk>/` |
| **Project** | Project List | `/projects/list/` |
| | Create Project | `/projects/create/` |
| | View Project | `/projects/detail/<int:pk>/` |
| **Subscription** | Subscribe/Unsubscribe to Project | `/subscribe/subscribe/` |
| | View Subscribed Project Posts | `/subscribe/list/` |

---

## **🐳 Using Docker**  
### **1️⃣ Build the Docker Image**  
```bash
docker build -t pinterest-clone .
```

### **2️⃣ Run the Docker Container**  
```bash
docker run -d -p 8000:8000 --name pinterest-clone pinterest-clone
```

### **3️⃣ Stop and Remove the Container**  
```bash
docker stop pinterest-clone
docker rm pinterest-clone
```

---

## **📜 License**  
This project is licensed under the MIT License.  
