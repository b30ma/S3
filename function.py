### Identify and Delete Unused Objects
import boto3

def delete_unused_objects(bucket_name):
    s3_client = boto3.client('s3')
    
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
    
    print(f"Deleted unused objects in bucket: {bucket_name}")

# Example usage
bucket_name = 'your-s3-bucket-name'
delete_unused_objects(bucket_name)

###Move Objects to Infrequent Access (IA) or Glacier Storage Class
def move_objects_to_ia(bucket_name):
    s3_client = boto3.client('s3')
    
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_client.copy_object(
                Bucket=bucket_name,
                CopySource={'Bucket': bucket_name, 'Key': obj['Key']},
                Key=obj['Key'],
                StorageClass='STANDARD_IA'
            )
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
    
    print(f"Moved objects to Infrequent Access storage class in bucket: {bucket_name}")

# Example usage
bucket_name = 'your-s3-bucket-name'
move_objects_to_ia(bucket_name)
