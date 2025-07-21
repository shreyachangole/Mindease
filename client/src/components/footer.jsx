import React, { useState } from 'react';

const faqs = [
  {
    question: "Is MindEase completely anonymous?",
    answer: "Yes, we don’t require any personally identifiable information. Your entries and chats are secure."
  },
  {
    question: "Can I talk to a real therapist?",
    answer: "Currently, MindEase offers AI-powered mental wellness support. We may partner with certified professionals soon."
  },
  {
    question: "Is this app free to use?",
    answer: "Yes, MindEase is completely free for all core features like journaling, music suggestions, and chatbot support."
  },
  {
    question: "How do you suggest songs?",
    answer: "Our system uses mood classification based on your entries or chat and gives relevant music via API integration."
  }
];

const Footer = () => {
  const [openIndex, setOpenIndex] = useState(null);

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <footer className="bg-indigo-950 text-white py-12 mt-20">
      <div className="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12">
        {/* Left section */}
        <div>
          <h2 className="text-3xl font-bold mb-4">MindEase 💜</h2>
          <p className="text-gray-300">Your companion in mental well-being. We’re here to support, uplift, and empower you.</p>
          <p className="text-gray-400 mt-4">© {new Date().getFullYear()} MindEase. All rights reserved.</p>
        </div>

        {/* FAQ section */}
        <div>
          <h3 className="text-2xl font-semibold mb-6 text-indigo-300">FAQs ❓</h3>
          {faqs.map((faq, index) => (
            <div key={index} className="mb-4">
              <button
                onClick={() => toggleFAQ(index)}
                className="w-full text-left focus:outline-none text-lg font-medium text-white hover:text-indigo-300"
              >
                {faq.question}
              </button>
              <div className={`text-gray-300 mt-2 transition-all duration-300 ${openIndex === index ? 'max-h-40 opacity-100' : 'max-h-0 overflow-hidden opacity-0'}`}>
                {faq.answer}
              </div>
              <hr className="border-indigo-600 my-2" />
            </div>
          ))}
        </div>
      </div>
    </footer>
  );
};

export default Footer;
