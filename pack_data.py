# -*- encoding: utf-8 -*-
# Author: Spencer Whitehead

import os
import glob
import json
import argparse


DATA_FIELDS = ['id', 'upload_date', 'duration', 'fulltitle',
               'title', 'tags', 'uploader_url',
               'categories', 'webpage_url_basename', 'display_id',
               'description']

YT_URL = 'https://www.youtube.com/watch?v=%s'


def get_relevant_metadata(meta_json, id_field=DATA_FIELDS[-3], tag_field=DATA_FIELDS[5], url_field='url'):
    relevant_data = {}
    with open(meta_json, 'r') as f:
        all_data = json.load(f)
        for field_name in DATA_FIELDS:
            if field_name != tag_field:
                relevant_data[field_name] = all_data[field_name]
            else:
                relevant_data[field_name] = [tag for tag in all_data[field_name] if tag.lower() != "web"]
    relevant_data[url_field] = YT_URL % relevant_data[id_field]
    return relevant_data


def filter_metadata(metadata_dir, out_dir):
    full_out_dir = os.path.expanduser(out_dir)
    if not os.path.exists(full_out_dir):
        os.makedirs(full_out_dir)

    for vid_metafname in glob.glob(os.path.join(metadata_dir, '*.info.json')):
        curr_meta = get_relevant_metadata(vid_metafname)
        outfname = os.path.join(full_out_dir, os.path.basename(vid_metafname))
        with open(outfname, 'w') as outf:
            json.dump(curr_meta, outf)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("input_dir", help="Directory containing meta-data files.")
    p.add_argument("output_dir", help="Directory to write filtered meta-data files.")
    args = p.parse_args()

    retrieve_metadata(args.input_dir, args.output_dir)
