import json
import uuid

import weaviate


class AIDataTracker:
    def __init__(self, weaviate_server="https://localhost:8080", username=None, password=None):
        if username and password:
            auth_config = weaviate.AuthClientPassword(username=username, password=password)
            self.client = weaviate.Client(weaviate_server, auth_client_secret=auth_config)
        else:
            self.client = weaviate.Client(weaviate_server)

    def create_schema(self, schema_definition):
        self.client.schema.create(schema_definition)

    def delete_schema(self):
        self.client.schema.delete_all()

    def add_data_object(self, class_name, data_object):
        obj_id = str(uuid.uuid4())
        data_object["uuid"] = obj_id
        self.client.data_object.create(class_name=class_name, data_object=data_object, uuid=obj_id)

    def update_data_object(self, class_name, uuid, data_object):
        self.client.data_object.update(class_name=class_name, uuid=uuid, data_object=data_object)

    def get_data_object(self, class_name, uuid, properties=None):
        return self.client.data_object.get(class_name=class_name, uuid=uuid, properties=properties)

    def delete_data_object(self, class_name, uuid):
        self.client.data_object.delete(class_name=class_name, uuid=uuid)

    def search_data_objects(self, class_name, query, properties=None):
        return self.client.query.get(class_name=class_name, properties=properties).with_near_text(
            {"concepts": query, "certainty": 0.6}).do()["data"]["Get"][class_name]

    def export_data(self, class_name, properties=None, output_file="output.json"):
        data_objects = self.client.query.get(class_name=class_name, properties=properties).do()["data"]["Get"][
            class_name]
        with open(output_file, 'w') as f:
            f.write(json.dumps(data_objects, indent=2))