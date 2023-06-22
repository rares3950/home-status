from flask import Flask, render_template, session, flash, jsonify
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import os

try:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, "servers.yaml")

    with open(config_path, "r") as f:
        servers = load(f, Loader=Loader)
except FileNotFoundError:
    print("Configuration not found. Are you sure you configured the service according to the handbook?")
    exit()

def pingIP(ip):
    response = os.system("ping -c 1 " + ip)
    return response

app = Flask(__name__)

@app.route('/ping/<identifier>')
def ping(identifier):
    try:
        ping = pingIP(servers["servers"][identifier]["localip"])
        if ping == 0:
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'down'})
    except:
        return jsonify({'error': 'server not found'})

@app.route('/')
def index():
    return render_template("index.html", servers=servers['servers'])