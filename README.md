*IN PROGRESS...*


# The Beatles - *Revolver* (1966)
![image](https://user-images.githubusercontent.com/52461409/223927735-bff9ebe0-c3bd-4009-91f5-a67a85c2e058.png)

*Revolver* is the seventh studio album by the English rock band the Beatles.

You can listen to it on (link):

[<img src="https://user-images.githubusercontent.com/52461409/223929644-e0013f84-8415-4223-a112-9533ccd1f64f.png" width="100">](https://open.spotify.com/album/3PRoXYsngSwjEQWR5PsHWR?si=z78W-dP1TICA_Ht0zolLAg)

[<img src="https://user-images.githubusercontent.com/52461409/223930420-e573c86c-ea70-4e13-a736-674d6fbd59c7.png" width="100">](https://music.apple.com/us/album/revolver/1441164670)

# Data
- Spotify Features
  - Extracted with [*spotipy*](https://github.com/spotipy-dev/spotipy) package
- Audio Wave
  - 14 songs in .wav files
  - Not uploaded in this repo due to a copyright issue
- Annotations Data ([*source*](http://isophonics.net/content/reference-annotations-beatles))
  - Structures in csv
  - Keys in csv
- Other Metadata ([*source*](https://www.kaggle.com/datasets/bvinning/uk-studio-albums-by-the-beatles))
  - Lyrics
  - Lead vocals, writers


## What I did with this album:
- Source Separation
  - Separate music into four sources: vocal, bass, drum, and other
  - Use pre-trained [*Hybrid Transformer Demucs*](https://github.com/facebookresearch/demucs) model (using deep neural networks)
  
- Audio Feature Extraction
  - Extract audio features such as mean, variance, minimum, and maximum values of spectrogram features, mfccs, zcr, rmse, chromagram features, and tempo features
  - Use [*ftrosa*](https://github.com/jo-cho/ftrosa) package which is based on [*librosa*](https://github.com/librosa/librosa)

- Melody Extraction and Transcription: extracting a main melody of each song
  - Get F0(fundamental frequency) of main vocal melody
  - Piano transcription of the melodies. (*in progress*)
  
- Lyrics Parts
  - Create lyric wordcloud with sentiment analysis
  - Use [*wordcloud*](https://github.com/amueller/word_cloud) and [*nltk*](https://github.com/nltk/nltk)
--- 

***TO-DOs***
- Harmony Parts
  - Singer Identification: identifying a lead vocal (John, Paul, George, or Ringo) of each song
    - Use unsupervised learning to distinguish the vocals. Is it possible with spectral features?
    - Or you can train a ML/DL model on the other Beatles vocal data and test to identify the vocals.
  - Chord recognition: detecting chords, keys of each song
- Rhythm Parts
  - Drum Pattern Anaylsis
  - Beat tracking
    - Get BPM, detect onset
    - Drum Transcription
- Structural Parts
  - Structure Analysis and Segmentation

- ... and I'll come up with more ideas.
