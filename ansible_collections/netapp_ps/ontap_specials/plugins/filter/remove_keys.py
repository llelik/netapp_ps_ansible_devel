import json

class FilterModule(object):
    def filters(self):
        return {
            'remove_keys': self.remove_keys
        }

    def remove_keys(self, json_input, keys_to_remove):
        def _remove_keys(data):
            if isinstance(data, dict):
                return {
                    key: _remove_keys(value)
                    for key, value in data.items()
                    if key not in keys_to_remove
                }
            elif isinstance(data, list):
                return [_remove_keys(item) for item in data]
            else:
                return data

        try:
            parsed_json = json.loads(json_input)
            filtered_json = _remove_keys(parsed_json)
            return json.dumps(filtered_json)
        except Exception as e:
            raise ValueError(f"Failed to remove keys: {e}")