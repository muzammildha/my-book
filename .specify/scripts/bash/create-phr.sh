#!/bin/bash

# Simple placeholder for create-phr.sh
# This script will eventually create a PHR markdown file
# For now, it just echoes the arguments and returns a mock JSON output.

TITLE=""
STAGE=""
FEATURE="none"
JSON_OUTPUT="false"

while (( "$#" )); do
  case "$1" in
    --title)
      TITLE="$2"
      shift 2
      ;;
    --stage)
      STAGE="$2"
      shift 2
      ;;
    --feature)
      FEATURE="$2"
      shift 2
      ;;
    --json)
      JSON_OUTPUT="true"
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [ -z "$TITLE" ] || [ -z "$STAGE" ]; then
  echo "Usage: $0 --title <title> --stage <stage> [--feature <name>] [--json]"
  exit 1
fi

# Generate a mock ID and path
MOCK_ID=$(date +%s)
MOCK_SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-zA-Z0-9]+/-/g' | cut -c 1-20)
MOCK_PATH="history/prompts/${STAGE}/${MOCK_ID}-${MOCK_SLUG}.${STAGE}.prompt.md"

if [ "$JSON_OUTPUT" = "true" ]; then
  echo "{\"phr_id\": \"${MOCK_ID}\", \"phr_path\": \"${MOCK_PATH}\"}"
else
  echo "Mock create-phr.sh called with:"
  echo "  Title: ${TITLE}"
  echo "  Stage: ${STAGE}"
  echo "  Feature: ${FEATURE}"
  echo "  Generated ID: ${MOCK_ID}"
  echo "  Generated Path: ${MOCK_PATH}"
fi
