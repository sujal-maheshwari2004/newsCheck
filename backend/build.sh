#!/usr/bin/env bash
set -o errexit

echo "Updating system packages..."
apt-get update

echo "Installing FFmpeg (required for yt-dlp audio processing)..."
apt-get install -y ffmpeg

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"
