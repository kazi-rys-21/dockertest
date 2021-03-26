import boto3


def main():
    # 1 - Create Client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FirstTable')

    response = table.scan()
    data = response['Items']
    print(data)


main()
