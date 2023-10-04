import os
import subprocess
import sys
import io
import shutil

def create_virtual_environment():
    env_folder = "env"
    
    if not os.path.exists(env_folder):
        print("Creando entorno virtual...")
        try:
            subprocess.run([sys.executable, "-m", "venv", env_folder], check=True)
        except subprocess.CalledProcessError:
            print("Error al crear el entorno virtual.")
            sys.exit(1)
        print("Entorno virtual creado con éxito.")

        # Actualizar pip a la última versión en el entorno virtual
        try:
            subprocess.run([os.path.join(env_folder, "Scripts", "python"), "-m", "pip", "install", "--upgrade", "pip"], check=True)
        except subprocess.CalledProcessError:
            print("Error al actualizar pip en el entorno virtual.")
    else:
        print("El entorno virtual ya existe. Saltando paso de creación.")



def activate_virtual_environment():
    env_folder = "env"  # Change the folder name to "env" for the virtual environment

    # Determine the appropriate command to activate the virtual environment based on the OS
    if os.name == 'nt':
        activate_cmd = os.path.join(env_folder, "Scripts", "activate")
    else:
        activate_cmd = os.path.join(env_folder, "bin", "activate")

    print("Activando el entorno virtual...")
    try:
        subprocess.run(activate_cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error al activar el entorno virtual.")
        sys.exit(1)
    print("Entorno virtual activado con éxito.")

def deactivate_virtual_environment():
    if os.name == 'nt':
        deactivate_cmd = "deactivate"
    else:
        deactivate_cmd = "deactivate"

    print("Desactivando el entorno virtual...")
    try:
        subprocess.run(deactivate_cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error al desactivar el entorno virtual.")
        sys.exit(1)
    print("Entorno virtual desactivado con éxito.")


def install_django():
    # Paso 3: Comprobar si Django ya está instalado
    print("Instalando Django...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "Django==4.2.4"], check=True)
    except subprocess.CalledProcessError:
        print("Error al instalar Django.")
        sys.exit(1)
    print("Django instalado con éxito.")




def check_virtual_environment():
    if os.name == 'nt':
        activate_cmd = os.path.join("env", "Scripts", "activate")
    else:
        activate_cmd = os.path.join(".env", "bin", "activate")

    if not os.environ.get('VIRTUAL_ENV'):
        print("************************** IAPORT SETUP APP *********************")
        print("******************El entorno virtual no está activado.*********************")
        print(f"----------Activa el entorno virtual manualmente con el siguiente comando: {activate_cmd}")
        print("----------Luego, vuelve a ejecutar el script con el entorno activado: python setupapp.py ")
        sys.exit(1)
    else:
        print("Entorno virtual activado correctamente.")

def install_dependencies():
    check_virtual_environment()

    # Paso 4: Instalar las dependencias desde el archivo requirements.txt
    print("Instalando las dependencias desde requirements.txt...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("Error al instalar las dependencias desde requirements.txt.")
        sys.exit(1)
    print("Dependencias instaladas con éxito.")



def start_django_project():
    # Paso 5: Iniciar el proyecto core de Django
    print("Iniciando el proyecto core de Django...")
    try:
        subprocess.run(["django-admin", "startproject", "core", "."], check=True)
    except subprocess.CalledProcessError:
        print("Error al iniciar el proyecto core de Django.")
        sys.exit(1)
    print("Proyecto core de Django iniciado con éxito.")


def create_gitignore():
    gitignore_content = """\
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media
#<django-project-name>/staticfiles/
*.py[cod]
*$py.class
*.so
.Python
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
*.manifest
*.spec
pip-log.txt
pip-delete-this-directory.txt
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/
*.mo
instance/
.webassets-cache
.scrapy
docs/_build/
.pybuilder/
target/
.ipynb_checkpoints
profile_default/
ipython_config.py
.pdm.toml
__pypackages__/
celerybeat-schedule
celerybeat.pid
*.sage.py
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.spyderproject
.spyproject
.ropeproject
/site
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
.pytype/
cython_debug/
# .idea/
poetry.toml
.ruff_cache/
pyrightconfig.json
"""
    with open(".gitignore", "w") as gitignore_file:
        gitignore_file.write(gitignore_content)



def create_requirements_txt():
    requirements_content = """\
asgiref==3.7.2
Django==4.2.4
django-ckeditor==6.7.0
django-cors-headers==4.2.0
django-environ==0.10.0
django-js-asset==2.1.0
django-storages==1.13.2
djangorestframework==3.14.0
Pillow==10.0.0
psycopg2==2.9.6
python-dotenv==1.0.0
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3

"""

    with open("requirements.txt", "w") as requirements_file:
        requirements_file.write(requirements_content)


def create_urls():
    urls_content = """\
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

"""

    with open("urls.py", "w") as urls_file:
        urls_file.write(urls_content)



def create_env():
    env_content = """\
SECRET_KEY='j_-_#11i)cjgjz0^c$03g!z1_ucmj+sdl!_(8vg#@d_8h*$jh!'
DEBUG=True

DATABASE_URL=''

ALLOWED_HOSTS_DEV= *
ALLOWED_HOSTS_DEPLOY=iaport.com,www.iaport.com


CORS_ORIGIN_WHITELIST_DEV=http://localhost:3000
CORS_ORIGIN_WHITELIST_DEV=https://iaport.com

CSRF_TRUSTED_ORIGINS_DEV=http://localhost:3000
CSRF_TRUSTED_ORIGINS_DEPLOY=https://iaport.com

"""

    with open(".env", "w") as env_file:
        env_file.write(env_content)


def create_settings():
    settings_content = """\
from pathlib import Path
import os
from environ import Env
from dotenv import load_dotenv

env = Env()
env.read_env()  # Lee las variables de entorno desde un archivo .env si existe

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'


ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS_DEV')]



# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [    

]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'
]

INSTALLED_APPS =DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'autoParagraph': False
    }
}
CKEDITOR_UPLOAD_PATH= "/media/"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'build/static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
}



CORS_ORIGIN_WHITELIST = [os.environ.get ('CORS_ORIGIN_WHITELIST_DEV')]


print("CSRF_TRUSTED_ORIGINS_DEV:", os.environ.get('CSRF_TRUSTED_ORIGINS_DEV'))
CSRF_TRUSTED_ORIGINS = [os.environ.get('CSRF_TRUSTED_ORIGINS_DEV')]
print("CSRF_TRUSTED_ORIGINS:", CSRF_TRUSTED_ORIGINS)



EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS_DEPLOY')]
    CORS_ORIGIN_WHITELIST = [os.environ.get('CORS_ORIGIN_WHITELIST_DEPLOY')]
    CSRF_TRUSTED_ORIGINS = [os.environ.get('CSRF_TRUSTED_ORIGINS_DEPLOY')]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            #"NAME": os.environ.get("DB_NAME"),
            #"USER": os.environ.get("DB_USER"),
            #"PASSWORD": os.environ.get("DB_PASSWORD"),
            #"HOST": os.environ.get("DB_HOST"),
            #"PORT": os.environ.get("DB_PORT"),
            "ATOMIC_REQUESTS": True,  # Aquí estableces ATOMIC_REQUESTS
        }
    }




"""

    with open("settings.py", "w") as settings_file:
        settings_file.write(settings_content)


def crear_carpeta_media():
    # Nombre de la carpeta que queremos crear
    carpeta_media = "media"

    try:
        # Crear la carpeta "apps"
        os.makedirs(carpeta_media)
        print(f'Se ha creado la carpeta "{carpeta_media}"')
    except Exception as e:
        print(f'Error al crear la carpeta: {e}')





def crear_carpeta_apps():
    # Nombre de la carpeta que queremos crear
    carpeta_apps = "apps"

    try:
        # Crear la carpeta "apps"
        os.makedirs(carpeta_apps)
        print(f'Se ha creado la carpeta "{carpeta_apps}"')
    except Exception as e:
        print(f'Error al crear la carpeta: {e}')



def crear_archivo_init_py():
    # Nombre del archivo "__init__.py" que queremos crear
    archivo_init_py = "__init__.py"

    # Ruta completa del archivo "__init__.py" dentro de la carpeta "apps"
    ruta_archivo_init_py = os.path.join("apps", archivo_init_py)

    try:
        # Crear el archivo "__init__.py" dentro de la carpeta "apps"
        with open(ruta_archivo_init_py, 'w') as f:
            f.write('')
        print(f'Se ha creado el archivo "{archivo_init_py}" dentro de la carpeta "apps"')
    except Exception as e:
        print(f'Error al crear el archivo "{archivo_init_py}": {e}')


import subprocess

def ejecutar_migrate():
    try:
        # Ejecutar el comando "python manage.py migrate" en Windows
        subprocess.run(["python", "manage.py", "migrate"])
        print("El comando 'migrate' se ha ejecutado correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el comando 'migrate': {e}")

def crear_carpeta_react():
    # Nombre de la carpeta que queremos crear
    carpeta_react = "react"

    try:
        # Crear la carpeta "react"
        os.makedirs(carpeta_react)
        print(f'Se ha creado la carpeta "{carpeta_react}"')
    except Exception as e:
        print(f'Error al crear la carpeta: {e}')


def create_tsconfig():
    tsconfig_content = """\
{
    "compilerOptions": {
        "baseUrl": "src",
        "target": "ES5",
        "lib": [
            "dom",
            "DOM.Iterable",
            "ESNext"
        ],
        "allowJs": true,
        "skipLibCheck": true,
        "esModuleInterop": true,
        "allowSyntheticDefaultImports": true,
        "noFallthroughCasesInSwitch": true,
        "module": "ESNext",
        "moduleResolution": "Node",
        "resolveJsonModule": true,
        "isolatedModules": true,
        "noEmit": true,
        "jsx": "react-jsx"
    },
    "include": [
        "src"
    ]

}


"""

    with open("tsconfig.json", "w") as tsconfig_file:
        tsconfig_file.write(tsconfig_content)


def move_and_replace_files():
    source_dir = os.getcwd()  # Directorio actual
    core_dir = os.path.join(source_dir, "core")  # Directorio "core" dentro del directorio actual
    
    # Verificar si el directorio "core" existe
    if not os.path.exists(core_dir):
        print("El directorio 'core' no existe en el directorio actual.")
        return
    
    files_to_move = ["settings.py", "urls.py"]  # Archivos a mover y reemplazar
    
    for file_name in files_to_move:
        source_file_path = os.path.join(source_dir, file_name)
        target_file_path = os.path.join(core_dir, file_name)
        
        # Verificar si el archivo fuente existe
        if os.path.exists(source_file_path):
            # Mover y reemplazar el archivo
            shutil.move(source_file_path, target_file_path)
            print(f"Archivo '{file_name}' movido y reemplazado en la carpeta 'core'.")
        else:
            print(f"El archivo '{file_name}' no existe en el directorio actual.")




def create_react_app(project_name):
    if not os.path.exists(project_name):
        os.system(f"npx create-react-app {project_name}")
        print(f"React app '{project_name}' created successfully.")
    else:
        print(f"The project folder '{project_name}' already exists. Skipping creation.")


def move_reactapp_files():
    current_dir = os.getcwd()
    reactapp_dir = os.path.join(current_dir, "reactapp")

    if os.path.exists(reactapp_dir):
        public_dir = os.path.join(reactapp_dir, "public")
        package_json = os.path.join(reactapp_dir, "package.json")

        if os.path.exists(public_dir) and os.path.exists(package_json):
            try:
                # Mover la carpeta "public" y el archivo "package.json"
                shutil.move(public_dir, current_dir)
                shutil.move(package_json, current_dir)

                # Eliminar la carpeta "reactapp"
                shutil.rmtree(reactapp_dir)

                print("Files moved and reactapp directory deleted successfully.")
            except Exception as e:
                print(f"An error occurred while moving files: {e}")
        else:
            print("Cannot find 'public' folder or 'package.json' in reactapp.")
    else:
        print("No 'reactapp' folder found in the current directory.")





def create_react_project_structure():
    folders = [
        "src",
        "src/assets",
        "src/components",
        "src/containers",
        "src/hocs",
        "src/redux",
        "src/styles",
        "src/assets/img",
        "src/assets/video",
        "src/components/navigation",
        "src/containers/errors",
        "src/containers/pages",
        "src/hocs/layouts",
        "src/hocs/routes",
        "src/redux/actions",
        "src/redux/reducers"
    ]

    files = [
        ("src/App.js", """
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import store from 'store';
import Error404 from 'containers/errors/Error404';
import Home from 'containers/pages/Home';
import Services from 'containers/pages/Services';
import Aboutus from 'containers/pages/Aboutus';
import Contact from 'containers/pages/Contact';


function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          {/* Error Display */}
          <Route path="*" element={<Error404 />} />

          {/* Home Display */}
          <Route path="/" element={<Home />} />
         
          {/* Aboutus Display */}
          <Route path="/Aboutus" element={<Aboutus />} />
         
          {/* Services Display */}
          <Route path="/Services" element={<Services />} />
         
          {/* Contact Display */}
          <Route path="/Contact" element={<Contact />} />
         


        </Routes>
      </Router>
    </Provider>
  );
}

export default App;

        """),
        ("src/index.js", """
import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

         """),
        ("src/reportWebVitals.js", """
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;

        """),
        ("src/store.js", """
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './redux/reducers'; // Asegúrate de importar tus reducers correctamente
import { composeWithDevTools } from 'redux-devtools-extension';

const initialState = {};

const middleware = [thunk]; // Cambiado 'meddleware' a 'middleware'

const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware)) // Usando 'composeWithDevTools' para integrar Redux DevTools
// applyMiddleware(...middleware)
);

export default store;

        """),
        ("src/containers/errors/Error404.jsx", """
            function Error404() {
                return (
                    <div>
                        Error 404
                    </div>
                );
            }

            export default Error404;
        """),
        ("src/containers/pages/Home.jsx", """
            
            import Layout from "hocs/layouts/Layout";
            import Navbar from "components/navigation/Navbar";
            import Footer from "hocs/layouts/Footer";
            import Header from "components/home/Header";

            function Home() {
                return (
                    <Layout>
                        <Navbar />
                        <div className="pt-28">
                            <Header/>
                        </div>
                        
                        <Footer />
                    </Layout>
                );
            }

            export default Home;
        
        """),
        ("src/containers/pages/Services.jsx", """
            
            import Layout from "hocs/layouts/Layout";
            import Navbar from "components/navigation/Navbar";
            import Footer from "hocs/layouts/Footer";

            function Services() {
                return (
                    <Layout>
                        <Navbar />
                        Services
                        <Footer />
                    </Layout>
                );
            }

            export default Services;
        """),
        ("src/containers/pages/Aboutus.jsx", """
            
            
            import Layout from "hocs/layouts/Layout";
            import Navbar from "components/navigation/Navbar";
            import Footer from "hocs/layouts/Footer";

            function Aboutus() {
                return (
                    <Layout>
                        <Navbar />
                        About us
                        <Footer />
                    </Layout>
                );
            }

            export default Aboutus;
        
        """),
        ("src/containers/pages/Contact.jsx", """
            import Layout from "hocs/layouts/Layout";
            import Navbar from "components/navigation/Navbar";
            import Footer from "hocs/layouts/Footer";

            function Contact() {
                return (
                    <Layout>
                        <Navbar />
                        Contact
                        <Footer />
                    </Layout>
                );
            }

            export default Contact;
        
        
        """),
        ("src/hocs/layouts/Footer.jsx", """
            // src/hocs/layouts/Footer.jsx

import React from 'react';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';
import './Footer.css';
import iaportlogo from 'assets/img/iaportlogo.png';

function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="footer">
            <div className="footer-content">
                <div className="footer-section">
                    <div className="footer-logo">
                        <img 
                            src={iaportlogo}
                            width={50}
                            height={40}
                            alt="IA Port Logo"
                        />
                    </div>
                    <h3 className="footer-section-title">About Us</h3>
                    <p className="footer-section-text">
                        We are a company dedicated to providing innovative solutions to meet your needs.
                    </p>
                </div>
                <div className="footer-section">
                    <h3 className="footer-section-title">Our Services</h3>
                    <ul className="footer-section-list">
                        <li><a href="#">Service 1</a></li>
                        <li><a href="#">Service 2</a></li>
                        <li><a href="#">Service 3</a></li>
                    </ul>
                </div>
                <div className="footer-section">
                    <h3 className="footer-section-title">Contact Us</h3>
                    <p className="footer-section-text">Feel free to reach out to us: <a className="footer-email" href="mailto:info@iaport.com">info@iaport.com</a></p>
                </div>
                <div className="footer-section">
                    <h3 className="footer-section-title">Follow Us on Social Media</h3>
                    <div className="social-icons">
                        <a className="social-link" href="https://www.facebook.com/your_page" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                            <FaFacebook className="social-icon" />
                        </a>
                        <a className="social-link" href="https://www.twitter.com/your_page" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
                            <FaTwitter className="social-icon" />
                        </a>
                        <a className="social-link" href="https://www.instagram.com/your_page" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                            <FaInstagram className="social-icon" />
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default Footer;

        """),
        ("src/hocs/layouts/Footer.css", """
            /* Footer.css */

/* General styles for the footer */

.footer {
  background-color: #141414;
  color: #ffffff;
  padding: 50px 0;
  text-align: center;
}

/* Container for footer content */

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  max-width: 1200px;
  margin: 0 auto;
}

/* Individual section of the footer */
.footer-section {
  flex: 1;
  padding: 20px;
  text-align: left;
}

/* Titles for footer sections */
.footer-section-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
}

/* Text in footer sections */
.footer-section-text {
  font-size: 14px;
  color: #ccc;
  margin-bottom: 20px;
}

/* List of links in footer sections */
.footer-section-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Elements of the list of links in footer sections */
.footer-section-list li {
  margin-bottom: 10px;
}

/* Links in the list of links in footer sections */
.footer-section-list li a {
  color: #6ab1f5;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.footer-section-list li a:hover {
  color: #1a8cd8;
}

/* Styles for social icons */
.social-icons {
  display: flex;
  gap: 30px;
}

/* Styles for social media links */
.social-link {
  color: #6ab1f5;
  font-size: 24px;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.social-link:hover {
  color: #1a8cd8;
}

/* Styles for email link */
.footer-email {
  color: #6ab1f5;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.footer-email:hover {
  color: #1a8cd8;
}

/* Styles for the footer logo */
.footer-logo {
  margin-bottom: 20px;
}

        """),
        ("src/hocs/layouts/Layout.jsx", """
            import { connect } from "react-redux";

            function Layout({ children }) {
                return (
                    <div>
                        {children}
                    </div>
                );
            }

            const mapStateToProp = state => ({
                // Map state if needed
            });

            export default connect(mapStateToProp)(Layout);
        """),
        ("src/redux/reducers/index.js", """
            import { combineReducers } from 'redux';

            export default combineReducers ({

            });
        """),
        ("src/styles/index.css", """
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

        """)
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file_name, content in files:
        with open(file_name, "w") as file:
            file.write(content)
            print(f"Created file: {file_name}")

    print("React project structure created successfully.")



def move_logo_file():
    # Rutas de origen y destino
    origen = "iaportlogo.png"
    destino = os.path.join("src", "assets", "img", "iaportlogo.png")
    
    # Mover el archivo
    try:
        shutil.copy(origen, destino)
        print("Logo copiado exitosamente.")
    except FileNotFoundError:
        print("El logo no se encontró en la ubicación de origen.")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")



def create_package():
    package_content = """\
{
  "name": "reactapp",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@emailjs/browser": "^3.11.0",
    "@jridgewell/sourcemap-codec": "^1.4.15",
    "@react-three/drei": "^9.80.5",
    "@react-three/fiber": "^8.13.7",
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.4.0",
    "feather-icons-react": "^0.6.2",
    "framer-motion": "^10.16.1",
    "maath": "^0.7.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^4.10.1",
    "react-redux": "^8.1.2",
    "react-router-dom": "^6.15.0",
    "react-scripts": "^5.0.1",
    "react-tilt": "^1.0.2",
    "react-vertical-timeline-component": "^3.6.0",
    "redux-devtools-extension": "^2.13.9",
    "redux-thunk": "^2.4.2",
    "three": "^0.155.0",
    "typescript": "^4.9.5",
    "web-vitals": "^2.1.4"
  },
  "devDependencies": {
    "@rollup/plugin-terser": "^0.4.3",
    "tailwindcss": "^3.3.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "npm run build:tailwind && react-scripts build",
    "build:tailwind": "tailwindcss build src/styles.css -o src/tailwind.css",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}


"""

    with open("package.json", "w") as package_file:
        package_file.write(package_content)



def create_styles_css_file():
    content = """
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Estilos globales */
body {
  font-family: 'Helvetica Neue', sans-serif;
  background-color: #f0f0f0;
}

/* Personalizaciones */
/* Puedes agregar estilos personalizados aquí */

/* Clases de utilidad */
/* Puedes usar las clases de utilidad de Tailwind CSS aquí */

/* Estilos específicos de componentes */
/* Si tienes estilos específicos para ciertos componentes, puedes definirlos aquí */
"""
    try:
        with open('src/styles.css', 'w') as file:
            file.write(content)
        print("Archivo styles.css creado exitosamente en la carpeta src.")
    except Exception as e:
        print("Ocurrió un error al crear el archivo:", e)





def create_tailwindconf():
    tailwindconf_content = """\
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        colornegro: '#1B1B1B', // Usando el valor hexadecimal
        
      },
    },
  },
  plugins: [],
};


"""

    with open("tailwind.config.js", "w") as tailwindconf_file:
        tailwindconf_file.write(tailwindconf_content)


def create_postconf():
    postconf_content = """\
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}



"""

    with open("postcss.config.js", "w") as postconf_file:
        postconf_file.write(postconf_content)




def create_navigation_files():
    # Crear la carpeta 'src/components/navigation' si no existe
    os.makedirs('src/components/navigation', exist_ok=True)

    # Contenido del archivo 'Navbar.js'
    navbar_js_content = """
    import React, { useState } from 'react';
import FeatherIcon from 'feather-icons-react';
import iaportlogo from 'assets/img/iaportlogo.png';
import './Navbar.css'; 
import { Link } from 'react-router-dom';

function Navbar() {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };
    
    return (
        <nav className={`bg-colornegro text-white p-4 shadow-lg ${menuOpen ? 'menu-open-bg' : ''}`}>
            <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                    <img 
                        src={iaportlogo}
                        width={50}
                        height={40}
                        alt="IA Port Logo"
                    />
                    <div className="text-2xl font-semibold">I A P O R T</div>
                </div>
                <div className="hidden md:flex space-x-8">
                    <Link to="/" className="hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="home" className="inline-block mr-2" />
                        <span className="icon-hover-text">Home</span>
                    </Link>
                    <Link to="/Services" className="hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="cpu" className="inline-block mr-2" /> 
                        <span className="icon-hover-text">Services</span>
                    </Link>
                    <Link to="/Aboutus" className="hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="users" className="inline-block mr-2" /> 
                        <span className="icon-hover-text">About us</span>
                    </Link>
                    <Link to="/Contact" className="hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="mail" className="inline-block mr-2" /> 
                        <span className="icon-hover-text">Contact</span>
                    </Link>
                </div>
                <div className="hidden md:flex space-x-4">
                    <button className="text-white text-sm hover:text-blue-300 cursor-pointer rounded-full px-4 py-1.5 transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="user" className="inline-block mr-2" /> Sign In
                    </button>
                    <button className="text-white text-sm hover:text-blue-300 py-2 px-4 rounded-full cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                        <FeatherIcon icon="plus" className="inline-block mr-2" /> Sign Up
                    </button>
                </div>
                <div className="md:hidden">
                    <button onClick={toggleMenu} className={`text-white text-xl focus:outline-none ${menuOpen ? 'open' : ''}`}>
                        {menuOpen ? '✕' : '☰'}
                    </button>
                </div>
            </div>
            {menuOpen && (
                <div className="md:hidden mt-4 flex flex-col justify-center items-center">
                    <div className="flex flex-col space-y-4">
                        <Link to="/" className="block hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="home" className="inline-block mr-2 ml-4" /> Home 
                        </Link>
                        <Link to ="/Aboutus" className="block hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="users" className="inline-block mr-2 ml-4" /> About us 
                        </Link>
                        <Link to="/Services" className="block  hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="cpu" className="inline-block mr-2 ml-4" /> Services 
                        </Link>
                        <Link to="/Contact" className="block hover:text-blue-300 cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="mail" className="inline-block mr-2 ml-4" /> Contact 
                        </Link>
                    </div>
                    <div className="flex flex-col space-y-4 mt-4">
                        <button className="flex items-center text-white text-sm hover:text-blue-300 cursor-pointer rounded-full px-4 py-1.5 transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="user" className="inline-block mr-2" /> Sign In
                        </button>
                        <button className="flex items-start text-white text-sm hover:text-blue-300 py-2 px-4 rounded-full cursor-pointer transition duration-300 ease-in-out transform hover:scale-105">
                            <FeatherIcon icon="plus" className="inline-block mr-2" /> Sign Up
                        </button>
                    </div>
                </div>
            )}
        </nav>
    );
}

export default Navbar;
    """

    # Contenido del archivo 'Navbar.css'
    navbar_css_content = """
    .icon-hover-text {
    display: none;
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    padding: 4px;
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    border-radius: 4px;
    font-size: 12px;
    pointer-events: none;
}

a:hover .icon-hover-text {
    display: block;
}

/* Agrega el color de fondo azul para el menú en modo móvil */
.menu-open-bg {
    background-color: rgb(0, 119, 255); /* Cambia este color al azul que desees */
}
    """

    # Rutas de los archivos
    navbar_js_path = 'src/components/navigation/Navbar.js'
    navbar_css_path = 'src/components/navigation/Navbar.css'

    # Escribir contenido en los archivos
    with open(navbar_js_path, 'w', encoding='utf-8') as navbar_js_file:
        navbar_js_file.write(navbar_js_content.strip())

    with open(navbar_css_path, 'w', encoding='utf-8') as navbar_css_file:
        navbar_css_file.write(navbar_css_content.strip())

    print("Archivos de navegación creados exitosamente.")



def create_header_files():
    # Directorio donde se deben crear los archivos
    target_directory = "src/components/home"
    
    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Contenido del archivo Header.js
    header_js_content = """

import React from "react";

import "./Header.css"; // Importa el archivo de estilos

const Header = () => {
  return (
    <div className="bg-black text-white">
      <div className="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56 text-center">
        <h1 className="title-style">
          Welcome to the <span className="text-blue-500">Future</span> of Modern Trading.
        </h1>
        <p className="description-style">
          Our AI-powered bots bring <span className="text-blue-500">unparalleled intelligence</span> to your investment decisions. Harness the <span className="text-blue-500">Power</span> of Finance and <span className="text-blue-500">Unlock</span> Your Portfolio's Potential.
        </p>
        <div className="mt-10 flex flex-col md:flex-row items-center justify-center gap-y-4 md:gap-x-6">
          <a href="#" className="cta-button">
            Get Started
          </a>
          <a href="#" className="learn-more-link">
            Learn More <span aria-hidden="true">→</span>
          </a>
        </div>
      </div>
      
    </div>
  );
};

export default Header;



"""
    
    # Contenido del archivo Header.css
    header_css_content = """
/* Header styles */
.bg-black {
  background-color: black;
}

/* Title styles */
.title-style {
  font-size: 2.5rem;
  font-weight: 800;
  color: #FFFFFF;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

/* Description styles */
.description-style {
  font-size: 1.25rem;
  line-height: 1.6;
  color: #B8C2CC;
}

/* CTA button styles */
.cta-button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #3B82F6;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 600;
  border-radius: 6px;
  transition: background-color 0.3s, transform 0.3s;
}

.cta-button:hover {
  background-color: #2563EB;
  transform: scale(1.05);
}

/* Learn More link styles */
.learn-more-link {
  font-size: 16px;
  font-weight: 600;
  color: #B8C2CC;
  transition: color 0.3s;
}

.learn-more-link:hover {
  color: #3B82F6;
}

/* Image container styles */
.image-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  bottom: -8rem; /* Adjust the position if needed */
  left: 50%;
  transform: translateX(-50%);
  opacity: 0.8;
}

/* AI Hand styles */
.ai-hand {
  width: 35rem; /* Increase the image size */
  animation: fadeInLeft 1s ease-in-out 0.5s forwards;
}

/* Human Hand styles */
.human-hand {
  width: 35rem; /* Increase the image size */
  animation: fadeInRight 1s ease-in-out 0.5s forwards;
}

"""
    
    # Crear archivo Header.js
    with open(os.path.join(target_directory, "Header.js"), "w", encoding="utf-8") as header_js_file:
        header_js_file.write(header_js_content)
    
    # Crear archivo Header.css
    with open(os.path.join(target_directory, "Header.css"), "w", encoding="utf-8") as header_css_file:
        header_css_file.write(header_css_content)
    
    print("Archivos Header.js y Header.css creados con éxito.")


def main():
    
    
    print("Ruta actual:", os.getcwd())  
    create_virtual_environment()
    
    
    
    install_django()
    
    
    project_name = "reactapp"  # Cambia este nombre si lo deseas
    create_react_app(project_name)
    create_requirements_txt()
    install_dependencies()
    start_django_project()
    create_gitignore()
    create_env()
    create_settings()
    crear_carpeta_apps()
    crear_archivo_init_py()
    crear_carpeta_media()
    create_urls()
    ejecutar_migrate()
    create_tsconfig()
    create_postconf()
    create_tailwindconf()
    move_and_replace_files()
    move_reactapp_files()
    create_react_project_structure()
    create_navigation_files ()
    move_logo_file()
    create_package()
    create_styles_css_file()
    create_header_files()
    
    

if __name__ == "__main__":
    main()
    




print("*******************************************************")
print("*******************************************************")
print("***** PASOS PARA CONFIGURAR EL PROYECTO CON REACT *****")
print("*******************************************************")
print("*******************************************************")




print("Paso 1:       *deactivate*                    para salir del entorno birutal")
print("Paso 2:       *npm install*                   para instalar las dependencias de Node.")
print("Paso 3:      *npm run build*                  para empacar archivos de React y Tailwind en la carpteta build.")
print("Paso 4:   *env/scripts/activate*              Activa del entorno virtual.")
print("Paso 5:*'python manage.py collectstatic'*     Crea la carpeta '{}'  .".format('static'))
print(" instalar iconos: npm install @fortawesome/fontawesome-free.")

    
   