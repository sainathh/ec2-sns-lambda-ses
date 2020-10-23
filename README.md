# ec2-sns-lambda-ses

httpd-status file -> check the Apache web server status
  This file triggers two scenarioes. 
  Scenario-1: ec2-sns-lambda-ses using lambda_function.py as handler to ses
  Scenario-2: ec2-ses -> Directly send the mail to ses using the default template.
  Based on that scenarioes, comment the lines in httpd-status file

# Execution Process
`` bash httpd-status
