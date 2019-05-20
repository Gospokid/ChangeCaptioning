from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import math
import sys
import pickle
import numpy as np
import json
import os

train_data = json.load( open("../Datasets/2sim/train.json","r") )
val_data = json.load( open("../Datasets/2sim/val.json","r") )
test_data = json.load( open("../Datasets/2sim/test.json","r") )

print('train_data_length :', len(train_data))
print('val_data_length :', len(val_data))
print('test_data_length :', len(test_data))

sys.path.append("coco-caption")
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap

#single
cache_fname_prefix = 'predictions/ddla_rerun'
#pred_file = os.path.join('predictions/ddla_rerun_predfile.json')
pred_file = os.path.join('predictions/volquelme_pred_att2in2_diff.json')
gt_file = os.path.join(cache_fname_prefix + '_gtfile.json')

coco = COCO(gt_file)
cocoRes = coco.loadRes(pred_file)
cocoEval = COCOEvalCap(coco, cocoRes)
cocoEval.params['image_id'] = cocoRes.getImgIds()
cocoEval.evaluate()