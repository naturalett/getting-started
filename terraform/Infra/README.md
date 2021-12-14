# Infra modules
- aws-opsworks
- aws-opsworks-instance
- ELB-as-a-module
- ELB-as-a-resource


## Prerequisits
- aws account configured with `aws configure`
- [jq](https://stedolan.github.io/jq/)

## SSM Parameters
1. Get familiar with [AWS-SSM](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html#get-parameter)
2. Create SSM Parameters:
    ```bash
    aws ssm put-parameter --name cred_aws_access_key --value <VALUE>
    aws ssm put-parameter --name cred_aws_secret_key --value <VALUE>
    ```
3. Connect to your EC2:
    ```bash
    export AWS_DEFAULT_REGION=us-east-1
    export AWS_ACCESS_KEY_ID=$(aws ssm get-parameter --name cred_aws_access_key | jq '.Parameter.Value')
    export AWS_SECRET_ACCESS_KEY=$(aws ssm get-parameter --name cred_aws_secret_key | jq '.Parameter.Value')
    ```

## aws-opsworks
Great example: https://github.com/AirWalk-Digital/terraform-aws-opsworks
