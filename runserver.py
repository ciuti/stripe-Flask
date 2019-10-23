import os
from stripe_flask import app

def runserver():
	port = int(os.environ.get('PORT', 5000))
	app.run(ssl_context=('cert.pem', 'key.pem'),host='0.0.0.0', port=port)

if __name__ == '__main__':
	runserver()
