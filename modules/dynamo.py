import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', endpoint_url="http://localhost:8000")

def tableExists():
	tables = client.list_tables()
	print(resposne)
	for table in tables['TableNames']:
		if (table == "Shows")
			return True
	return False

def createTable():
	table = dynamodb.create_table(
		TableName='Shows',
		KeySchema=[
			{
				'AttributeName': 'showID',
				'KeyType': 'HASH'  #Partition key
			},
			{
				'AttributeName': 'showTitle',
				'KeyType': 'RANGE'  #Sort key
			}
			],
			AttributeDefinitions=[
			{
				'AttributeName': 'showiD',
				'AttributeType': 'N'
			},
			{
				'AttributeName': 'showTitle',
				'AttributeType': 'S'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 10,
			'WriteCapacityUnits': 10
		}
	)

	print("Table status:", table.table_status)