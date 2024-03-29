from flask import Flask, request, jsonify
import util

app=Flask(__name__)

@app.route('/get location names')

def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

def hello():
    return "Hi"


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediciton...")
    app.run()