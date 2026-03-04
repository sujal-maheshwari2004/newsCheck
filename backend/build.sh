#!/usr/bin/env bash
set -o errexit

echo "Downloading FFmpeg static build..."

curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o ffmpeg.tar.xz

tar -xf ffmpeg.tar.xz

FFMPEG_DIR=$(find . -type d -name "ffmpeg-*-amd64-static")

echo "Setting up FFmpeg..."

mkdir -p ffmpeg-bin
cp $FFMPEG_DIR/ffmpeg ffmpeg-bin/
cp $FFMPEG_DIR/ffprobe ffmpeg-bin/

chmod +x ffmpeg-bin/ffmpeg
chmod +x ffmpeg-bin/ffprobe

export PATH="$PWD/ffmpeg-bin:$PATH"

echo "FFmpeg installed locally."

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build completed."
