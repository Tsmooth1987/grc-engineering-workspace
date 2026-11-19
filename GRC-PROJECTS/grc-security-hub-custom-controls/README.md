# 🛡️ AWS Security Hub Custom Controls

**Advanced AWS Security Automation - Custom Security Hub Controls Beyond Standard Benchmarks**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Development-yellow)

## 🎯 Overview

Build custom AWS Security Hub controls that go beyond standard FSBP/CIS benchmarks to address specific business requirements and compliance frameworks. This project demonstrates advanced Security Hub expertise and the ability to create tailored security controls for organizational needs.

## ✨ Features

- **Custom Control Development**: Security Hub controls using Python and Lambda
- **CloudFormation Deployment**: Infrastructure as Code for control deployment
- **Compliance Framework Mapping**: Map controls to SOC 2, ISO 27001, NIST CSF
- **Automated Testing**: Testing framework for control validation
- **Custom Framework Support**: Address specific organizational compliance requirements

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- AWS CLI configured with credentials
- Security Hub enabled in AWS account
- Knowledge of Security Hub control architecture

### Installation

```bash
# Clone the repository
git clone https://github.com/Tsmooth1987/grc-security-hub-custom-controls.git
cd grc-security-hub-custom-controls

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Deploy custom controls
./deployment/deploy-controls.sh

# Test custom controls
python -m pytest tests/

# Validate controls in Security Hub
python -m pytest tests/test_validation.py
```

## 🏗️ Architecture

```
Custom Control → Lambda Function → Security Hub API → Security Findings
```

### Components
- **Custom Controls**: Python-based control logic
- **Lambda Functions**: AWS Lambda for control execution
- **CloudFormation**: Infrastructure as Code for deployment
- **IAM**: Least-privilege access control
- **S3**: Storage for control outputs and logs

## 📊 Custom Controls

### Control 1: Custom Compliance Framework Check
- **Objective**: Check compliance against custom organizational framework
- **Framework**: Custom internal requirements
- **Skills**: Security Hub control logic, compliance mapping

### Control 2: AWS Service Specific Controls
- **Objective**: Monitor specific AWS services for security configurations
- **Framework**: Service-specific best practices
- **Skills**: Service configuration analysis, finding generation

### Control 3: AI System Security Controls
- **Objective**: Monitor AI systems for security and compliance
- **Framework**: ISO/IEC 42001 principles
- **Skills**: AI governance, control logic for AI systems

### Control 4: Multi-Aggregate Control
- **Objective**: Aggregate findings from multiple controls
- **Framework**: Executive oversight
- **Skills**: Finding aggregation, consolidation logic

### Control 5: Temporal Compliance Check
- **Objective**: Monitor compliance changes over time
- **Framework**: Continuous compliance monitoring
- **Skills**: Time-based analysis, change detection

## 📁 Project Structure

```
grc-security-hub-custom-controls/
├── custom_controls/ (Control implementations)
├── deployment/ (CloudFormation templates)
├── tests/ (Unit tests)
└── docs/ (Documentation)
```

## 🔧 Technical Stack

- **Language**: Python 3.11+
- **AWS Services**: Security Hub, Lambda, CloudFormation, IAM, S3
- **Libraries**: boto3, jsonschema, pytest
- **Frameworks**: SOC 2, ISO 27001, NIST CSF
- **Output**: Security Hub findings, CloudFormation templates

## 📈 Performance

- **Control Execution**: <5 seconds per control
- **Deployment Time**: <2 minutes via CloudFormation
- **Finding Generation**: Real-time Security Hub integration
- **Test Coverage**: >80%

## 🛡️ Security

- Least-privilege IAM roles
- Security Hub access control
- Encrypted S3 storage (AES256)
- CloudTrail logging enabled
- IAM policy validation

## 🎓 Background

This project leverages experience from the Security Hub Excel Pipeline to demonstrate advanced Security Hub custom control development. It addresses the need for tailored security controls that go beyond standard benchmarks to meet specific organizational compliance requirements.

## 📊 Use Cases

- **Custom Compliance**: Implement organization-specific security controls
- **Service Monitoring**: Monitor specific AWS services for security posture
- **AI Governance**: Extend Security Hub to AI systems and ISO/IEC 42001
- **Executive Oversight**: Aggregate findings for leadership review
- **Continuous Monitoring**: Track compliance changes over time

## 🚀 Deployment

### CloudFormation Deployment

```bash
# Package and deploy
./deployment/deploy-controls.sh
```

### Manual Deployment

```bash
aws cloudformation deploy \
  --template-file deployment/template.yaml \
  --stack-name security-hub-custom-controls \
  --capabilities CAPABILITY_IAM
```

## 📝 Development

### Setup Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test
pytest tests/test_controls.py
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Terence Webster**
- GitHub: [@Tsmooth1987](https://github.com/Tsmooth1987)
- Website: [terence-webster.com](https://terence-webster.com)
- LinkedIn: [Terence Webster](https://linkedin.com/in/terencewebster)

## 🙏 Acknowledgments

- AWS Security Hub documentation and Control Catalog
- AWS Security Hub custom controls best practices
- Security automation community
- AWS Lambda and serverless architecture patterns

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Contact: terence.j.webster@gmail.com
- LinkedIn: [Terence Webster](https://linkedin.com/in/terencewebster)

---

**Built with advanced AWS Security Hub expertise and custom control development capabilities**

*This project demonstrates progression from basic Security Hub automation to advanced custom control development, showcasing comprehensive Security Hub expertise.*