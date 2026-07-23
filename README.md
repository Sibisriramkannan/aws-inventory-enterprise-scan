# 🚀 AWS Inventory Enterprise Scan

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazonaws)
![Boto3](https://img.shields.io/badge/Boto3-SDK-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Enterprise-grade AWS Inventory Scanner built with Python and Boto3 to collect AWS infrastructure details across multiple services and generate inventory reports in **CSV, JSON, and Excel** formats.

---

# 📖 Overview

Managing AWS resources across multiple regions and accounts can become challenging as infrastructure grows. This project automates AWS resource discovery and generates comprehensive inventory reports that can be used for:

- Infrastructure Audits
- Cloud Asset Management
- Security Reviews
- Cost Optimization
- Documentation
- Backup Planning
- Compliance Reporting

---

# ✨ Features

- ✅ EC2 Instances
- ✅ AMIs
- ✅ Elastic IPs
- ✅ VPCs
- ✅ Subnets
- ✅ Route Tables
- ✅ Internet Gateways
- ✅ NAT Gateways
- ✅ Security Groups
- ✅ Network ACLs
- ✅ IAM Users
- ✅ IAM Groups
- ✅ IAM Roles
- ✅ IAM Policies
- ✅ S3 Buckets
- ✅ EBS Volumes
- ✅ EBS Snapshots
- ✅ RDS Databases
- ✅ Lambda Functions
- ✅ CloudWatch Alarms
- ✅ Auto Scaling Groups
- ✅ Launch Templates
- ✅ Load Balancers (ALB/NLB)
- ✅ Target Groups
- ✅ Route 53 Hosted Zones
- ✅ ECS Clusters
- ✅ EKS Clusters
- ✅ CloudFormation Stacks
- ✅ Systems Manager Managed Instances
- ✅ Elastic File System (EFS)

---

# 🛠 Tech Stack

- Python
- Boto3
- AWS CLI
- Pandas
- OpenPyXL
- JSON
- CSV

---

# 📂 Project Structure

```text
aws-inventory-enterprise-scan/

├── config/
├── inventory/
├── output/
│   ├── csv/
│   ├── excel/
│   └── json/
├── screenshots/
├── docs/
├── utils/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

# 🏗 Architecture

```
                 Python Inventory Scanner
                         │
                         ▼
                      Boto3 SDK
                         │
                         ▼
                    AWS Account
                         │
 ┌────────────┬────────────┬───────────────┐
 ▼            ▼            ▼               ▼
 EC2         IAM          S3             Networking
 ▼            ▼            ▼               ▼
 Lambda      RDS      CloudWatch     Auto Scaling
 ▼            ▼            ▼               ▼
           Inventory Collection Engine
                         │
                         ▼
          CSV | JSON | Excel Reports
```

---

# ⚙️ Prerequisites

- AWS Account
- Python 3.10+
- AWS CLI
- Boto3
- IAM User with Read-Only permissions

---

# 🔑 Authentication

Configure AWS CLI:

```bash
aws configure
```

Verify credentials:

```bash
aws sts get-caller-identity
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/aws-inventory-enterprise-scan.git
```

Navigate to the project:

```bash
cd aws-inventory-enterprise-scan
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the scanner:

```bash
python main.py --access-key YOUR-KEY --secret-key YOUR-KEY
```

---

# 📊 Output

The tool generates reports in:

```
output/

├── csv/
├── json/
└── excel/
```

Example reports:

- EC2_Instances.csv
- IAM_Users.xlsx
- S3_Buckets.json
- VPC_Report.csv
- RDS_Instances.xlsx

---

# 📸 Screenshots

```
screenshots/

01_AWS_Login.png

02_Run_Script.png

03_Output.png

04_Excel_Report.png

05_JSON_Report.png
```

---

# 🎯 Use Cases

- AWS Infrastructure Inventory
- Cloud Documentation
- Asset Discovery
- Security Audits
- Compliance Reporting
- Disaster Recovery Planning
- Migration Planning
- Cost Optimization

---

# 🚀 Future Enhancements

- Multi-Account Support
- Multi-Region Scanning
- AWS Organizations Integration
- HTML Dashboard
- Email Reports
- Resource Tag Compliance Report
- Cost Explorer Integration
- Security Best Practices Report
- AWS Config Integration

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, submit issues, or create pull requests.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sibisriram Kannan**

Cloud Engineer (SRE)

- ☁ AWS
- 🔷 Azure
- ☁ GCP
- 🐧 Linux
- 🪟 Windows Server
- ⚙ DevOps
- 🤖 Automation

---

⭐ If you found this project useful, please consider giving it a star!
