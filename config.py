import os


class Config:
    '''
    General configuration parent class
    '''

    QUOTES_API_URL = 'http://quotes.stormconsultancy.co.uk/popular.json'


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General confirguration settings

    '''

    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General confirguration settings

    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
