# TrafficWatch

Aplicación de alerta de autos sospechosos reconocido por medio de camaras de vigilancia y inteligencia artificial

## Clonación del Repositorio

### Usando HTTP

```bash
git clone https://github.com/Nispeter/PI_2023-2.git
```

### Usando SSH

```bash
git clone git@github.com:Nispeter/PI_2023-2.git
```
## Frontend

### Requisitos Previos

- Node.js: Debes tener Node.js instalado en tu sistema. Puedes descargarlo desde la página [oficial de Node.js](https://nodejs.org/).

### Instalación de pnpm

pnpm es el administrador de paquetes utilizado para el frontend. Sigue estas instrucciones para instalarlo:

#### Windows

1. Abre PowerShell como administrador.
1. Ejecuta: `iwr https://get.pnpm.io/v6.16.js -useb | node`.

#### Linux

1. Abre la terminal.
1. Ejecuta: `curl -fsSL https://get.pnpm.io/v6.16.js | node - add --global pnpm`.

#### macOS

1. Abre la terminal.
1. Ejecuta: `curl -fsSL https://get.pnpm.io/v6.16.js | node - add --global pnpm`.

### Configuración de Archivo .env

1. En la carpeta del frontend, crea un archivo .env basándote en .env.example.
1. Copia el contenido de .env.example en .env.
1. Modifica los valores en .env según sea necesario.

### Ejecución del Proyecto

1. Navega a la carpeta del frontend.
1. Instala las dependencias con pnpm install.
1. Inicia el proyecto con `pnpm dev`.
1. Accede a la aplicación en http://localhost:5173.

## Backend

### Configuración del Entorno Virtual

1. Asegúrate de tener Python instalado en tu sistema.
1. Navega a la carpeta del backend.
1. Crea un entorno virtual con `python -m venv venv`.
1. Activa el entorno virtual:
    Windows: `.\venv\Scripts\activate`
    Linux/macOS: `source venv/bin/activate`
1. Instala las dependencias con `pip install -r requirements.txt`.

### Ejecución del Backend

1. Con el entorno virtual activado, inicia el backend con `uvicorn app:app`.
1. El servidor del backend ahora debería estar corriendo.