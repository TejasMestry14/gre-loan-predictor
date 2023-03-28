app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))