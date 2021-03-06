"""Run the server in development mode."""
from thyme.server import get_instance

if __name__ == "__main__":
    app = get_instance()
    app.secret_key = 'super secret key'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
