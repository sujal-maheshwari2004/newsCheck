import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import App from './App.jsx'
import Verify from './Verify.jsx'

import './index.css'

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>

      <Route path="/" element={<App />} />

      <Route path="/verify" element={<Verify />} />

    </Routes>
  </BrowserRouter>
)
