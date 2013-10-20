from functools import wraps
from flask import Flask, jsonify, current_app, request
import json
import model as Model
import spoof_analytics as analytics
 
app = Flask(__name__)

"""
Taken from:  https://gist.github.com/1094140
"""



def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function
    

@app.route("/")
def hello():
    return "Hello World! Onaserver is alive"
    
@app.route('/param',methods=['GET'])
@jsonp
def p():
    res={
            'd_param':Model.d_param
        }
    return jsonify(res)
    
@app.route('/analytics/pageviews',methods=['GET'])
@jsonp
def pageviews():
    res=analytics.generate_pageview_data(30)
    return jsonify(res)

@app.route('/analytics/timespent',methods=['GET'])
@jsonp
def timespent():
    res=analytics.generate_timespent_data(30)
    return jsonify(res)    
    
if __name__ == "__main__":
    app.run(debug=True)