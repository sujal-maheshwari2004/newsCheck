#!/usr/bin/env bash
set -o errexit

echo "Installing FFmpeg static build..."

curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o ffmpeg.tar.xz

tar -xf ffmpeg.tar.xz

FFMPEG_DIR=$(find . -type d -name "ffmpeg-*-amd64-static")

cp $FFMPEG_DIR/ffmpeg /usr/local/bin/
cp $FFMPEG_DIR/ffprobe /usr/local/bin/

echo "FFmpeg installed."

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build completed."
