---

````markdown
# 🧠 Django DRF Learning Repo

This is my personal learning repository built with **Django** and **Django REST Framework (DRF)**.  
Here I apply everything I'm learning about building RESTful APIs using Python and Django.

## 🔧 What I’ve Learned and Practiced

- ✅ DRF setup and configuration
- ✅ Function-Based Views (FBV)
- ✅ Class-Based Views (CBV)
- ✅ Mixins and Generic Views
- ✅ ViewSets and Routers
- ✅ Serializers and ModelSerializers
- ✅ Permissions and authentication
- ✅ Full CRUD via REST API

## 🚀 Running the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/drf-lab.git
   cd drf-lab
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and start the server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the app**

   * API Root: `http://127.0.0.1:8000/api/`
   * Admin Panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
drf_lab/
├── api/             # Main app with views, serializers, urls
├── drf_lab/         # Project settings
├── manage.py
└── requirements.txt
```

## 🧪 Next Steps

* [ ] Add JWT authentication
* [ ] Add documentation (Swagger / drf-spectacular)
* [ ] Write automated tests
* [ ] Add Docker support
* [ ] Deploy to a platform (e.g. Railway, Render)

## 📄 License

This is an educational project. Licensed under the MIT License.

---

Made with 🧠 and ☕ while learning Django and DRF.
