# 🤖 DC BOT

¡Bienvenido a **DC BOT**!  
Un bot de Discord desarrollado en Python, diseñado para ser modular, fácil de mantener y en constante evolución.

## 🚀 Características

- **Comandos personalizados:**  
  Actualmente incluye el comando `$gemini` que utiliza la API de Gemini para generar respuestas inteligentes.
- **Integración con Gemini AI:**  
  Aprovecha el poder de la IA de Google Gemini para responder a tus preguntas o generar contenido.
- **Gestión de variables de entorno:**  
  Uso de `.env` para mantener seguras tus claves y configuraciones sensibles.
- **Código limpio y modular:**  
  Separación de lógica en archivos como `main.py` y `utils.py` para facilitar el mantenimiento y la escalabilidad.

## 📦 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/bot-py.git
   cd bot-py
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. crea un archivo `.env` basado en el `.env.example` y añade tus variables de entorno:
   ```bash
   BOT_ID=tu_id_de_bot
   BOT_TOKEN=tu_token_de_bot
   GEMINI_TOKEN=tu_api_key_de_gemini
   ```

4. Ejecuta el bot:
   ```bash
   python main.py
   ```

## 🛠️ Uso

- En tu servidor de Discord, escribe:
    ```plaintext
    $gemini "<tu_pregunta>"
    ```

El bot responderá con una respuesta generada por la IA de Google Gemini.

**NOTA:** Es importante que la pregunta esté entre comillas dobles para que se interprete correctamente.

## 📚 Estructura del proyecto

```plaintext
bot-py/
├── main.py         # Archivo principal del bot
├── utils.py        # Funciones auxiliares y lógica de Gemini
├── .env.example    # Ejemplo de archivo de variables de entorno
├── .gitignore      # Archivos y carpetas ignorados por git
└── README.md       # Este archivo
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el siguiente apartado para más detalles.

## 🌱 Futuras actualizaciones

Este bot está en constante desarrollo. ¡Pronto se agregarán nuevas funcionalidades, comandos y mejoras! Si tienes ideas o sugerencias, no dudes en abrir un issue o hacer un pull request.