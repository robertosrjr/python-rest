from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from api.controller.userController import UserController

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://127.0.0.1:5000/spec'  # Our API url (can of course be a local resource)

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My First Rest API in Pyhton"
    swag['info']['description'] = "Python 3.8 + Flask + Swagger"
    return jsonify(swag)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

controller = UserController()
@app.route('/users')
def get():
  return controller.get()

def initialize_app(app):
  app.config['RESTPLUS_VALIDATE'] = True
  app.config['ERROR_404_HELP'] = False

def main():
  initialize_app(app)
  app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == "__main__":
    main()