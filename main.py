from flask import Flask, request

@app.route('/')
def index():
    return "this is test"