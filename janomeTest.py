# from janome.tokenizer import Tokenizer
# # # 簡単な使用方法
# # t = Tokenizer()
# # for token in t.tokenize('21時から、おしえて！白上教官アークナイツ特別授業たまに資材のステージやったりしていたんだけど、もっとアークナイツを楽しむために！！！！！白上教官に来ていただきます個人レッスンだ'):
# #     print(token)
import sys
import MeCab
m = MeCab.Tagger ("-Ochasen")
print (m.parse ("多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾"))