#!/bin/bash
# deploy.sh - Deploy Elektripaigaldiste Juhend to Synology NAS

NAS_USER="DmitriG"
NAS_IP="192.168.10.105"
NAS_PATH="/volume1/web/juhend"

echo "Building MkDocs site..."
source .venv/bin/activate
mkdocs build

echo "Deploying to NAS..."
SSH_CMD="ssh -i /Users/dmitrigridin/.ssh/melior_nas -o IdentitiesOnly=yes"
$SSH_CMD ${NAS_USER}@${NAS_IP} "rm -rf ${NAS_PATH}/*"
tar --no-xattrs --no-mac-metadata -cf - -C site . | $SSH_CMD ${NAS_USER}@${NAS_IP} "tar -xf - -C ${NAS_PATH}" 2>/dev/null
echo "Failid kopeeritud!"

echo ""
echo "Done! Open: http://${NAS_IP}/juhend/"
