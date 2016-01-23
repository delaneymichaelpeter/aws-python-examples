import boto3

"""
 This Method will create a table using boto3.resource versus boto3.client
 
"""
# Get the Service Resource
dynamodb = boto3.resource('dynamodb')

# Create Table
movie_table = dynamodb.create_table(
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
          'ReadCapacityUnits'  : 5,
          'WriteCapacityUnits' : 5
       })	

# Wait for the table to finished creating
print("Waiting for Movies Table to be created")
movie_table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
print("Table Created", movie_table.item_count)
