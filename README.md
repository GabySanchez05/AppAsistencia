# 🎓 AppAsistencia — Sistema de Asistencia Estudiantil

Aplicación web para el registro, verificación y control de asistencia de estudiantes de una institución escolar.

---

## 📐 Metodología de Desarrollo de Software: Modelo en V

El ciclo de vida del desarrollo de **AppAsistencia** se fundamenta rigurosamente en la metodología del **Modelo en V** (desarrollo secuencial con fases correspondientes de verificación y validación). Esta metodología garantiza que cada nivel de abstracción en el diseño del sistema cuente con especificaciones formales antes de proceder a la construcción, manteniendo una trazabilidad directa desde los requisitos del cliente hasta el código fuente final.

A continuación, se detalla la ejecución de la **Rama Descendente** y el **Punto de Inflexión** aplicados a la fase actual del proyecto:

---

### 🔽 Rama Descendente (Fase de Verificación y Especificación)

Esta etapa traduce progresivamente las necesidades del entorno escolar en especificaciones técnicas de bajo nivel:

#### 1. Análisis de Requisitos (Requirement Gathering)
* **Definición Teórica:** Es la fase inicial donde se recopilan, analizan y documentan formalmente las necesidades operativas de los usuarios y los objetivos que debe satisfacer el software. Se determinan tanto los requisitos funcionales (capacidades del sistema) como los no funcionales (rendimiento, seguridad, entorno de ejecución y restricciones).
* **Aplicación en AppAsistencia:**
  - **Requisitos Funcionales:** Identificación de la necesidad de sistematizar el control de asistencia en una institución educativa mediante cuatro perfiles bien diferenciados: *Administrador*, *Profesor*, *Estudiante* y *Visitante*. Requerimientos de auto-registro público, autenticación segura con roles, consulta de fichas personales y panel de control de base de datos.
  - **Requisitos No Funcionales:** Entorno de desarrollo reproducible y multiplataforma mediante virtualización por contenedores, base de datos relacional robusta con soporte para integridad referencial, interfaz web responsiva y herramientas integradas de inspección de datos.
  - **Artefactos del Proyecto:** Matriz de requisitos del subproyecto académico, especificación de casos de uso y definición del alcance técnico.

#### 2. Análisis del Sistema (System Analysis)
* **Definición Teórica:** Se traduce el conjunto de requisitos de usuario en una descripción formal del comportamiento global del sistema. Se definen los límites del software, la arquitectura funcional, los flujos de navegación y los mecanismos de autorización y seguridad sin descender aún a detalles particulares de código.
* **Aplicación en AppAsistencia:**
  - **Control de Acceso Basado en Roles (RBAC):** Se estableció la matriz de interacción y privilegios:
    - *Administrador:* Supervisión global, creación de usuarios institucionales y acceso a la administración técnica de datos.
    - *Profesor:* Espacio de trabajo docente para el control de asistencia diaria y seguimiento de secciones escolares.
    - *Estudiante:* Portal individual para verificación de datos y consulta de asistencias.
    - *Visitante:* Acceso libre a la información institucional y a los formularios de registro e inicio de sesión.
  - **Políticas de Autenticación y Redirección Dinámica:** Flujo operacional donde la raíz (`/`) evalúa la sesión y rol del usuario autenticado para redirigirlo de inmediato a su panel institucional correspondiente.
  - **Artefactos del Proyecto:** Mapeo de rutas globales, matriz de navegación y diseño del flujo de sesiones.

#### 3. Diseño de Software / Arquitectura (Software Design)
* **Definición Teórica:** Define la arquitectura técnica de alto nivel, la selección del stack tecnológico, la descomposición en componentes principales, los protocolos de comunicación y la infraestructura de despliegue y persistencia.
* **Aplicación en AppAsistencia:**
  - **Arquitectura Contenerizada y Multicapa:** Implementación de un ecosistema desacoplado mediante **Docker Compose**, compuesto por 4 servicios aislados e interconectados por una red interna privada:
    1. `db`: Motor de base de datos relacional **PostgreSQL 16**.
    2. `backend`: Núcleo de lógica y vistas en **Django 5.1** bajo arquitectura *Model-View-Template* (MVT).
    3. `frontend`: Entorno de desarrollo frontend moderno estructurado con **Vite.js**.
    4. `adminer`: Visor web ligero para auditoría visual directa del motor PostgreSQL.
  - **Gestión Desacoplada de Configuración:** Separación estricta entre código fuente y credenciales de configuración mediante variables de entorno (`.env`).
  - **Artefactos del Proyecto:** `docker-compose.yml`, `backend/Dockerfile`, `frontend/Dockerfile` y `backend/config/settings.py`.

