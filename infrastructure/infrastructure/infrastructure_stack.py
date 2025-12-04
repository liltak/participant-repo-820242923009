from aws_cdk import Stack
from constructs import Construct


class InfrastructureStack(Stack):
    """
    Main CDK stack for the application infrastructure.
    
    This stack is currently empty and ready for AWS resource definitions.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO: Add AWS resources here
