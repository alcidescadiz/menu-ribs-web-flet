#!/usr/bin/env bash
set -e

# 1. Instalar Flutter SDK localmente en el entorno de compilación
echo "Instalando Flutter..."
git clone https://github.com/flutter/flutter.git -b stable --depth 1 _flutter
export PATH="$PATH:`pwd`/_flutter/bin"

# 2. Configurar Flutter para la web
flutter precache --web

# 3. Instalar dependencias de Python
pip install -r requirements.txt

# 4. Compilar la aplicación Flet para Web
flet build web