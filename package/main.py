"""Main entrypoint function for destroy all aws resources"""

import logging
import os
import timeparse
import ec2
import autoscaling
import loadbalancing
import ebs

aws_resources = os.getenv('AWS_RESOURCES', 'tostop')
older_than = os.getenv('OLDER_THAN', 'none')

# Setup simple logging for INFO
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    """ Main function entrypoint for lambda """

    # Convert older_than variable to seconds
    older_than_seconds = timeparse.timeparse(older_than)

    if aws_resources == "*" or "ec2" in aws_resources:
        ec2.nuke_all_ec2(older_than_seconds)

    if aws_resources == "*" or "autoscaling" in aws_resources:
        autoscaling.nuke_all_autoscaling(older_than_seconds)

    if aws_resources == "*" or "loadbalancing" in aws_resources:
        loadbalancing.nuke_all_loadbalancing(older_than_seconds)

    if aws_resources == "*" or "ebs" in aws_resources:
        ebs.nuke_all_ebs(older_than_seconds)
