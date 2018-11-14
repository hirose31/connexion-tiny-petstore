# -*- coding: utf-8 -*-

import connexion
import logging

from tiny_petstore import encoder
from tiny_petstore.configs import ProdConfig
from tiny_petstore.extensions import db


def create_app(config_object=ProdConfig):
    logging.basicConfig(level=logging.DEBUG)

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config.from_object(config_object)
    app.add_api('openapi.yaml')

    register_extensions(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)

    # when you want to response your own error response
    # instead ofproblem+json:
    # ref: https://github.com/zalando/connexion/issues/138#issuecomment-206361679
    # @app.app.after_request
    # def rewrite_error_response(response):
    #     if response.mimetype == 'application/problem+json':
    #         body = response.get_json(silent=True)
    #         if body is not None:
    #             response.set_data(json.dumps(error_response(
    #                 code=body['status'],
    #                 message=body['title'],
    #                 detail=body['detail'],
    #             ),
    #                 sort_keys=True,
    #                 indent=4,
    #             ))
    #             response.headers['Content-Type'] = 'application/json'
    #             response.status_code = 200
    #     return response

    return app


def register_extensions(app):
    db.init_app(app.app)
    db.init_db(app.app)


def register_errorhandlers(app):
    pass
    # def errorhandler(error):
    #     response = error.to_json()
    #     response.status_code = error.status_code
    #     return response

    # app.errorhandler(InvalidUsage)(errorhandler)


def register_shellcontext(app):
    pass
    # """Register shell context objects."""
    # def shell_context():
    #     """Shell context objects."""
    #     return {
    #         'db': db,
    #         'User': user.models.User,
    #         'UserProfile': profile.models.UserProfile,
    #         'Article': articles.models.Article,
    #         'Tag': articles.models.Tags,
    #         'Comment': articles.models.Comment,
    #     }

    # app.shell_context_processor(shell_context)


def register_commands(app):
    pass
    # """Register Click commands."""
    # app.cli.add_command(commands.test)
    # app.cli.add_command(commands.lint)
    # app.cli.add_command(commands.clean)
    # app.cli.add_command(commands.urls)
