from janome.tokenizer import Tokenizer
t = Tokenizer()

# for token in t.tokenize('"多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾"'):
#   print(token)
# print()
# from janome.tokenizer import Tokenizer
# t = Tokenizer()
# for token in t.tokenize('今日も１日がんばるぞい'):
#   print(token.surface)
# print()
# from janome.tokenizer import Tokenizer
# t = Tokenizer()
# for token in t.tokenize('今日も１日がんばるぞい', wakati=True):
#   print(token)
# print()
# from janome.tokenizer import Tokenizer
# t = Tokenizer()
# for token in t.tokenize('今日も１日がんばった'):
#   print(token.base_form)
# print()

# import jieba
#
# seg_list = jieba.cut("多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾",cut_all=True)
# print("Full Mode:", "/ ".join(seg_list)) #全模式
#
# seg_list = jieba.cut("多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾",cut_all=False)
# print("Default Mode:", "/ ".join(seg_list)) #精确模式
#
# seg_list = jieba.cut("多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾") #默认是精确模式
# print( ", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾") #搜索引擎模式
# print(", ".join(seg_list))

from janome.analyzer import Analyzer
from janome.tokenfilter import *
text = u'多分タピオカ8万粒は食べてきた笑#タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分#夜市#台北101#龍山寺#中正紀念堂#謝#謝謝台湾 場所: 台北，台湾'
token_filters = [POSKeepFilter(['名詞']), TokenCountFilter()]
b = Analyzer(token_filters=token_filters)
# for k, v in a.analyze(text):
#  print('%s: %d' % (k, v))
# StopWordFilter の実装
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *


# class StopWordFilter(TokenFilter):
#   def __init__(self, word_list=[], word_list_file=''):
#     """
#     ここに初期化コードを記述
#     """

  # def apply(self, tokens):
  #   """
  #   ここにフィルター処理を記述
  #   """
# token_filters = [StopWordFilter(word_list=['プログラミング'])]
# a = Analyzer(tokenizer=Tokenizer(), token_filters=token_filters)
# for token in a.analyze('Pythonは人気の高いプログラミング言語です。'):
#   print(token)


# class CompoundNounFilter(TokenFilter):
#
#   def apply(self, tokens):
#     _ret = None
#     for token in tokens:
#       if _ret:
#         if token.part_of_speech.startswith(u'名詞') and _ret.part_of_speech.startswith(u'名詞'):
#           _ret.surface += token.surface
#           _ret.part_of_speech = u'名詞,複合,*,*'
#           _ret.base_form += token.base_form
#           _ret.reading += token.reading
#           _ret.phonetic += token.phonetic
#         else:
#           ret = _ret
#           _ret = token
#           yield ret
#       else:
#         _ret = token
#     if _ret:
#       yield _ret
# CompoundNounFilter(TokenFilter).apply()
# token_filters = [CompoundNounFilter()]
# text ="多分タピオカ8万粒は食べてきた笑タピオカってなんなん#台湾#台湾旅行#台湾グルメ#九份#十分夜市#台北101#龍山寺#中正紀念堂#謝謝台湾 場所: 台北，台湾"
# a = Analyzer(token_filters=token_filters)
tokens = b.analyze(text)

word_list = []

for token in tokens:
  word = token.surface
  word_list.append(word)

words_wakati = " ".join(word_list)
print(word_list)