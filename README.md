# AWS Enterprise Inventory Collector

Scans all enabled AWS regions and exports inventory/audit data to `aws_inventory.xlsx`.

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

Recommended permissions: `ReadOnlyAccess` + `SecurityAudit`.
Use only on AWS accounts you own or are authorized to audit.
