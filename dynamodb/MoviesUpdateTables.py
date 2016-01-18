from __future__ import  print_function
import boto3
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, 
self).default(o)

client   = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

movie_table = dynamodb.Table('Movies')
print("Movie Table=", movie_table )
print("")

print("Load New Item")
title = "The Big New Movie"
year  = 2015 
theInfo = "{ 'plot' : 'Nothing happens at all.' }"

response = movie_table.put_item(
    Item={
        'year'  : year,
        'title' : title,
        'info'  : { 'plot'   : 'One More Time Nothing happens at all.', 
                    'rating' : decimal.Decimal(0),
                    'actors' : ["Larry", "Mo", "Curly"]
                }
    }
)

response = movie_table.get_item(
    Key={
        'year' : year,
        'title': title
    }
)
item = response['Item']
print("SPIT OUT CONTENTS")
print(json.dumps(item, cls=DecimalEncoder))
                          
