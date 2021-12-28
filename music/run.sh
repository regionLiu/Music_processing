source .env/bin/activate
python main.python
zip -r split_file.zip split_file/
rm -rf split_file/*.wav wav_file/*.wav