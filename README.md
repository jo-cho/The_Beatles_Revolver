# The Beatles - *Revolver* (1966)

*Revolver* is the seventh studio album by the English rock band the Beatles.

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
