from dotenv  import load_dotenv
import os

load_dotenv()
user=os.environ["MONGO_USER"]
password=os.environ["MONGO_PASSWORD"]
database=os.environ["MONGO_DB"]


DEBUG=True
MONGO_URI=f"mongodb+srv://{user}:{password}@cluster0.0o6r9.mongodb.net/{database}?retryWrites=true&w=majority"

