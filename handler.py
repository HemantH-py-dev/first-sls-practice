import datetime
import json


def hello(event, context):

    body = dict(
        name="Hemanth",
        DOB="5th April 1998",
        current_time=datetime.datetime.now().strftime("%c"),
    )

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
