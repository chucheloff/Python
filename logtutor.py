import logging

print('welcome to logger - bogger wtf is # NOTE: doing in here')

# THOSE ARE ATOM BUILT-IN HELPERS:
# NOTE: well, where does it go
# WARNING: why you gotta do me like that
# TODO: this might be helpful in some cases


# LOGGER LEVELS FOR logging.basicConfig(level,force) setup
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0

print('\nsetting NOTSET level\n')
logging.basicConfig( level = logging.NOTSET )
logging.warning('HeLP')
logging.debug('greta van fleet')
logging.info('logging info level')
logging.error('nice')
logging.log(msg = 'just log, okay?', level = logging.NOTSET)

print('\nsetting ERROR level\n')
logging.basicConfig( level = logging.ERROR, force = True)
logging.warning('HeLP')
logging.debug('greta van fleet')
logging.info('logging info level')
logging.error('nice')
logging.log(msg = 'just log, okay?', level = logging.NOTSET)

print('\nsetting DEBUG level\n')
logging.basicConfig( level = logging.DEBUG, force = True)
logging.warning('HeLP')
logging.debug('greta van fleet')
logging.info('logging info level')
logging.error('nice')
logging.log(msg = 'just log, okay?', level = logging.NOTSET)

print('\nsetting WARNING level\n')
logging.basicConfig( level = logging.WARNING, force = True)
logging.warning('HeLP')
logging.debug('greta van fleet')
logging.info('logging info level')
logging.error('nice')
logging.log(msg = 'just log, okay?', level = logging.NOTSET)

print('\nsetting INFO level\n')
logging.basicConfig( level = logging.INFO, force = True)
logging.warning('HeLP')
logging.debug('greta van fleet')
logging.info('logging info level')
logging.error('nice')
logging.log(msg = 'just log, okay?', level = logging.NOTSET)

# i see what you can do and its scary  but beautiful
