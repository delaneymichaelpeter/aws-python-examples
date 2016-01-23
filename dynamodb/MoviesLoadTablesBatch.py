"""
 Tried to Implement this, this function loads data via batch mode
 which is better and more effecient

 http://boto3.readthedocs.org/en/latest/guide/dynamodb.html#batch-writing

"""
from __future__ import print_function
import boto3
import time
import json
import decimal

client   = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

movie_table = dynamodb.Table('Movies')
print("Movie Table", movie_table )

#batch_list = movie_table.batch_writer()
#print("Batch List", batch_list)

# Option up Json file
with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal )
    for movie in movies:
        year  = int( movie['year'] )
        title = movie['title']
        info  = movie['info']
        print("ADDING MOVIE:", year, title, info, "\n" )
        
        # Batch Load 
        with movie_table.batch_writer() as batch:
            batch.put_item(
                Item={ 
                    'year' : year,
                    'title': title,
                    'info' : info,
                }
            )
    






