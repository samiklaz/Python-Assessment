import json
from utility import num_to_words, type_checker, filepath_validator

def value_mapper(input_filepath, output_filepath) -> None:
    """
    Maps the attributes of a JSON file to a new format and writes the result to an output file.
    
    Args:
        input_filepath (str): The path to the input JSON file.
        output_filepath (str): The path to the output JSON file.
    """
    # Check if filepaths are valid
    if filepath_validator(input_filepath) and filepath_validator(output_filepath):
        # Read input JSON from input_filepath
        with open(input_filepath) as input_file:
            data = json.load(input_file)
            # Get the "message" attributes or an empty dictionary if it doesn't exist
            message_attrs = data.get("message", {})
            
            output = {}
            attr_num = 0
            
            # Check if the JSON is not empty
            if message_attrs:
                # Iterate over attributes of the "message" key, checking for data types
                for attr, value in message_attrs.items():
                    attr_num += 1
                    output[f"key_{num_to_words[attr_num]}"] = {
                        "type": type_checker(value),
                        "tag": "",
                        "description": "",
                        "required": False
                    }
                
                # Create JSON to be dumped to output_filepath
                output_dataset = json.dumps(output, indent=4)
                # Write to the output_filepath
                with open(output_filepath, 'w') as output_file:
                    output_file.write(output_dataset)
    else:
        return {}

# Example usage:
value_mapper('data/data_1.json', "schema/schema_1.json")
value_mapper('data/data_2.json', "schema/schema_2.json")
