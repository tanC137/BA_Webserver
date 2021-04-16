#IMPORTS
from flask import Flask
from flask import request
from flask import redirect
from flask import Response
from flask_talisman import Talisman
from datetime import datetime

#Initilize Flask
app = Flask(__name__)
Talisman(app)

@app.route("/", methods=['GET'])
def hello_world():
    if request.method == "GET":
        useragent = request.headers.get('User-Agent')
        if useragent == "h4ck3r":
            status_code = Response(status=403)
            return status_code
        else:
            dt_str = datetime.now().strftime("Date: %m/%d/%Y | Time: %H:%M")
            ret = f"Hello World {dt_str}"
            return ret

#Run flask webserver
if __name__ == "__main__":
    #app.run(port = 5050, host='0.0.0.0', ssl_context=('C:\\Users\\talukta\\Projects\\BA_Webserver\\app\\cert.pem', 'C:\\Users\\talukta\\Projects\\BA_Webserver\\app\\key.pem'))
    app.run(port = 5050, host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))