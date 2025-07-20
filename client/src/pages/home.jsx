import React from 'react';
import Navbar from '../components/nav';

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-r from-indigo-200 via-purple-200 to-pink-200">
      <Navbar />
      <div className="flex flex-col items-center justify-center h-[80vh] px-4">
        <h1 className="text-5xl font-bold text-gray-800 mb-6 text-center">
          Welcome to MindEase 🧠
        </h1>
        <p className="text-xl text-gray-700 max-w-2xl text-center mb-8">
          Your mental well-being companion. Share your feelings, track your thoughts, and connect with supportive resources.
        </p>
      </div>
    </div>
  );
};

export default Home;
