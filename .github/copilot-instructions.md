## Instrucciones para agentes AI (proyecto: Pagina-local)

Este repositorio es una pequeña aplicación Flask con plantillas HTML estáticas y almacenamiento simple en JSON. Las siguientes notas ayudan a que un agente AI sea productivo rápidamente aquí.

- **Arquitectura (vista global)**: aplicación monolítica en `app.py` (rutas principales: `/` = login, `/register` = registro, `/home` = pantalla principal). Plantillas en `templates/` y recursos estáticos en `static/`.
- **Almacenamiento**: `users.json` en la raíz guarda un diccionario {username: {"email":..., "password":...}}. Las funciones `cargar_usuarios()` y `guardar_usuarios(data)` gestionan lectura/escritura.
- **Autenticación mínima**: no hay base de datos ni hashing de contraseñas (contraseñas en texto plano). La persistencia "recordarme" usa cookie `remember_user` con `max_age=7 días`.

- **Puntos clave de código**:
  - `app.py`: principal punto de entrada. Rutas y lógica de negocio están aquí.
  - `templates/login.html`, `templates/register.html`, `templates/home.html`: renderizados con variables (por ejemplo `user` en `home.html`).
  - `static/css/style.css`, `static/js/main.js`: assets estáticos.

- **Convenciones del proyecto**:
  - Nombres de funciones y comentarios en español (`cargar_usuarios`, `guardar_usuarios`). Mantén la misma lengua en nuevas funciones o comentarios.
  - Manipulación de `users.json` se hace en raíz; evita crear múltiples escritores concurrentes (este repo no soporta concurrencia segura).

- **Cómo ejecutar localmente (dev)**:
  - Entorno: instala Flask si no existe: `pip install flask`.
  - Ejecutar: desde la carpeta del proyecto, `python app.py` (usa `debug=True` ya presente en `app.py`). Accede en `http://127.0.0.1:5000`.

- **Qué mirar antes de cambiar lógica de usuarios**:
  - Verifica `users.json` (estructura) y usa `cargar_usuarios()`/`guardar_usuarios()` para manipularlo.
  - Si agregas hashing o migración de contraseñas, proporciona una ruta de migración y no rompas la lectura directa desde `users.json`.

- **Patrones y ejemplos concretos**:
  - Añadir saludo mostrado en `home`: `user = request.cookies.get("remember_user", "Invitado")` y luego `render_template("home.html", user=user)` — el saludo puede prefijarse en el backend (como ya se hace: `user = f"Hola {user}"`).
  - Registro: en `/register` se evita usuarios duplicados con `if username in users:`.

- **Limitaciones y advertencias** (importante para cambios):
  - Seguridad: contraseñas sin cifrar y sin validación de correo — evita usar en producción.
  - Concurrencia: lectura/escritura de `users.json` no es atómica; para múltiples usuarios concurrentes usar una base de datos o locks.

- **Tareas comunes y ejemplos de cambios**:
  - Para cambiar texto mostrado en `home`, modifica `app.py` (variable `user`) o `templates/home.html` (recomendado para cambios de UI).
  - Para añadir dependencias, agrega `requirements.txt` con `flask` y cualquier paquete nuevo.

Si necesitas que agregue `requirements.txt` o que convierta el almacenamiento a SQLite para concurrencia, dímelo y lo implemento. ¿Hay alguna sección que quieras ampliar o ejemplos adicionales que prefieras? 