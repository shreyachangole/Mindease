import React from 'react';

const Features = () => {
  const features = [
    {
      title: "Mood-Based ChatBot 🤖",
      description: "Chat anonymously with our AI bot that understands your mood and responds with personalized suggestions.",
      color: "from-indigo-500 to-purple-500"
    },
    {
      title: "Music Recommendations 🎵",
      description: "Get songs based on your current mood to uplift, relax, or reflect.",
      color: "from-pink-500 to-red-500"
    },
    {
      title: "Anonymous Journal ✍️",
      description: "Express your thoughts privately. Track your feelings over time with ease.",
      color: "from-green-400 to-emerald-600"
    },
    {
      title: "Supportive Wall 💬",
      description: "Connect anonymously with others experiencing similar feelings.",
      color: "from-yellow-400 to-orange-500"
    },
  ];

  return (
    <section className="py-16 bg-gradient-to-br from-indigo-50 to-pink-100">
      <div className="max-w-6xl mx-auto px-4">
        <h2 className="text-4xl font-extrabold text-center text-indigo-800 mb-14">🌟 Key Features of MindEase</h2>
        
        <div className="grid md:grid-cols-2 gap-10">
          {features.map((feature, index) => (
            <div key={index} className="backdrop-blur-md bg-white/70 border border-white/40 shadow-xl rounded-2xl p-6 transition-transform transform hover:scale-105 duration-300">
              <div className={`w-12 h-12 rounded-full bg-gradient-to-r ${feature.color} flex items-center justify-center text-white text-xl font-bold mb-4`}>
                {feature.title.split(" ")[feature.title.split(" ").length - 1]}
              </div>
              <h3 className="text-2xl font-semibold text-indigo-700 mb-2">{feature.title}</h3>
              <p className="text-gray-700">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
