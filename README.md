# Hotel Booking RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) based chatbot built using FastAPI and integrated with Cohere’s `command-r-plus` language model. It is designed to answer queries related to hotel booking data such as cancellation policies, contact details, reservation trends, and more.

---

##  Features

- **RAG Architecture**: Retrieves relevant context using FAISS before generating an answer.
- **LLM-powered Answers**: Uses Cohere’s `command-r-plus` to answer natural language queries.
- **API Endpoints**:
  - `/api/ask` – Accepts a hotel-related question and returns a detailed, contextual answer.
  - `/api/analytics?metric=<metric>` – Provides pre-computed analytics such as revenue trend, cancellation rate, etc.

---

##  Sample Test Queries & Expected Responses

| Query | Expected Response (Example) |
|-------|-----------------------------|
| **"What is the cancellation policy?"** | "Most hotels allow cancellation up to 24 hours before check-in. However, policies vary by hotel. Please refer to your booking confirmation for specifics." |
| **"How do I contact the hotel?"** | "You can contact the hotel via the phone number or email listed in your booking confirmation. If unavailable, visit the hotel's website for more details." |
| **"Which country has the highest number of bookings?"** | "According to recent data, Portugal has the highest number of hotel bookings in the dataset." |
| **"What is the lead time before bookings are made?"** | "On average, guests book their hotels 80 days in advance. This can vary depending on the season." |
| **"Can I modify my reservation?"** | "Most hotels allow reservation changes subject to availability. Contact the hotel directly or use the platform where you made your booking." |

 Note: Responses may vary slightly depending on the context retrieved.

---

##  Setup Instructions

1. Clone the repo:
   ``
   git clone https://github.com/your-org/hotel-rag-chatbot
   cd hotel-rag-chatbot

2. Install dependencies:
    ``
    pip install -r requirements.txt


3. Run the app:
    ``
    uvicorn main:app --reload

