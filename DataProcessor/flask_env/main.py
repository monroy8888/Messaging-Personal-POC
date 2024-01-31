from flask import Flask, jsonify
from connectionmq.connection_prepro_rmq import consume_rabbitmq, initialize_rabbitmq

app = Flask(__name__)


@app.route("/rabbit", methods=["GET"])
def rabbit_message():
    body = consume_rabbitmq()
    if body is not None:
        result = body.decode()
        return jsonify({"result": result})
    else:
        return jsonify({"result": "No results."})


@app.before_first_request
def before_first_request():
    initialize_rabbitmq()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)