#### 4. Diseño de Módulos (Module Design)
* **Definición Teórica:** Especifica con precisión la lógica interna, algoritmos, métodos, interfaces y modelos de datos de cada componente o módulo individual que conforma la solución.
* **Aplicación en AppAsistencia:**
  - **Módulo de Autenticación y Cuentas (`accounts`):** Extensión del modelo base de usuarios mediante `User(AbstractUser)` incorporando roles enumerados (`ADMIN`, `PROFESOR`, `ESTUDIANTE`), campos de contacto y fotografía, complementado por formularios especializados (`LoginForm`, `RegisterForm`, `UserProfileForm`).
  - **Módulo Escolar (`attendance`):** Modelado relacional que refleja el ecosistema escolar:
    - `Grade`: Grados y niveles académicos (Primaria / Secundaria).
    - `Student`: Ficha del estudiante con código de matrícula único y clave foránea hacia el grado.
    - `Attendance`: Registro diario con restricción de unicidad (`unique_together = ['student', 'date']`), estados normativos (*Presente*, *Ausente*, *Tardanza*, *Justificado*) y relación con el docente que asienta el registro.
  - **Módulo Núcleo (`core`):** Mixins reutilizables (`AdminRequiredMixin`, `ProfesorRequiredMixin`) para protección de controladores basados en clases (*CBVs*).
  - **Artefactos del Proyecto:** Archivos `models.py`, `forms.py`, `views.py` y `mixins.py` organizados por aplicación.

---

### 🔄 Punto de Inflexión

Representa la transición clave del ciclo en V donde los planos de diseño y especificaciones teóricas se materializan en código fuente ejecutable:

#### Codificación (Coding)
* **Definición Teórica:** Es la fase de construcción directa donde se programa, compila y ensambla el código fuente siguiendo los lineamientos de las etapas de diseño anteriores, aplicando principios de modularidad, legibilidad y estándares de desarrollo.
* **Aplicación en AppAsistencia:**
  - **Desarrollo Backend:** Implementación de vistas basadas en clases (*Class-Based Views*), enrutadores modulares (`urls.py`), context processors para inyección de roles en la interfaz y comandos CLI de aprovisionamiento (`seed_data`).
  - **Desarrollo Frontend e Interfaz:** Maquetación de plantillas HTML semánticas con arquitectura de herencia (`base.html`), desarrollo de hoja de estilos institucional personalizada (`styles.css`) con paleta escolar (Azul Colegial `#1b365d` y Amarillo Dorado `#facc15`), y scripts interactivos en JavaScript (`app.js`) para componentes como el visor interactivo de contraseñas.
  - **Persistencia y Esquema:** Creación y aplicación de migraciones automáticas sobre PostgreSQL para generar la estructura física de las tablas.
  - **Control de Versiones:** Gestión integral del código fuente mediante control de versiones en **Git** y **GitHub** con mensajes de confirmación descriptivos y estructurados.

---

## 🛠️ Stack de Desarrollo

- **Backend:** Python 3.12 + Django 5.1 (REST Framework, CORS)
- **Frontend:** Vite.js
- **Base de Datos:** PostgreSQL 16
- **Visor de Base de Datos Web:** Adminer
- **Contenedores:** Docker + Docker Compose

---

## 🚀 Inicio Rápido para Colaboradores y Docentes

### 1. Clonar el repositorio
```bash
git clone https://github.com/GabySanchez05/AppAsistencia.git
cd AppAsistencia
```

