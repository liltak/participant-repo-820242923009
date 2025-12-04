#!/usr/bin/env python3
import aws_cdk as cdk

from infrastructure.infrastructure_stack import InfrastructureStack


app = cdk.App()

InfrastructureStack(
    app,
    "InfrastructureStack",
    # Uncomment to specify AWS account and region
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
)

app.synth()
