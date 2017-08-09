import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

dynamo_client = boto3.client('dynamodb')
dynamo_resource = boto3.resource('dynamodb')

def table_exists():
	tables = dynamo_client.list_tables()
	for table in tables['TableNames']:
		if (table == "shows"):
			return True
	return False

def create_table():
	table = dynamo_client.create_table(
		TableName='shows',
		KeySchema=[
			{
				'AttributeName': 'showID',
				'KeyType': 'HASH'  #Partition key
			},
			{
				'AttributeName': 'showTitle',
				'KeyType': 'RANGE' #Sort Key
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'showID',
				'AttributeType': 'S'
			},
			{
				'AttributeName': 'showTitle',
				'AttributeType': 'S'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 1,
			'WriteCapacityUnits': 1
		}
	)

def list_shows():
	table = dynamo_resource.Table('shows')

	response = table.scan(
	    Select= 'ALL_ATTRIBUTES',
	)

	found_shows = response['Items']
	print(found_shows)

def get_tracked_shows():
	table = dynamo_resource.Table('shows')

	response = table.scan(
	    Select= 'SPECIFIC_ATTRIBUTES',
	    AttributesToGet=['showID'],
	)

	found_shows = response['Items']
	shows = []
	for found_show in found_shows:
		shows.append(found_show['showID'])
	
	return shows

def insert_to_table(show_object):
	table = dynamo_resource.Table('shows')

	table.put_item(
		Item={
		'showID': show_object['show_id'],
		'showTitle': show_object['show_name'],
		'userID': show_object['user_id'],
		'userName': show_object['user_name'],
		}
	)

def add_show(show_object):
	if not table_exists():
		print("Table doesn't exist. Making now.")
		create_table()
	else:
		insert_to_table(show_object)
