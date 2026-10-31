import { defineConfig } from 'vite'

// Configuración de desarrollo y compilación para Vite.js
export default defineConfig({
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: {
      // Redirigir peticiones de API y servicios al backend de Django
      '/api': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      // Proxy para el panel de administración
      '/admin': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
      // Proxy para archivos estáticos generados por Django
      '/static': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
  },
})
