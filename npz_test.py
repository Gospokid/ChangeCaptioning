from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np

att_feat_1 = np.load('/home/volquelme/img_cap/data/combined_out_att/0.npz')['feat']
print('att_feat_1 shape : ', att_feat_1.shape) # (14, 14, 2048)
att_feat_2 = np.load('/home/volquelme/img_cap/data/combined_out_att/0_2.npz')['feat']
att_feat_diff = np.load('/home/volquelme/img_cap/data/combined_out_att/0_diff.npz')['feat']

att_feat_re = att_feat_1.reshape(-1, att_feat_1.shape[-1])
print('att_feat_re shape', att_feat_re.shape)

att_feat = np.concatenate((att_feat_1, att_feat_2, att_feat_diff), axis = 1)
print('att_feat shape : ', att_feat.shape)

fc_feat_1 = np.load('/home/volquelme/img_cap/data/combined_out_fc/0.npy')
print('fc_feat_1 shape : ', fc_feat_1.shape) # (2048, )
fc_feat_2 = np.load('/home/volquelme/img_cap/data/combined_out_fc/0_2.npy')
fc_feat_diff = np.load('/home/volquelme/img_cap/data/combined_out_fc/0_diff.npy')

fc_feat = (fc_feat_1 + fc_feat_2 + fc_feat_diff) / 3
print('fc_feat shape : ', fc_feat.shape)

