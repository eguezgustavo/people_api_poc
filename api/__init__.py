from flask import Flask, request, jsonify

import core
import adapters


def create_api():
    app = Flask(__name__)


    @app.route("/custom-field", methods=["POST"])
    def create_custom_field():
        app = core.PeopleAPICore(
            custom_fields_repository=adapters.MongoCustomFieldRepository(),
            person_repository=None,
        )

        field_data = request.get_json()
        created_field = app.create_custom_field(**field_data)
    
        return created_field._asdict()

    @app.route("/custom-field/<tenant_id>", methods=["GET"])
    def get_custom_fields_for_tenant(tenant_id):
        app = core.PeopleAPICore(
            custom_fields_repository=adapters.MongoCustomFieldRepository(),
            person_repository=None,
        )
    
        return jsonify([field._asdict() for field in app.get_all_for_tenant(tenant_id)])

    @app.route("/person/<tenant_id>", methods=["POST"])
    def create_person(tenant_id):
        app = core.PeopleAPICore(
            custom_fields_repository=adapters.MongoCustomFieldRepository(),
            person_repository=adapters.MongoPersonRepository(),
        )
        person_data = request.get_json()
        name = person_data.pop("name")
        last_name = person_data.pop("last_name")

        created_person = app.create_person(tenant_id, name, last_name, **person_data)
        return created_person._asdict()

    @app.route("/person/<person_id>", methods=["GET"])
    def get_person(person_id):
        app = core.PeopleAPICore(
            custom_fields_repository=None,
            person_repository=adapters.MongoPersonRepository(),
        )

        return app.get_person(person_id)._asdict()

    return app
