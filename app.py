from flask import Flask, jsonify, request
from core import sincedb

app = Flask(__name__)


@app.route('/')
def index():
    return 'Sincedb status. Try getting with /status'


@app.route('/status', methods=['GET'])
def status():
    parsed_sincedb = sincedb.parse_sincedb(request.args.get('sincedb'))
    all_files = sincedb.get_files(request.args.get('path'))
    return jsonify(
        sincedb.merge_path_stats(parsed_sincedb, all_files, ignore_missing=request.args.get('ignore_missing')))


if __name__ == '__main__':
    app.run(debug=True)
