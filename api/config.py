from decouple import config


class Config:
    MYSQL_HOST = config('MYSQL_HOST')


class dev(Config):
    DEBUG = True


class pro(Config):
    DEBUG = False


config1 = {
    'dev': dev,
    'pro': pro
}
