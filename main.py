from flask import Flask
from flask_restful import Resource, Api, reqparse
import signalk
import uart

ser = uart.start_uart()

app = Flask(__name__)
api = Api(app)

signalkprefix = "/signalk/v1/api"
projectprefix = "/vessels/self/environment/inside"
urlprefix = signalkprefix + projectprefix

class Lights(Resource):
    def get(self):
        data = "There is one onboard LED installed, ID: 1"
        return {'data': data}, 200  # return data and 200 OK code
    
    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('value', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary

        skdata = signalk.put_light_1(args['value'])

        status = uart.send(ser, skdata)
        
        if status == 0:
            return "Light 1 set to " + args['value'] , 200
        
        else:
            return "Some kind of error" , 500

api.add_resource(Lights, urlprefix + '/lights')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')  # run our Flask app