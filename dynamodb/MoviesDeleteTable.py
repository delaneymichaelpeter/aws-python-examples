from __future__ import print_function
import boto3

dynamodb = boto3.resource('dynamodb')
movie_table = dynamodb.Table('Movies')

print("Deleting Movies Table")
movie_table.delete()


