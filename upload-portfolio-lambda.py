import json
import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-2:188099064930:DeployPortfolioTopic')

    try:
        s3 = boto3.resource('s3')

        portfolio_bucket = s3.Bucket('portfolio.westlea.info')
        build_bucket = s3.Bucket('portfoliobuild.westlea.info')

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "Job done!"
        topic.publish(Subject="Success - Portfolio Deployed", Message="The Portfolio changes were deployed successfully.")
    except:
        topic.publish(Subject="Failed to Deploy Portfolio", Message="The Portfolio changes were not deployed.")
        raise
    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
