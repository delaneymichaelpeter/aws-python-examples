
import boto3
import time
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB itme to json
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)



client   = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')



movie_table = dynamodb.Table('Movies')
print("Movie Table=", movie_table )
print("Print Movies in 1985")

response = movie_table.query(
    ProjectionExpression="#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames={"#yr" : "year"},
    KeyConditionExpression=Key('year').eq(2013) & Key('title').between('A', 'L')
)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

