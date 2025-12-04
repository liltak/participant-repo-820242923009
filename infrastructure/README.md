# CDK Infrastructure

This directory contains the AWS CDK infrastructure code for the project.

## Prerequisites

- Python 3.8 or later
- AWS CLI configured with appropriate credentials
- Node.js (for AWS CDK CLI)

## Setup

### Option 1: Using uv (Recommended - Faster)

1. Create a virtual environment:
```bash
uv venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Install AWS CDK CLI (if not already installed):
```bash
npm install -g aws-cdk
```

5. Bootstrap CDK (first time only):
```bash
cdk bootstrap
```

### Option 2: Using pip

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install AWS CDK CLI (if not already installed):
```bash
npm install -g aws-cdk
```

4. Bootstrap CDK (first time only):
```bash
cdk bootstrap
```

## Verification

To verify the CDK stack can be synthesized without errors:

```bash
# Using the CDK CLI (requires CDK CLI version 2.1033.0 or later)
cdk synth

# Or directly run the app
python app.py
```

If synthesis succeeds, you'll see CloudFormation template output or the command will complete without errors.

## Usage

### Synthesize CloudFormation template
```bash
cdk synth
```

### Deploy the stack
```bash
cdk deploy
```

### View differences between deployed stack and current code
```bash
cdk diff
```

### Destroy the stack
```bash
cdk destroy
```

## Project Structure

- `app.py` - CDK app entry point
- `infrastructure/` - CDK stack definitions
  - `infrastructure_stack.py` - Main infrastructure stack
- `cdk.json` - CDK configuration
- `requirements.txt` - Python dependencies

## Adding Resources

To add AWS resources to your infrastructure, edit `infrastructure/infrastructure_stack.py` and add CDK constructs within the `InfrastructureStack` class.

Example:
```python
from aws_cdk import aws_s3 as s3

# Inside InfrastructureStack.__init__
bucket = s3.Bucket(self, "MyBucket",
    versioned=True,
    removal_policy=cdk.RemovalPolicy.DESTROY
)
```

## Useful Commands

- `cdk ls` - List all stacks in the app
- `cdk synth` - Synthesize CloudFormation template
- `cdk deploy` - Deploy stack to AWS
- `cdk diff` - Compare deployed stack with current state
- `cdk docs` - Open CDK documentation

## Environment Configuration

By default, the stack uses the AWS account and region from your AWS CLI configuration. To specify a different account/region, uncomment and modify the `env` parameter in `app.py`.
