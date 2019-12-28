import logging
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    app.logger.debug('debug message')
    app.logger.info('info message')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.critical('critical message')
    return 'Hello World'


if __name__ == "__main__":
 handler = logging.FileHandler('/var/log/example5/app.log')
 handler.setLevel(logging.DEBUG)
 formatter = logging.Formatter('%(asctime)s - %(name)s - % (levelname)s - %(message)s')
 handler.setFormatter(formatter)
 app.logger.addHandler(handler)
 app.logger.setLevel(logging.DEBUG)
 app.run(host='0.0.0.0', port=5000)