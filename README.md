# AI Data Tracker Library

The AI Data Tracker library is a Python package that provides a simple and efficient way to track the inputs and outputs of AI systems, store and manage them in a Weaviate database, and perform semantic searches and data reviews.

## Features

- Connect to self-hosted or WCS Weaviate instances.
- Input and output logging with various data instances and extraneous data types.
- Support for creating, updating, and deleting schemas and data objects.
- Perform semantic searches and data reviews.
- Mass export for dataset usage.

## Installation

This library requires Python 3.6 or later. You can install it using pip:

```
pip install ai-data-tracker
```

## Usage

Here's a basic example of how to use the AI Data Tracker library:

```python
from ai_data_tracker import AIDataTracker

# Initialize the AIDataTracker
tracker = AIDataTracker(weaviate_server="https://localhost:8080", username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Define a schema
schema_definition = {
    "classes": [
        {
            "class": "AIInputOutput",
            "properties": [
                {
                    "name": "input",
                    "dataType": ["string"]
                },
                {
                    "name": "output",
                    "dataType": ["string"]
                }
            ]
        }
    ]
}

# Create the schema
tracker.create_schema(schema_definition)

# Add a data object
data_object = {
    "input": "What is the capital of France?",
    "output": "The capital of France is Paris."
}
tracker.add_data_object("AIInputOutput", data_object)

# Search for data objects
search_results = tracker.search_data_objects("AIInputOutput", "capital of France")

# Export data objects to a JSON file
tracker.export_data("AIInputOutput", output_file="exported_data.json")
```

## API Reference

### `AIDataTracker(weaviate_server, username=None, password=None)`

Initialize the AI Data Tracker instance.

**Parameters:**

- `weaviate_server` (str): The Weaviate instance URL.
- `username` (str, optional): The username for the Weaviate instance.
- `password` (str, optional): The password for the Weaviate instance.

### `create_schema(schema_definition)`

Create a schema in the Weaviate instance.

**Parameters:**

- `schema_definition` (dict): The schema definition.

### `delete_schema()`

Delete the entire schema in the Weaviate instance.

### `add_data_object(class_name, data_object)`

Add a data object to the Weaviate instance.

**Parameters:**

- `class_name` (str): The class name in which the data object will be added.
- `data_object` (dict): The data object to be added.

### `update_data_object(class_name, uuid, data_object)`

Update a data object in the Weaviate instance.

**Parameters:**

- `class_name` (str): The class name of the data object.
- `uuid` (str): The UUID of the data object to be updated.
- `data_object` (dict): The updated data object.

### `get_data_object(class_name, uuid, properties=None)`

Get a data object from the Weaviate instance.

**Parameters:**

- `class_name` (str): The class name of the data object.
- `uuid` (str): The UUID of the data object.
- `properties` (list, optional): The list of properties to retrieve.

### `delete_data_object(class_name, uuid)`

Delete a data object from the Weaviate instance.

**Parameters:**

- `class_name` (str): The class name of the data object.
- `uuid` (str): The UUID of the data object to be deleted.

### `search_data_objects(class_name, query, properties=None)`

Search for data objects in the Weaviate instance.

**Parameters:**

- `class_name` (str): The class name to search in.
- `query` (str): The search query.
- `properties` (list, optional): The list of properties to retrieve.

### `export_data(class_name, properties=None, output_file="output.json")`

Export data objects from the Weaviate instance to a JSON file.

**Parameters:**

- `class_name` (str): The class name to export.
- `properties` (list, optional): The list of properties to retrieve.
- `output_file` (str, optional): The output file name. Default is "output.json".