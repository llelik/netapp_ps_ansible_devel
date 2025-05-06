class FilterModule:
    def filters(self):
        return {
            'dash_to_empty': self.dash_to_empty
        }

    def dash_to_empty(self, value):
        if value is None:
            return ''
        elif isinstance(value, str) and value == '-':
            return ''
        return value