source .env/bin/activate
sh env.sh
python main.py
zip -r split_file.zip split_file/
rm -rf split_file/*.wav wav_file/*.wav