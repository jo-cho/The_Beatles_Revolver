import pandas as pd
import os
from ftrosa import get_all_musical_features

wav_path = "data/wav/"
separated_path = "data/separated/htdemucs/" # separated sources using HTDemucs

if __name__ == '__main__':
    track_list = []
    for song in os.listdir(wav_path):
        track_list.append(song.split('.')[0])

    print('Tracklist: ', track_list)

    df_list = []
    count = 0

    for i in track_list:
        path_audio = wav_path + i + '.wav'
        song_name = i.split('_', maxsplit=1)[1]
        df_ = get_all_musical_features(
            path_audio,
            song_name,
            start=30,
            duration=30,
            stats=['mean', 'std', 'max', 'min'],
            chroma_method_list=['cqt'])
        df_list.append(df_)
        count += 1
        print(count, 'songs extracted')
    audio_features = pd.concat(df_list, axis=1).T.reset_index(names=['song'])

    # for separated stems (bass, drums, vocals, other)

    instruments = ['bass', 'drums', 'vocals', 'other']

    df_list = []
    count = 0

    for i in track_list:
        df_list_inst = []
        for j in instruments:
            path_audio = separated_path + i + '/' + j + '.wav'
            song_name = i.split('_', maxsplit=1)[1]
            df_ = get_all_musical_features(
                path_audio,
                song_name=j,
                start=30,
                duration=30,
                stats=['mean', 'std', 'max', 'min'],
                chroma_method_list=['cqt'])
            df_list_inst.append(df_.T.reset_index(names=['instrument']))
            df_track = pd.concat(df_list_inst, axis=0)
            df_track.insert(loc=0, column='song', value=song_name)
            print(' ', j, ' extracted')
        df_list.append(df_track)
        count += 1
        print(count, 'song extracted')
    audio_separated_features = pd.concat(df_list, axis=0).reset_index(drop=True)

    # save as csv files
    audio_features.to_csv('data/audio_features.csv')
    audio_separated_features.to_csv('data/audio_separated_features.csv')