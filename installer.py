#This script installs all the python package requirements

import importlib.util
import sys
import subprocess

package_name = 'selenium'
spec = importlib.util.find_spec(package_name)

if spec is None:
    subprocess.check_call(["python", '-m', 'pip', 'install', package_name]) # install pkg

package_name = 'chromedriver'
spec = importlib.util.find_spec(package_name)

if spec is None:
    subprocess.check_call(["python", '-m', 'pip', 'install', package_name]) # install pkg

package_name = 'gspread'
spec = importlib.util.find_spec(package_name)

if spec is None:
    subprocess.check_call(["python", '-m', 'pip', 'install', package_name]) # install pkg

package_name = 'oauth2client'
spec = importlib.util.find_spec(package_name)

if spec is None:
    subprocess.check_call(["python", '-m', 'pip', 'install', package_name]) # install pkg

package_name = 'geopy'
spec = importlib.util.find_spec(package_name)

if spec is None:
    subprocess.check_call(["python", '-m', 'pip', 'install', package_name]) # install pkg
