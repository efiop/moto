import boto
from sure import expect

from moto import mock_ec2


@mock_ec2
def test_network_acls():
    pass