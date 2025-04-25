class FilterModule(object):
    def filters(self):
        return {
            'process_ontap_info': self.process_ontap_info
        }

    def process_ontap_info(self, ontap_info):
        result = {}
        for key, value in ontap_info.items():
            if isinstance(value, dict) and 'records' in value and value['records'] == []:
                result[key] = []
            elif isinstance(value, dict) and 'records' in value and isinstance(value['records'], list) and len(value['records']) > 0:
                result[key] = value['records'][0]
        return result