from src import application
import os

application.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 5000))
application.run(host='0.0.0.0', port = port)
