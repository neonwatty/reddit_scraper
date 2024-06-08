from index import app
import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=3000, host="0.0.0.0")

