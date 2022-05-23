import os
from dotenv import dotenv_values
from flask import Flask, jsonify, render_template, request,Blueprint
from app.endpoints.iss_endpoint import isscheck



app = Flask(__name__,template_folder='app/templates')

@app.route('/')
def index():
      plp=isscheck()
      return render_template("index.html",plp=plp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)