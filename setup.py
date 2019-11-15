from distutils.core import setup
import py2exe
 
setup(
    console=['medvisor.py'],
    options = {
        'py2exe': {
            'packages': ['torch', 'pandas', 'numpy', 'xgboost', 'sklearn']
        }
    }
)