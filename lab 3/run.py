from core import create_app
from flask_cors import CORS

app = create_app()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}}, methods= ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)