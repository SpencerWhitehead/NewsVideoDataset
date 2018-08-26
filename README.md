# NewsVideoDataset
This repository includes the resources and instructions for retrieving the news video dataset from [Whitehead et al., 2018](http://nlp.cs.rpi.edu/paper/videocaption.pdf).

# Dataset statistics
| | Videos | Duration (seconds) | Tags | Sentences | Unique words (vocab) |
| ------------- |  :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| Total | 2,883 | 151,474 | 13,431 | 3,302 | 8,512 |
| Average (per video) |  | 52.5 | 4.7 | 1.2 | 3.0 |

# Retrieving the videos
First, install the youtube_dl program from here: https://github.com/rg3/youtube-dl. Next, run the following command:

```
youtube-dl -o "OUTPUT_FILE_PATH/vid.%(id)s.%(ext)s" --batch-file urls.txt --restrict-filenames --write-info-json --recode-video mp4 --sleep-interval 20 --max-sleep-interval 50
```
This will retrieve the videos and meta-data from YouTube. If you would like to refine the meta-data files and eliminate potentially irrelevant information like the video playback quality options, then run:
```
python pack_data.py
```

# Citation
```
@inproceedings{whiteheadKaVD2018,
    Author = {Whitehead, Spencer and Ji, Heng and Bansal, Mohit and Chang, Shih-Fu and Voss, Clare R.},
    title={Incorporating Background Knowledge into Video Description Generation},
    booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    year={2018},
    month={October},
    publisher={Association for Computational Linguistics},
    location={Brussels, Belgium}
}
```

# Disclaimer
This dataset is for educational and research purposes only. The videos found at the URLs are protected under their respective YouTube licenses and the terms therein. The videos were uploaded to YouTube and created by the AFP news agency (https://www.youtube.com/user/AFP, https://www.afp.com/en). We claim no ownership of these videos or their contents. They belong to their original copyright owners.
