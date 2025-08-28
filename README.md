# Sistema_login_seguro-Python_bcrypt


Aplicación en Python para **gestionar usuarios con registro, inicio de sesión y validación de contraseñas seguras**.  
El sistema utiliza **bcrypt** para encriptar contraseñas y un archivo CSV como base de datos simple.

## Características

- **Registro de usuarios** con:
  - Validación de nombre de usuario (no numérico, no inicia con número, único).
  - Contraseñas seguras (mín. 8 caracteres, sin espacios, con mayúscula, número y carácter especial).
  - Encriptación de contraseña con **bcrypt**.
- **Inicio de sesión seguro**:
  - Verificación de usuario en archivo CSV.
  - Validación de contraseña encriptada.
  - Bloqueo temporal tras intentos fallidos.
- **Gestión en consola (CLI)**.

## Requisitos

- Python 3.x
- Librería `bcrypt`

Instalación de `bcrypt`:
```bash
pip install bcrypt

	Libre de virus.www.avast.com
