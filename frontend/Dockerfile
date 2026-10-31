# =============================================
# Dockerfile - Frontend Vite.js
# =============================================
FROM node:22-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar código fuente
COPY . .

# Puerto de Vite dev server
EXPOSE 5173

# Comando por defecto (dev server)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

