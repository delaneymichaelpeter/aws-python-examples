from __future__ import print_function
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

#number_of_movies = movie_table.item_count()
number_of_movies = movie_table.query_count()
print("Number of Movies=", number_of_movies )

response = movie_table.query(
    KeyConditionExpression=Key('year').eq(1986)
)

for i in response['Items']:
    print(i['year'], ":", i['title'] )

