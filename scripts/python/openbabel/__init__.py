import sys
import warnings
from . import openbabel

__version__ = "3.1.0"

_thismodule = sys.modules[__name__]

class OBProxy(object):
    def __getattr__(self, name):
        if hasattr(_thismodule, name):
            return getattr(_thismodule, name)
        elif hasattr(openbabel, name):
            warnings.warn('"import openbabel" is deprecated, instead use "from openbabel import openbabel"')
            return getattr(openbabel, name)
        else:
            raise AttributeError

sys.modules[__name__] = OBProxy()
