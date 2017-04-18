from flask import Flask, jsonify, request
from core import sincedb, errors
import logging

app = Flask(__name__)
logger = logging.getLogger('app')


@app.route('/')
def index():
    return 'Sincedb status. Try getting with /status'


@app.route('/status', methods=['GET'])
def status():
    logger.debug('Got request to fetch status...')
    if request.args.get('sincedb') is None or request.args.get('path') is None:
        raise errors.SincedbServiceError('Parameters path and sincedb are mandatory', status_code=400)

    logger.info('Sincedb: %s, Path: %s' % (request.args.get('sincedb'), request.args.get('path')))
    try:
        parsed_sincedb = sincedb.parse_sincedb(request.args.get('sincedb'))
        all_files = sincedb.get_files(request.args.get('path'))
        merged_status = sincedb.merge_path_stats(parsed_sincedb, all_files,
                                                 ignore_missing=request.args.get('ignore_missing'))
        logger.debug(jsonify(merged_status))
        return jsonify(merged_status)
    except Exception as e:
        raise errors.SincedbServiceError('Error while retrieving status: {0}'.format(e), status_code=500)


@app.errorhandler(errors.SincedbServiceError)
def handle_error(e):
    print(e)
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', debug=True)
