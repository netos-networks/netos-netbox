#!/bin/bash

# Variables passed from Ansible or set manually
REPO_URL=$1
TOKEN=$2
PLUGIN_ADD=$3

# Split PLUGIN_ADD into two variables:
PLUGIN_URL=${PLUGIN_ADD//_/-}  # Replace underscores with dashes for the URL
PLUGIN_FILE=${PLUGIN_ADD//-/_}  # Replace dashes with underscores for file names and array keys

# Fetch the list of .tar.gz URLs from the PyPI repository using PLUGIN_URL
RESPONSE=$(curl -s "https://__token__:${TOKEN}@${REPO_URL}/${PLUGIN_URL}")

# Fetch URLs from the response
URLS=$(echo "$RESPONSE" | grep -oP '(?<=href=")[^"]+\.tar\.gz')

# Check if any URLs were found
if [ -z "$URLS" ]; then
  echo "FAILED"
  exit 1
fi

# Extract the version numbers and URLs
declare -A versioned_urls
for url in $URLS; do
  # Extract version from the URL (assuming PLUGIN_URL-X.Y.Z.tar.gz format)
  version=$(echo "$url" | grep -oP "${PLUGIN_URL//-/_}-\K[\d\.]+(?=\.tar\.gz)")

  # Store the URL in the array using the sanitized version as the key
  if [ ! -z "$version" ]; then
    versioned_urls["$version"]=$url
  fi
done

# Check if any valid versions were found
if [ ${#versioned_urls[@]} -eq 0 ]; then
  echo "No valid version numbers found."
  exit 1
fi

# Sort versions using the sanitized keys
sorted_versions=$(echo "${!versioned_urls[@]}" | tr ' ' '\n' | sort -t. -k1,1n -k2,2n -k3,3n)

# Get the latest version
latest_version=$(echo "$sorted_versions" | tail -n 1)
latest_url=${versioned_urls[$latest_version]//uk-git01.core.netos.io/git01.netos.io}

# Download the latest version using PLUGIN_FILE for the file name
mkdir -p /netos/working-dir/netos-plugins
file_name="${PLUGIN_FILE}-${latest_version}.tar.gz"
file_path="/netos/working-dir/netos-plugins/$file_name"
wget --header="PRIVATE-TOKEN: ${TOKEN}" -q -O "$file_path" "$latest_url"

# Output only the file name if successful, or "FAILED" if not
if [ $? -eq 0 ]; then
  echo "$file_name"
else
  echo "FAILED"
  exit 1
fi
