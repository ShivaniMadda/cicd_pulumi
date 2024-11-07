import pulumi
import pulumi_aws as aws

 

# # Create a new EC2 key pair
# key_pair = aws.ec2.KeyPair("my-key-pair",
#     key_name="mykey12",
#     public_key="your-public-key-here"  # Replace with your actual public key
# )

 

# Create a new security group
security_group = aws.ec2.SecurityGroup("my-security-group",
    description="Allow SSH access",
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=22,
            to_port=22,
            cidr_blocks=["0.0.0.0/0"],
        )
    ],
)

 

# Define the EC2 instance
ec2_instance = aws.ec2.Instance("demo-instance1",
    instance_type="t2.micro",
    ami="ami-0866a3c8686eaeeba",  # Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
    key_name='mykey',
    vpc_security_group_ids=[security_group.id],
    tags={
        "Name": "my-ubuntu-instance"
    }
)

 

# Export the instance's public IP
pulumi.export("instance_public_ip", ec2_instance.public_ip)
