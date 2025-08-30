import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import {createBrowserRouter,RouterProvider}  from 'react-router-dom' ;

import Home from './Pages/Home';
import NotFoundPage from './Errors/NotFoundPage';


const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "*", element: <NotFoundPage /> },

]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
