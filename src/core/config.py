import os

# Data Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../../data/hotel_bookings.csv")

# Model Paths
VECTOR_DB_PATH = os.path.join(BASE_DIR, "../../models/faiss_index")

# API Settings
LLM_MODEL_NAME = "facebook/opt-1.3b"  # Change to a smaller model if needed
