# AWS Inventory Enterprise Scan

## Overview

AWS Inventory Enterprise Scan is a Python-based automation tool that scans AWS infrastructure using Boto3 and generates inventory reports for cloud administrators.

## Features

- EC2 Inventory
- VPC Inventory
- IAM Inventory
- S3 Inventory
- Route53
- Lambda
- CloudWatch
- RDS
- ELB
- EKS
- ECS
- EBS
- Security Groups
- Elastic IP
- Subnets
- 
## Tech Stack

- Python
- Boto3
- AWS CLI
- Pandas
- OpenPyXL

## Architecture

Python Script
      │
      ▼
 Boto3 SDK
      │
      ▼
AWS Account
      │
      ├── EC2
      ├── IAM
      ├── S3
      ├── VPC
      ├── Lambda
      ├── Route53
      ├── CloudWatch
      ├── RDS
      ├── ...
      │
      ▼
 Export
CSV | Excel | JSON

## Installation

### Clone Repository

git clone https://github.com/yourusername/aws_inventory_enterprise_scan.git

### Install Requirements

pip install -r requirements.txt

## Install
```bash
pip install -r requirements.txt
```

## Run using AWS profile
```bash
python main.py --profile default
```

## Run using access key / secret key
```bash
python main.py --access-key YOUR_KEY --secret-key YOUR_SECRET
```
## Output

CSV

Excel

JSON

Recommended permissions: `ReadOnlyAccess` + `SecurityAudit`.
Use only on AWS accounts you own or are authorized to audit.
