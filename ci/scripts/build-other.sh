#!/bin/bash

# Exits as soon as any line fails.
set -euo pipefail

source ci/scripts/common.env.sh

# Should set a stable version of connector node
STABLE_VERSION=9d2e1331680335661fd3e55ee234532358683201

echo "--- Build Java connector node"
git clone https://"$GITHUB_TOKEN"@github.com/risingwavelabs/risingwave-connector-node.git
cd risingwave-connector-node
# checkout a stable version
git checkout $STABLE_VERSION
mvn package -Dmaven.test.skip=true
echo "--- Upload Java artifacts"
cp service/target/service-*.jar ./connector-service.jar
buildkite-agent artifact upload ./connector-service.jar
