""" Configurator """

import os
import json
import sys

RELATIVE_CONFIG_FOLDER = './configuration'

class Configurator(object):
    """ Configurator """
    class __Configurator(object):
        """ __Configurator """
        def __init__(self):
            """ Constructor """
            self.config = Configurator.__get_configurations(sys.argv)

        def get_config(self):
            """ Get configuration """
            return self.config

    instance = None

    def __init__(self):
        """ Constructor """
        if not  Configurator.instance:
            Configurator.instance = Configurator.__Configurator()
    
    def __getattr__(self, name):
        """ Get atrribute """
        return getattr(self.instance, name)

    @staticmethod
    def _drop():
        Configurator.instance = None
    
    @staticmethod
    def get_instance():
        """ Get instance """
        if not Configurator.instance:
            Configurator.instance = Configurator.__Configurator()
        return Configurator.instance.config
    
    @staticmethod
    def __get_environment(arguments):
        """ Get environment """
        env = 'development'
        for argument in arguments:
            if argument.startswith('--env='):
                env = argument.rsplit('=', 1)[1]
        return env 
    
    @staticmethod
    def __get_config_from_file(env):
        """ Get configuration from file """
        file_env = os.path.join(RELATIVE_CONFIG_FOLDER, env + '.json')
        if os.path.isfile(file_env):
            with open(file_env, 'r') as file_content:
                return json.load(file_content)
        return {
            "httpServer": {"host": "0.0.0.0", "debug": True, "port": 5000}}

    @staticmethod
    def __get_configurations(arguments):
        """ Get configurations """
        env = Configurator.__get_environment(arguments)
        config = Configurator.__get_config_from_file(env)
        config['environment'] = env
        return config
