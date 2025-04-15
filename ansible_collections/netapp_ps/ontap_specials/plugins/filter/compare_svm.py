import json

class FilterModule(object):
    def filters(self):
        return {
            'compare_svm': self.compare_svm
        }

    def compare_svm(self, var1, var2, ignore_params):
        # Convert variables to dictionaries
        dict1 = json.loads(var1)
        dict2 = json.loads(var2)

        # Recursively compare dictionaries
        def compare_dicts(d1, d2):
            diff = {}
            for key in set(d1.keys()) | set(d2.keys()):
                if key in ignore_params:
                    continue

                if key not in d2:
                    diff[key] = d1[key]
                elif key not in d1:
                    diff[key] = d2[key]
                elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    nested_diff = compare_dicts(d1[key], d2[key])
                    if nested_diff:
                        diff[key] = nested_diff
                elif d1[key] != d2[key]:
                    diff[key] = d1[key]

            return diff

        # Perform the comparison
        diff_result = compare_dicts(dict1, dict2)

          # Remove ignored parameters with empty list values
        for param in ignore_params:
            if param in diff_result and diff_result[param] == []:
                del diff_result[param]


        return json.dumps(diff_result)