import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md py-4 px-6 flex justify-between items-center">
      <h1 className="text-2xl font-bold text-indigo-700">MindEase</h1>
      <div className="space-x-4">
        <button className="text-indigo-600 hover:text-indigo-800">Login</button>
        <button className="bg-indigo-600 text-white px-4 py-1 rounded-full hover:bg-indigo-700">Register</button>
      </div>
    </nav>
  );
};

export default Navbar;
