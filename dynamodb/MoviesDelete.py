from __future__ import print_function
import boto3
from botocore.exceptions import ClientError
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
            return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')
table = "The Big New Move"
year  = 2015

try:
    response = table.delete_item(
        Key={
            'year' : year,
            'title' : title
        },
        ConditionExpression="info.rating <= :val", 
        ExpressionAttributeValues={ 
            ":val" : decimal.Decimal(5)
        }
)
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("PutItme succeeded:")
    print(json.dumps(response, cls=DecimalEncoder))
