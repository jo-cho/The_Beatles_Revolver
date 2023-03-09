# The Beatles - *Revolver* (1966)
![image](https://user-images.githubusercontent.com/52461409/223927735-bff9ebe0-c3bd-4009-91f5-a67a85c2e058.png)

*Revolver* is the seventh studio album by the English rock band the Beatles.

Streaming on:

[<img src="https://user-images.githubusercontent.com/52461409/223929644-e0013f84-8415-4223-a112-9533ccd1f64f.png" width="100">](https://open.spotify.com/album/3PRoXYsngSwjEQWR5PsHWR?si=z78W-dP1TICA_Ht0zolLAg)

[<img src="https://user-images.githubusercontent.com/52461409/223930420-e573c86c-ea70-4e13-a736-674d6fbd59c7.png" width="100">](https://music.apple.com/us/album/revolver/1441164670)

## Data: What we have here
- Spotify Features
  - Extracted with *spotipy*
  - 
- Audio Features
  - Extracted with *ftrosa*, *librosa*
- Audio Features by Instrument(vocal,bass,drum,other)
  - Source-separated by *HD Demucs* model
  - Extracted with *ftrosa*, *librosa*
- Annotations Data
  - Structure
  - Key
- Other Metadata
  - Lyrics
  - Lead Vocals
  - Producer



## What can we do with the data?

***TO-DOs***
- See what features can identify a lead vocal (john, paul, george, or ringo) of each song - SINGER IDENTIFICATION
  - Use unsupervised learning to distinguish the vocals. Is it possible with spectral features?
  - Of course you can train a ML/DL model on the whole Beatles vocal data and test to identify the vocals. But it's too common thing.
- Analyze drums patterns
- Draw a lyric map
- Melody extraction and key detection on vocals
- ... and I'll come up with more ideas.
