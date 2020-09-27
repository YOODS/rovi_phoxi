# rovi_phoxi
RoVI wrappers for PhoXi

## fdriver.py  
PhoXiControlの出力ファイルをroviに再発行します。ファイルは**.ros/phoxi**以下にあるとみなします。

### To launch
~~~
roslaunch rovi_phoxi fdriver.launch
~~~

### Topics to publish
<table>
<tr><th>Name<th>Type<th>Description
<tr><td>ps_floats_all<td>Numpy<td>3DデータNumpy形式。全ピクセルの三次元座標をピクセル順に出力します。
<tr><td>ps_floats<td>Numpy<td>3DデータNumpy形式。三次元座標が求められた点のみ出力します。
<tr><td>image_raw<td>Image<td>最新のraw画像を１秒毎に更新します
<tr><td>image_raw1<td>Image<td>点群取得時にそのraw画像を出力します
<tr><td>Y1<td>Bool<td>X1処理完了
</table>

### Topics to subscribe
<table>
<tr><th>Name<th>Type<th>Description
<tr><td>X1<td>Bool<td>PLYファイルをps_floatに出力します
</table>

## ユーティリティ
### dump_caminfo  
PhoXiカメラパラメータ(K,D)をyaml形式で出力します。以下手順にてphoxiのカメラパラメータファイルを用意します。
~~~
?????
~~~
### ロボットキャリブレーション
~~~
roslaunch rovi_phoxi rcalib_wpc.launch
~~~
