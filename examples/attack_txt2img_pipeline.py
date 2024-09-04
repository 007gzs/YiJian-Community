# -*- coding: utf-8 -*-
# Copyright 2024 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is specially provided for Global AI Offensive and Defensive Challenge Track 1：Vaccination for Text-to-Image Generative Models (https://tianchi.aliyun.com/competition/entrance/532268/information?lang=en-us)

import torch
import numpy as np
import pandas as pd
from diffusers import KolorsPipeline, FluxPipeline

from yijian_community.data import load_data, save_data
from yijian_community.model import HFTxt2ImgInfer
from yijian_community.defense import ThuCoaiShieldLM, InternVL2ImageDefense