### 2. Variables de entorno
Crear el archivo `.env` copiando el ejemplo (en Windows PowerShell o CMD):
```powershell
copy .env.example .env
```
*(o en Linux/Mac: `cp .env.example .env`)*

### 3. Levantar todo el stack con Docker
```bash
docker-compose up --build
```

> **¡Listo!** En el primer arranque, el contenedor de backend realiza automáticamente las migraciones (estructurando las tablas relacionales en la base de datos) y deja habilitadas las cuentas base para las pruebas de roles.

---

## 🌐 Servicios y Enlaces de Acceso

| Servicio | URL | Descripción |
|---|---|---|
| **Sistema Web (Django)** | [http://localhost:8000](http://localhost:8000) | Plataforma escolar, inicio de sesión y registro |
| **Frontend (Vite)** | [http://localhost:5173](http://localhost:5173) | Servidor de desarrollo frontend con recarga en caliente |
| **Django Admin** | [http://localhost:8000/admin/](http://localhost:8000/admin/) | Panel de administración de tablas del modelo |
| **Visor de Base de Datos (Adminer)** | [http://localhost:8080](http://localhost:8080) | Inspección visual en vivo de tablas SQL, relaciones y datos |

---

## 🗄️ Cómo Visualizar la Base de Datos en Tiempo Real

El docente o revisor cuenta con **dos opciones integradas en el navegador** sin instalar software adicional:

### Opción A: Django Admin (Gestión del Modelo de Datos)
1. Ingresar a [http://localhost:8000/admin/](http://localhost:8000/admin/)
2. Iniciar sesión con:
   - **Usuario:** `admin`
   - **Contraseña:** `Admin123!`
3. Permite visualizar, buscar, filtrar y administrar directamente las tablas de usuarios, estudiantes, secciones y asistencias.

### Opción B: Adminer (Visor SQL de PostgreSQL en Vivo)
1. Ingresar a [http://localhost:8080](http://localhost:8080)
2. Los datos de conexión son:
   - **Sistema:** `PostgreSQL`
   - **Servidor:** `db`
   - **Usuario:** `asistencia_user`
   - **Contraseña:** `asistencia_pass_2026`
   - **Base de datos:** `asistencia_db`
3. Permite ver el esquema relacional, ejecutar sentencias SQL directas y verificar las tablas en tiempo real conforme se registren nuevos datos.

---

## 👥 Cuentas de Acceso por Rol (Datos Iniciales)

| Rol | Usuario | Contraseña | Permisos y Alcance |
|---|---|---|---|
| **👑 Administrador** | `admin` | `Admin123!` | Acceso total al sistema, panel Django Admin y creación de cualquier tipo de usuario. |
| **👨‍🏫 Profesor** | `profesor` | `Profesor123!` | Panel docente institucional para el seguimiento y control de asistencia escolar. |
| **🎓 Estudiante** | `estudiante` | `Estudiante123!` | Portal del estudiante para consulta de información personal y récord de asistencias. |

> Cualquier visitante puede crear una nueva cuenta mediante el botón **"Registrarse"** seleccionando el rol de Estudiante o Profesor.

---

## 📁 Estructura del Proyecto

```
AppAsistencia/
├── docker-compose.yml          # Orquestación de db, backend, frontend y adminer
├── .env.example                # Plantilla de variables de entorno
├── .gitignore                  # Exclusiones de Git
├── README.md                   # Esta documentación
│
├── backend/                    # Proyecto Django
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/                 # Configuración principal (settings, urls)
│   ├── accounts/               # App de usuarios, roles, login y registro
│   ├── attendance/             # App de grados, estudiantes y asistencias
│   ├── core/                   # Mixins, utilidades y comando seed_data
│   ├── templates/              # Plantillas HTML con navegación por rol
│   └── static/                 # Estilos CSS escolares (Azul/Amarillo) y JS
│
└── frontend/                   # Proyecto Vite.js
    ├── Dockerfile
    ├── package.json
    ├── vite.config.js
    └── index.html
```

---

## 📜 Licencia

Proyecto académico desarrollado para el subproyecto de Desarrollo de Aplicaciones 1.
