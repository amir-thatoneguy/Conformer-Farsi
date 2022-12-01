import sys
import os
import pandas as pd
import subprocess
import json
import codecs
import unidecode


def normalize_str(txt) -> str:
    # TODO: REPLACE WITH YOUR OWN NORMALIZATION LOGIC HERE!!!!   
    valid_chars = (" ","ي", "ی","ه","و","ن", "م","ل", "گ", "ک", "ق", "ف", "غ", "ع", "ظ", "ط", "ض", "ص", "ش", "س", "ز", "ر", "ذ", "د", "خ", "ح", "چ", "ج", "ث", "ت", "پ", "ب","ک","ء", "ژ","ئ","آ","ا")
    new_txt = txt.strip()
    res_arr = []
    for c in new_txt:
        if c in valid_chars:
            res_arr.append(c)
        else:
            res_arr.append(' ')
    res = ''.join(res_arr).strip()    
    return ' '.join(res.split())

def tsv_to_manifest(tsv_files, manifest_file, prefix):
  manifests = []
  for tsv_file in tsv_files:
    print('Processing: {0}'.format(tsv_file))
    dt = pd.read_csv(tsv_file, sep='\t', encoding='utf8')
    for index, row in dt.iterrows():
      try:
        entry = {}
        os.system("mkdir -p wavs/{0}".format(prefix))
        mp3_file = "/content/CommonVoice_dataset/CV_unpacked/cv-corpus-5.1-2020-06-22/fa/clips/" + row['path'] # + ".mp3"
        wav_file = "/content/drive/MyDrive/wavs/{0}/".format(prefix) + row['path'].replace("mp3", "wav") #".wav"
        subprocess.check_output("sox {0} -c 1 -r 16000 {1}".format(mp3_file, wav_file), shell=True)
        duration = subprocess.check_output(
          "soxi -D {0}".format(wav_file), shell=True)
        entry['audio_filepath'] = wav_file
        entry['duration'] = float(duration)
        entry['text'] = normalize_str(row['sentence'])
        manifests.append(entry)
      except:
        print("SOMETHING WENT WRONG - IGNORING ENTRY")

  with codecs.open(manifest_file, 'w', encoding='utf-8') as fout:
    for m in manifests:
      fout.write(json.dumps(m, ensure_ascii=False) + '\n')
  print('Done!')


def main():
  prefix = sys.argv[1]
  tsv_to_manifest([prefix + ".tsv"], prefix+".json", prefix)
  

if __name__ == "__main__":
    main()