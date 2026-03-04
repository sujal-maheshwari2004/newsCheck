import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    react(),
  ],
  build: {
    outDir: 'dist',
  },
  server: {
    proxy: {
      '/process': 'http://localhost:8000',
    },
  },
  preview: {
    host: true,
    port: 4173,
    allowedHosts: [
      "newscheck-1.onrender.com"
    ]
  }
});
