import pandas as pd
from nlputils import *

df = pd.read_csv('./data/smartphone.csv', encoding='utf-8')
galexy_posts = df.get('Title') + " " + df.get('Description')
print(galexy_posts)

galexy_stop_words = "은 이 것 등 더 를 좀 즉 인 옹 때 만 원 이때 개 일 기 시 럭 갤 성 삼 스 폰 트 드 기 이 리 폴 사 전 마 자 플 블 가 중 북 수 팩 년 월 저 탭"
galexy_stop_words = galexy_stop_words.split(' ')
galexy_stop_words[0:10]

print('불용어 제거 결과 >>')
clean_list = get_koean_clean_word(galexy_posts, galexy_stop_words)
print(clean_list)

print('자주사용하는 단어 리스트 10가지 >>')
top_10_list = get_most_common_words(clean_list, 10)
print(top_10_list)
