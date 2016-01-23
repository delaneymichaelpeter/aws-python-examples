from __future__ import print_function
import boto3
import time
import json
import decimal

client   = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')


print("#####################  Tables ########################")
all_tables = client.list_tables()
print("Table List=", all_tables )
print("")

movie_table = dynamodb.Table('Movies')
print("Movie Table=", movie_table )
print("")


table_name = 'Movies'
if table_name not in all_tables['TableNames']:
    print("Table Movies DOES NOT Exist")

    # Create Movie Table
    print("Create Movies Table")
    movie_table = client.create_table(
        TableName='Movies',
        KeySchema=[
            {
		'AttributeName' : 'year',
                'KeyType'       : 'HASH'  
            },
	    {
               'AttributeName' : 'title',
               'KeyType'       : 'RANGE' 
            }
        ],
        AttributeDefinitions=[
            {
               'AttributeName' : 'year',
               'AttributeType' : 'N'  
            },
            {
              'AttributeName' : 'title',
              'AttributeType' : 'S' 
            }
        ],
       ProvisionedThroughput={
          'ReadCapacityUnits'  : 1,
          'WriteCapacityUnits' : 1
       })	
    movie_table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
    print("Table create status=",  movie_table )
else: 
    print("Table Exits")



"""
# Read data into Movies table
with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal )
    for movie in movies:
        year  = int( movie['year'] )
        title = movie['title']
        info  = movie['info']
        print("ADDING MOVIE:", year, title, info, "\n" )
        movie_table.put_item(
            Item={ 
                'year' : year,
                'title': title,
                'info' : info,
            }
        )

# Put some data into our Table
movies = movie_table.put_item(
	Item={
		'year'  : 2015,
		'title' : 'Revenent',
		'info'  : {'plot' : 'Western sytle'}	
	}
)
print("Add Table data status=",  movies )
"""





