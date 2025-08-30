import React from "react";
import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100 text-gray-800">
      <h1 className="text-9xl font-extrabold text-gray-700">404</h1>
      <p className="text-2xl md:text-3xl font-light mt-4">Oops! Page not found</p>
      <p className="text-gray-500 mt-2">
        The page you are looking for doesn’t exist or has been moved.
      </p>
      <Link
        to="/"
        className="mt-6 px-6 py-3 rounded-2xl bg-red-600 text-white text-lg font-medium shadow hover:bg-red-700 transition"
      >
        Go Home
      </Link>
    </div>
  );
}
