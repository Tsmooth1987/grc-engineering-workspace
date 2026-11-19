#!/bin/bash
set -e

echo "=========================================="
echo "Packaging Multi-Account Aggregator"
echo "=========================================="

rm -rf build
mkdir -p build

echo "Installing dependencies..."
pip3 install -r requirements.txt -t build/ --upgrade

echo "Copying Lambda function..."
cp lambda_function.py build/

echo "Creating deployment package..."
cd build
zip -r ../lambda-source.zip . -q
cd ..

SIZE=$(ls -lh lambda-source.zip | awk '{print $5}')
echo ""
echo "=========================================="
echo "✅ Package created successfully!"
echo "=========================================="
echo "File: lambda-source.zip"
echo "Size: $SIZE"
echo ""
