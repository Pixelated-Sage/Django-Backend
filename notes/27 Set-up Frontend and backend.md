
## ⚙️ Step-by-Step: Frontend Setup (React + Tailwind with Vite)

### 📌 1. Create Frontend Project

```bash
npm create vite@latest frontend
```

- **Project name:** `frontend`
    
- **Framework:** React
    
- **Variant:** JavaScript
    

Then:

```bash
cd frontend
npm install
```

---

### 📌 2. Install Tailwind CSS

Follow exactly:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Now update **`tailwind.config.js`**:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

In **`src/index.css`**, replace everything with:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Then import this in `main.jsx`:

```js
import './index.css'
```

---

### 📌 3. Basic Routing Setup (React Router)

```bash
npm install react-router-dom
```

In `src/` folder:

- `pages/Home.jsx`
    
- `pages/Input.jsx`
    
- `pages/Results.jsx`
    

Create routes in `App.jsx`:

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Input from "./pages/Input";
import Results from "./pages/Results";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/input" element={<Input />} />
        <Route path="/results" element={<Results />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

Each page just return a heading for now, like:

```jsx
// Home.jsx
export default function Home() {
  return <h1 className="text-2xl font-bold text-center mt-10">Welcome to SkillMatcher</h1>;
}
```

---

### ✅ Frontend Milestone:

-  React + Vite app created
    
-  Tailwind configured
    
-  React Router setup with 3 routes
    
-  Dummy pages working
    

---

## 🛠️ Now — Backend Setup (Django + DRF)

### 📌 1. Create Django Project

```bash
mkdir backend && cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django djangorestframework
django-admin startproject backend .
python manage.py startapp matcher
```

Add to `INSTALLED_APPS` in `backend/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'matcher',
]
```

---

### 📌 2. Create API Endpoint

In `matcher/views.py`:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def match_skills(request):
    skills = request.data.get('skills', [])
    # Dummy logic
    recommendations = {
        "Python": ["Data Science", "Web Dev"],
        "C++": ["DSA", "Competitive Programming"]
    }

    matched = {}
    for skill in skills:
        matched[skill] = recommendations.get(skill, ["No match found"])

    return Response({"matches": matched})
```

In `matcher/urls.py`:

```python
from django.urls import path
from .views import match_skills

urlpatterns = [
    path('match-skills/', match_skills),
]
```

Then in `backend/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('matcher.urls')),
]
```
