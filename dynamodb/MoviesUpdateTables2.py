from __future__ import print_function
import boto3
import json
import decimal
from botocore.exceptions import ClientError


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('Movies')

title = "The Big New Movie"
year  = 2015

print("Attempting Conditional Update")
try:
    response = table.update_item(
        Key={
            'year'  : year,
            'title' : title
        },
        UpdateExpression="remove info.actors[0]",
        ConditionExpression="size(info.actors) >= :num",
        ExpressionAttributeValues={
            ':num': 3
        },
        ReturnValues="UPDATED_NEW"
    )
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("PutItem succeeded:")
    print(json.dumps(response, cls=DecimalEncoder))


print("PutItem succeeded:")
#print(json.dumps(response, cls=DecimalEncoder))
