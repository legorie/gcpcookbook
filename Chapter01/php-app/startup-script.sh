#!/bin/bash
# Modified from https://github.com/GoogleCloudPlatform/getting-started-php/blob/master/optional-compute-engine/gce/startup-script.sh

# [START all]
set -e
export HOME=/root

# [START php]
yum update
yum install -y httpd php php-mysql php-pdo
systemctl start httpd.service
systemctl enable httpd.service


# Fetch the project ID from the Metadata server
PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")

# Get the application source code
git config --global credential.helper gcloud.sh
git clone https://source.developers.google.com/p/gcp-cookbook/r/gcpcookbook  /opt/src -b master
#ln -s /opt/src/optional-compute-engine /opt/app
cp /opt/src/Chapter01/php-app/pdo/* /var/www/html -r
# [END php]

# [START project_config]
# Fetch the application config file from the Metadata server and add it to the project
#curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/project-config" \
#  -H "Metadata-Flavor: Google" >> /opt/app/config/settings.yml
# [END project_config]
# [START logging]
# Install Fluentd
curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash

# Start Fluentd
systemctl start google-fluentd.service
# [END logging]
# [END all]
