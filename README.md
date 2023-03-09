*IN PROGRESS...*


# The Beatles - *Revolver* (1966)
![image](https://user-images.githubusercontent.com/52461409/223927735-bff9ebe0-c3bd-4009-91f5-a67a85c2e058.png)

*Revolver* is the seventh studio album by the English rock band the Beatles.

Streaming on:

[<img src="https://user-images.githubusercontent.com/52461409/223929644-e0013f84-8415-4223-a112-9533ccd1f64f.png" width="100">](https://open.spotify.com/album/3PRoXYsngSwjEQWR5PsHWR?si=z78W-dP1TICA_Ht0zolLAg)

[<img src="https://user-images.githubusercontent.com/52461409/223930420-e573c86c-ea70-4e13-a736-674d6fbd59c7.png" width="100">](https://music.apple.com/us/album/revolver/1441164670)

# Data
- Spotify Features
  - Extracted with [*spotipy*](https://github.com/spotipy-dev/spotipy) package
- Audio Features
  - Extracted with [*ftrosa*](https://github.com/jo-cho/ftrosa) package, [*librosa*](https://github.com/librosa/librosa) package
- Audio Features by Different Instrument(vocal,bass,drum,other)
  - Source-separated by [*Hybrid Transformer Demucs*](https://github.com/facebookresearch/demucs) model
  - Extracted with [*ftrosa*](https://github.com/jo-cho/ftrosa) package, [*librosa*](https://github.com/librosa/librosa) package
- Annotations Data ([*source*](http://isophonics.net/content/reference-annotations-beatles))
  - Structure in csv
  - Key in csv
- Other Metadata ([*source*](https://www.kaggle.com/datasets/bvinning/uk-studio-albums-by-the-beatles))
  - Lyrics
  - Lead vocals, writers



## What I did with this album:

***TO-DOs***
- Harmony Parts
  - Singer Identification: identifying a lead vocal (John, Paul, George, or Ringo) of each song
    - Use unsupervised learning to distinguish the vocals. Is it possible with spectral features?
    - Or you can train a ML/DL model on the whole Beatles vocal data and test to identify the vocals.
  - Melody Extraction: extracting a main melody of each song
    - Get F0(frequency) pitch contour
    - Transcribe the vocal melodies to notes.
  - Key Detection: detecting chords, keys of each song
    - Chord recognition
- Rhythm Parts
  - Drum Pattern Anaylsis
  - Beat tracking
    - Get BPM, detect onset, transcribe to drum midi.
- Structural Parts
- Lyrics Parts
  - Lyric map
- ... and I'll come up with more ideas.
