from core import create_app
from flask_cors import CORS

app = create_app()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}}, methods= ['GET', 'POST', 'PUT', 'DELETE'])

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs.txt", format="%(asctime)s: %(message)s", level=logging.INFO)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)