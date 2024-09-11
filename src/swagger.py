from flasgger import Swagger, NO_SANITIZER

swagger_template = {
    "info": {
        "title": "Backend Service",
        "description": "Backend APIs",
        "version": "0.0.1",
    }
}


def configure_swagger(app):
    swagger = Swagger(app, template=swagger_template, sanitizer=NO_SANITIZER)
