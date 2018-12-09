import os
environment = os.getenv('ENVIRONMENT', 'dev')

from .base_settings import *

if environment == 'dev':
    from .dev_settings import *

if environment == 'prod':
    from .prod_settings import *

from .base_templates import *
