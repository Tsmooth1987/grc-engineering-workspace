#!/bin/bash

# AWS Security Hub Custom Controls - Deployment Script
# Deploys custom controls infrastructure using CloudFormation

set -e

# Configuration
PROJECT_NAME="security-hub-custom-controls"
ENVIRONMENT="dev"
REGION="us-east-1"
STACK_NAME="${PROJECT_NAME}-${ENVIRONMENT}"
TEMPLATE_FILE="deployment/template.yaml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "AWS Security Hub Custom Controls Deployment"
echo "=========================================="
echo ""

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo -e "${RED}Error: AWS CLI is not installed${NC}"
    exit 1
fi

# Check if user is authenticated
echo "Checking AWS authentication..."
if ! aws sts get-caller-identity &> /dev/null; then
    echo -e "${RED}Error: AWS authentication failed. Please run 'aws configure'${NC}"
    exit 1
fi

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo -e "${GREEN}✓ Authenticated as account: ${ACCOUNT_ID}${NC}"
echo ""

# Validate CloudFormation template
echo "Validating CloudFormation template..."
aws cloudformation validate-template --template-body file://${TEMPLATE_FILE} > /dev/null
echo -e "${GREEN}✓ Template validation successful${NC}"
echo ""

# Package Lambda function (if using external file)
echo "Packaging Lambda function..."
# For now, the Lambda code is embedded in the template
echo -e "${GREEN}✓ Lambda code embedded in template${NC}"
echo ""

# Deploy CloudFormation stack
echo "Deploying CloudFormation stack..."
aws cloudformation deploy \
  --template-file ${TEMPLATE_FILE} \
  --stack-name ${STACK_NAME} \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    ProjectName=${PROJECT_NAME} \
    Environment=${ENVIRONMENT} \
    EnableMonitoring=true \
  --region ${REGION}

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Stack deployment successful${NC}"
    echo ""
    
    # Get stack outputs
    echo "Stack Outputs:"
    aws cloudformation describe-stacks \
      --stack-name ${STACK_NAME} \
      --query 'Stacks[0].Outputs' \
      --output table
    
    echo ""
    echo -e "${GREEN}=========================================="
    echo "Deployment Complete!"
    echo "==========================================${NC}"
    echo ""
    echo "Next Steps:"
    echo "1. Test the Lambda function:"
    echo "   aws lambda invoke --function-name ${PROJECT_NAME}-custom-controls-${ENVIRONMENT} response.json"
    echo ""
    echo "2. Monitor CloudWatch logs:"
    echo "   aws logs tail /aws/lambda/${PROJECT_NAME}-custom-controls-${ENVIRONMENT} --follow"
    echo ""
    echo "3. Integrate with Security Hub:"
    echo "   Update Security Hub custom controls configuration"
    echo ""
else
    echo -e "${RED}✗ Stack deployment failed${NC}"
    exit 1
fi