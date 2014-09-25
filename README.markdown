# はじめに
これはtmuxpowerlineのステータス上に現在の天気と温度を表示するためのものです．
weather.pyの中にあるlocationという変数をあなたの住んでいる地域に書き換えることで，その地域の現在の天気と温度が表示されます．

# 環境

- python3
- ライブラリ
    - requests

# 設定
これらのファイルを次のようなディレクトリに置いてください．

- weather.pyとweatherpy.shを/path/to/tmux-powerline/segments以下に置いてください．

- /path/to/tmux-powerline/themes以下にある各自テーマにある"TMUX_POWERLINE_RIGHT_STATUS_SEGMENTS"に"weatherpy"という名前を追加してください．

