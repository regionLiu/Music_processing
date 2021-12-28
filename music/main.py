import os
import argparse


class Ffmpeg_tools:
    # ffmpeg -i ./file/4451511f2521cea6a78e8d0c7a5b9c03.mp4 -f wav -ar 16000 a.wav
    # ffmpeg -i ./wav_file/a.wav -b:a 64k -acodec mp3 -ar 44100 -ac 1 ./split_file/a.mp3
    # ffmpeg -i ./wav_file/a.wav -vn -acodec copy -ss 00:00:00 -t 00:01:30 1.wav
    # ffmpeg -i ./wav_file/BoobssoundMoanOrgasm…teenwav_file.wav -vn -acodec copy -ss 00:00:22 -to 00:00:33 -c copy ./split_file/BoobssoundMoanOrgasm…teensplit_file2.wav
    cmd_map = {
        "mv_to_audio": "ffmpeg -i {0} -f wav -ar 16000 {1}",
        "split_audio": "ffmpeg -i {0} -vn -acodec copy -ss {1} -to {2} -c copy {3}",
        "zip_to_mp3": "ffmpeg -i {0} -b:a 64k -acodec mp3 -ar 44100 -ac 1 {1}",
        "splite_voice":"separate -i audio_example.mp3 -p spleeter:2stems -o output"
    }
    
    
    def __init__(self, name, suffix, cmd_type, times = []):
        self._name = name
        self._suffix = suffix
        self._file_path = "./file/{}".format(".".join([name,suffix]))
        self._wav_path = "./wav_file/{}".format(".".join([name+"wav_file",'wav']))
        self._cmd_type = cmd_type
        self._split_path = './split_file/{}'
        self._zip_file = "./zip_file/{}".format(".".join([name+"zip_file",'mp3']))
        self._times = times
        
        
    def run(self):
        try:
            params = self.construction_params()
            cmds = self.construction_cmd(params=params)
            for _ in cmds:
                if self.excute_cmd(_):
                    print("成功")
                else:
                    print("失败")
                    break
        except Exception as e:
            print(e)
            
    def construction_cmd(self, params):
        cmd_strs = []
        try:
            for _ in params:
                cmd_strs.append(self.cmd_map.get(self._cmd_type).format(*_))
            return cmd_strs
        except Exception as e:
            print(e)
            return []
    
    def construction_params(self):
        params = []
        try:
            if self._cmd_type == 'mv_to_audio':
                params.append([self._file_path, self._wav_path])
            if self._cmd_type == 'split_audio':
                for _ in range(len(self._times)):
                    split_path = self._split_path.format('.'.join([self._name+"split_file"+str(_), 'wav']))
                    params.append([self._wav_path, self._times[_][0], self._times[_][1], split_path])
            
            if self._cmd_type == 'zip_to_mp3':
                params.append([self._file_path, self._zip_file])
            
            return params
        except Exception as e:
            print(e)
            return params
    
    def excute_cmd(self, cmd):
        try:
            print(cmd)
            a = os.system(cmd)
            print(a)
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="mv_to_audio")
    # parser.add_argument('--old_file_path', help="原文件路径")
    # parser.add_argument('--new_file_path', help="新文件路径")
    
    
    
    # args = parser.parse_args()
    # print(args)
    split_times = {
        # "4451511f2521cea6a78e8d0c7a5b9c03" : [['00:00:03','00:00:32'],['00:00:34','00:01:37'],['00:01:43','00:02:45'],['00:03:01','00:03:57'],['00:04:01','00:04:51'],['00:04:53','00:05:17']],
        "PILLOWHUMPINGASMRthebestpleasuresounds": [['00:00:15','00:00:24'],['00:00:38','00:00:48'],['00:00:51','00:01:02'],['00:01:44','00:00:50'],['00:01:10','00:01:16'],['00:01:31','00:01:33'],['00:02:05','00:02:15'],['00:02:18','00:02:33'],['00:02:46','00:02:55'],['00:03:02','00:03:12'],['00:03:14','00:03:26'],['00:03:35','00:03:45'],['00:03:46','00:04:06']]

        # "345":[['00:00:01','00:00:07']]
    }
    for i,j,k in os.walk('./file'):
        for _ in k:
            
            file_names = _.split('.')
            name = file_names[0]
            suffix = file_names[1]
            Ffmpeg_tools(name, suffix, 'mv_to_audio').run()
            Ffmpeg_tools(name, suffix, 'split_audio', split_times[name]).run()