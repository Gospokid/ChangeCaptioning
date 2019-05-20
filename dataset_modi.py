from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json

ref_file_nodiff = open('Image_ID_with_no_differences.txt', 'rt')
id_nodiff = ref_file_nodiff.read()
list_nodiif = id_nodiff.split(',')
print('print 1st list_nodiff for check : ', list_nodiif[0])
print('list_nodiff length :', len(list_nodiif),'\tset length :',len(set(list_nodiif)))
ref_file_nocap = open('Image_ID_with_no_caption.txt', 'rt')
id_nocap = ref_file_nocap.read()
list_nocap = id_nocap.split(',')
print('print 1st list_nocap for check : ', list_nocap[0])
print('list_nocap length :', len(list_nocap),'\tset length :',len(set(list_nocap)))
out = {}
out['images'] = []
no_caption = []
no_difference = []

with open('data/combined.json', 'r') as f:
    j_file = json.load(f)
    print('print 1st image_id for check', j_file['images'][0]['id'])

    for i, temp_images in enumerate(j_file['images']):
        if temp_images['id'] in list_nodiif:
            print('image_id with no differences :', temp_images['id'])
        elif temp_images['id'] in list_nocap:
            print('image_id with no captions :', temp_images['id'])
        else:
            j_info = {}
            j_info['filepath'] = temp_images['filepath']
            j_info['filename'] = temp_images['filename']
            j_info['sentences'] = temp_images['sentences']
            j_info['id'] = temp_images['id']
            j_info['split'] = temp_images['split']
            out['images'].append(j_info)

json.dump(out, open('data/dataset_modi_combined.json', 'w'))

#f_no_caption = open('Image_id_with_no_caption.txt', 'wt')
#f_no_caption.write(str(no_caption))
#f_no_caption.close()
#print('number_of_image_ID_with_no_caption', len(no_caption))

#f_no_difference = open('Image_ID_with_no_differnces.txt', 'wt')
#f_no_difference.write(str(no_difference))
#f_no_difference.close()
#print('number_of_image_ID_with_no_difference', len(no_difference))
