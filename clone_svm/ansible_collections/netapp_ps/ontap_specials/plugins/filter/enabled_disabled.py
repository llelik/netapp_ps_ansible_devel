
def enabled_disabled(value):
    if isinstance(value, bool):
        return 'enabled' if value else 'disabled'
    elif isinstance(value, str):
        if value.lower() in ['yes', 'true']:
            return 'enabled'
        elif value.lower() in ['no', 'false']:
            return 'disabled'
    return value

class FilterModule:
    def filters(self):
        return {
            'enabled_disabled': enabled_disabled
        }