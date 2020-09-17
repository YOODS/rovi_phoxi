# rovi_phoxi
RoVI wrapper for PhoXi

## Topics
### To publish
<table>
<tr><th>Name<th>Type<th>Description
<tr><td>ps_floats_all<td>Numpy<td>3DデータNumpy形式。全ピクセルの三次元座標をアドレス順に出力します。
<tr><td>ps_floats<td>Numpy<td>3DデータNumpy形式。三次元座標が求められた点のみ出力します。
<tr><td>ps_pc<td>PointCloud<td>3DデータPointCloud形式。三次元座標が求められた点のみ出力します。
<tr><td>left/image_raw<td>Image<td>左カメラraw画像
<tr><td>left/image_rect<td>Image<td>左カメラrectify画像
<tr><td>/error<td>String<td>
<tr><td>stat<td>Bool<td>接続状態
<tr><td>Y1<td>Bool<td>撮像結果(X1に対するレスポンス)
</table>

### To subscribe
<table>
<tr><th>Name<th>Type<th>Description
<tr><td>X1<td>Bool<td>撮像トリガ
</table>
