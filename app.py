#import our library and packages
from flask import Flask

#creat Flask instance/application
app = Flask(__name__)

#create our directory
@app.route('/<name>')
def home(name):
  return "Hello " + name

#run our web application
if __name__ == "__main__":
  app.run()