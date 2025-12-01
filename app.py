from flask import Flask, render_template, request, redirect, url_for, make_response
from flask import session
import json
import os

app = Flask(__name__)

app.secret_key = "clave-super-secreta"

# --- Cargar o crear un archivo para almacenar usuarios ---
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)


def cargar_usuarios():
    with open("users.json", "r") as f:
        return json.load(f)


def guardar_usuarios(data):
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)


# --- Ruta principal: Login ---
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = cargar_usuarios()

        user_input = request.form["user"]
        password = request.form["password"]
        remember = request.form.get("remember")

        # Verificar credenciales
        for username, info in users.items():
            if (username == user_input or info["email"] == user_input) and info["password"] == password:
                session["user"] = username
                resp = make_response(redirect(url_for("home")))

                if remember:
                    resp.set_cookie("remember_user", username, max_age=60*60*24*7)  # 7 días
                    
                return resp

        return render_template("login.html", error="Usuario o contraseña incorrectos")

    return render_template("login.html")


# --- Crear usuario ---
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = cargar_usuarios()

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Validaciones
        if username in users:
            return render_template("register.html", error="El usuario ya existe")

        if password != confirm_password:
            return render_template("register.html", error="Las contraseñas no coinciden")

        # Guardar usuario nuevo
        users[username] = {"email": email, "password": password}

        guardar_usuarios(users)

        return redirect("/")

    return render_template("register.html")



# --- Pantalla principal después del login ---
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/edit_user")
def edit_user():
    return render_template("edit_user.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/logout")
def logout():
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
