#Run this on your console if you havent got Flask yet
#pip3 install flask

from flask import Flask #imports Flask library
#needs Python 2.6 or higher
import os #needed to access global variables stored in Amazon AWS

application = Flask(__name__) #instanting the library

@application.route('/') #tells URL which URL should call the associated function
def hello_world():
    db_name = os.environ['DATABASE_NAME'] #the environment variable key-value pair was created in Configurations > Software in AWS
    return "Hello World"

if __name__ == '__main__': #runs this application
    application.run()
