import json
import os
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3_BUCKET = "jb-lamda-testing"

def lambda_handler(event, context):
    logger.info(f'Calling out to {S3_BUCKET} bucket to list objects')
    logger.info(f'event: {event}')
    logger.info(f'context: {context}')

    s3_client = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

    logger.info(f'bucket: {bucket}')
    logger.info(f'key: {key}')
        
    # Get all the objects from the bucket. Max 1000
    objects_in_bucket = s3_client.list_objects(Bucket=S3_BUCKET)

    logger.info('Found {} objects in the bucket. Printing a sample...'.format(len(objects_in_bucket['Contents'])))

    for key in objects_in_bucket['Contents'][:5]:
        logger.info('Found {} in bucket'.format(key['Key']))
