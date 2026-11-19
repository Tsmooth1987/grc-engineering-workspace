"""
Tests for Custom Security Hub Controls
"""

import pytest
import json
import sys
import os
from unittest.mock import Mock, patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from custom_controls.custom_compliance_control import CustomComplianceControl


class TestCustomComplianceControl:
    """Test suite for custom compliance control"""

    @patch('custom_controls.custom_compliance_control.boto3.client')
    def test_control_initialization(self, mock_boto3_client):
        """Test control initialization"""
        test_event = {
            'accountId': '291846646255',
            'region': 'us-east-1',
            'action': 'SECURITY_HUB_CONTROL'
        }

        control = CustomComplianceControl(test_event)
        assert control.event == test_event
        assert control.compliance_rules is not None

    @patch('custom_controls.custom_compliance_control.boto3.client')
    def test_compliance_rules_loading(self, mock_boto3_client):
        """Test compliance rules are loaded correctly"""
        test_event = {
            'accountId': '291846646255',
            'region': 'us-east-1'
        }

        control = CustomComplianceControl(test_event)
        assert 's3_versioning' in control.compliance_rules
        assert 's3_encryption' in control.compliance_rules
        assert 'iam_mfa' in control.compliance_rules
        assert 'iam_password_policy' in control.compliance_rules

    @patch('custom_controls.custom_compliance_control.boto3.client')
    def test_s3_bucket_evaluation_structure(self, mock_boto3_client):
        """Test S3 bucket evaluation structure"""
        test_event = {
            'accountId': '291846646255',
            'region': 'us-east-1'
        }

        control = CustomComplianceControl(test_event)

        # Mock bucket
        bucket = {
            'Id': 'arn:aws:s3:::my-bucket',
            'Type': 'AWS::S3::Bucket'
        }

        evaluation = control.evaluate_resource(bucket)
        assert 'resource_id' in evaluation
        assert 'resource_type' in evaluation
        assert 'compliance_status' in evaluation
        assert 'findings' in evaluation
        assert 'evaluated_at' in evaluation

    @patch('custom_controls.custom_compliance_control.boto3.client')
    def test_iam_user_evaluation_structure(self, mock_boto3_client):
        """Test IAM user evaluation structure"""
        test_event = {
            'accountId': '291846646255',
            'region': 'us-east-1'
        }

        control = CustomComplianceControl(test_event)

        # Mock user
        user = {
            'Id': 'arn:aws:iam::291846646255:user/test-user',
            'Type': 'AWS::IAM::User'
        }

        evaluation = control.evaluate_resource(user)
        assert 'resource_id' in evaluation
        assert 'resource_type' in evaluation
        assert 'compliance_status' in evaluation
        assert 'findings' in evaluation

    @patch('custom_controls.custom_compliance_control.boto3.client')
    def test_lambda_handler_structure(self, mock_boto3_client):
        """Test Lambda handler returns proper structure"""
        test_event = {
            'accountId': '291846646255',
            'region': 'us-east-1',
            'action': 'SECURITY_HUB_CONTROL'
        }

        control = CustomComplianceControl(test_event)
        result = control.process_event(test_event)
        assert 'Findings' in result
        assert isinstance(result['Findings'], list)

        # Verify finding structure
        if result['Findings']:
            finding = result['Findings'][0]
            assert 'SchemaVersion' in finding
            assert 'Id' in finding
            assert 'ProductArn' in finding
            assert 'Title' in finding
            assert 'Description' in finding
            assert 'Severity' in finding


if __name__ == "__main__":
    pytest.main([__file__, "-v"])