item_schema = {
    'code': {
        'type': 'string',
        'minlength': 6,
        'maxlength': 6,
        'required': True,
        'unique': True,
    },

    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 32,
        'required': True
    },

    'users': {
        "type": "list",
        "schema": {
            'type': 'dict',
            'schema': {
                'user': {
                    'type': "dbref"
                },
                'first_used': {
                    'type': 'datetime'
                }
            }
        }
    },

    'location': {
        'type': 'dbref'
    },

    'invoice': {
        'type': 'string'
    },

    'details': {
        'type': 'string'
    }
}

item = {
    'item_title': 'item',

    'additional_lookup': {
        'url': 'regex("[\w]+[\d]+")', #TODO: improve regular expression and add it as a check
        'field': 'code'
    },

    # We choose to override global cache-control directives for this resource.
    # default options in example
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': item_schema
}

user_schema = {
    "name": {
        "type": "string"
    },
    "email": {

    }
}

user = {
    "schema": user_schema
}

location_schema = {
    "address": {
        "type": "string"
    }
}

location = {
    "schema": location_schema
}

