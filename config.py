class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    MONGO_URI = 'mongodb://localhost:27017/default_db'

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/dev_db'

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/test_db'

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://localhost:27017/prod_db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}