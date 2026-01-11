# データ可視化 (Data Visualization)

このディレクトリには、データからグラフを生成し、可視化するためのツールを格納します。

## ツール一覧

### 1. 基本グラフ生成ツール (`basic_plotter.py`)

CSVファイルを読み込み、基本的なグラフ（棒グラフ、散布図、ヒストグラム）を生成して画像ファイルとして保存します。

#### 使い方

```bash
python3 basic_plotter.py [入力CSV] [出力画像] --type [種類] --x [X軸] [オプション]
```

#### コマンド例

- **棒グラフ (Bar Plot)**
  ```bash
  # 'city'ごとの'age'の平均値を棒グラフで表示
  python3 basic_plotter.py data.csv bar_chart.png --type bar --x city --y age
  ```

- **散布図 (Scatter Plot)**
  ```bash
  # 'age'と'salary'の関係を散布図で表示
  python3 basic_plotter.py data.csv scatter_plot.png --type scatter --x age --y salary
  ```

- **ヒストグラム (Histogram)**
  ```bash
  # 'age'の分布をヒストグラムで表示
  python3 basic_plotter.py data.csv hist.png --type histogram --x age
  ```

- **色分けを追加する場合 (Hue)**
  ```bash
  # 上記の散布図を'gender'カラムで色分け
  python3 basic_plotter.py data.csv scatter_hue.png --type scatter --x age --y salary --hue gender
  ```

#### 引数

- `input`: (必須) 変換元のCSVファイルパス。
- `output`: (必須) 保存先の画像ファイルパス (例: `my_plot.png`)。
- `--type`: (必須) グラフの種類。`bar`, `scatter`, `histogram` から選択。
- `--x`: (必須) X軸として使用するカラム名。
- `--y`: (任意) Y軸として使用するカラム名。`bar`と`scatter`では必須です。
- `--hue`: (任意) グラフを色分けする際に使用するカラム名。

---
今後、箱ひげ図、ヒートマップなど、対応するグラフの種類を増やしていく予定です。