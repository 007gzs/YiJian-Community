import os
from datasets import load_dataset

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

txt2txt_set = load_dataset("csv", data_files=os.path.join(CURRENT_DIR, "txt2txt/txt2txt.csv"))
txt2img_set = load_dataset("csv", data_files=os.path.join(CURRENT_DIR, "txt2img/txt2img.csv"))
img_txt2txt_set = load_dataset("csv", data_files=os.path.join(CURRENT_DIR, "img_txt2txt/img_txt2txt.csv"))
