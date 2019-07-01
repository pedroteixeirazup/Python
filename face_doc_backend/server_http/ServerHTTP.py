""" Server HTTP """

import json
import logging
from threading import Thread
import flask
from flask import Flask, request, Response, send_file, url_for, jsonify
from gevent.pywsgi import WSGIServer

from service import file_services, image_detect_face, object_detect_image
from configurator import Configurator
from flask_cors import CORS, cross_origin
import sys
import uuid

APP = Flask(__name__)
APP.image_detect_face = None
CORS(APP)

LOGGING_FORMAT = '%(asctime)s : [%(levelname)s] : %(message)s'


@APP.route('/feedback', methods=['POST'])
# @cross_origin()
def feedback():
    try:
        feedback = request.json['feedback']
        id_image = request.json['image_id']
        # id_prediction = request.json['prediction_id']
    except:
        print('Error on feedback, try again')
    return jsonify({'status': 200})

@APP.route('/predict', methods=['POST'])
# @cross_origin()
def upload_base64():
    try:    
        validation = "validImage"
        base64_string = request.json['base64']
        file_services.decode_to_image(base64_string)
        conf = image_detect_face.detect_face('out.jpg')
        conf = file_services.normalize_conf(conf)
        conf_doc = object_detect_image.detect_object('out.jpg')

        if not conf or conf_doc is None:
            validation = "invalidImage"
            conf_doc = 0
    except:
        print('Error on predict the image, try again.')
        
    return jsonify({'image_id': uuid.uuid4(), 'confiance_face': conf, 'confiance_doc': float(round(conf_doc*100,2)), 'status': 200, 'validation': validation })



class ServerHTTP(Thread):
    """ Server HTTP """
    def __init__(self):
        Thread.__init__(self)
        self.setName('HTTPServer-' + self.getName())

    def run(self):
        config = Configurator.Configurator.get_instance()
        if config['environment'] == 'production':
            logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)
            APP.config['FLASK_ENV'] = config['environment']
            APP.config['ENV'] = config['environment']
            APP.config['FLASK_DEBUG'] = False
            http_server = \
                WSGIServer((config['httpServer']['host'],config['httpServer']['port'], APP))
            if not config['httpServer']['host']:
                host = 'http://0.0.0.0'
            else:
                host = config['httpServer']['host']
            logging.info('WSGIServer starting:')
            logging.info('* Serving WSGIServer app %s', self.getName())
            logging.info('* Environment: %s', APP.config['ENV'])
            logging.info('* Running on %s:%s',host, str(config['httpServer']['port']))
            http_server.serve_forever()
        else:
            logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
            APP.config['FLASK_ENV'] = 'development'
            APP.config['ENV'] = 'development'
            APP.config['FLASK_DEBUG'] = True
            APP.run(host=config['httpServer']['host'],
                    debug=config['httpServer']['debug'],
                    port=config['httpServer']['port'],
                    threaded=True,
                    use_reloader=False)

