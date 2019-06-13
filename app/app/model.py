from datetime import datetime
to_date = lambda s: datetime.strptime(s, '%d/%m/%Y')

item_schema = {
    'code': {
        'type': 'string',
        'required': True,
        'unique': True,
        'regex': "[A-Z]{3}_[0-9]{4}"
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
                'name': {
                    'type': "string"
                },
                'id': {
                    'type': "string"
                },
                'usage_start': {
                    'type': 'datetime',
                    'coerce': to_date
                },
                'usage_end': {
                    'type': 'datetime',
                    'coerce': to_date,
                    'nullable': True
                }
            }
        }
    },

    'location': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': "string"
            },
            'id': {
                'type': "string"
            }
        }
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
        'url': 'regex("[A-Z]{3}_[0-9]{4}")',
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
        "type": "string",
        "regex": "\A[a-z0-9\+\-_\.]+@[a-z\d\-.]+\.[a-z]+\Z"
    }
}

user = {
    'item_title': 'user',
    "schema": user_schema,
    'item_methods': ['PATCH', 'PUT', 'DELETE']
}

location_schema = {
    "name": {
        "type": "string",
        "required": True
    },
    "address": {
        "type": "string",
        "required": True
    },
    "description": {
        "type": "string",
        "required": False
    }
}

location = {
    'item_title': 'location',
    "schema": location_schema,
    'item_methods': ['PATCH', 'PUT', 'DELETE'],
}

