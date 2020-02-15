# [예제 2.12] 전처리 함수 사용 예제 

# [예제 2.13] matplotlib 불러오고 한글폰트 설정 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
%matplotlib inline

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 맥OS 인 경우 위 두 줄을 입력하지 말고 아래 코드를 입력하세요
# rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


# [예제 2.14] 종합 매매가격 지수 그래프 그리기 
path = r'f:\data\kb\★(월간)KB주택가격동향_시계열(2019.12).xlsx'
data_type = '매매종합'
new_data = KBpriceindex_preprocessing(path, data_type)
new_data['전국']['전국'].plot(legend='전국')
plt.show()


# [예제 2.16] subplot을 이용해 서울과 대구 그래프 그리기

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('서울')
plt.plot(new_data['서울']['서울']['2008-01':])

plt.subplot(1, 2, 2)
plt.title('대구')
plt.plot(new_data['대구']['대구']['2008-01':])

plt.show()


# [예제 2.22] 누락된 지역 삭제 및 상위, 하위 10개만 출력 

diff = ((new_data.loc['2018-1-1'] - new_data.loc['2016-1-1']) / new_data.loc['2016-1-1'] * 100).dropna()
print("하위 10개")
print(diff.sort_values()[:10])
print(' ')
print("상위 10개")
print(diff.sort_values(ascending=False)[:10])


# [예제 2.23] 가격지수 증감률을 막대그래프로 시각화

import numpy as np
from matplotlib import style
style.use('ggplot')

fig = plt.figure(figsize=(13, 7))
ind = np.arange(20)

ax = fig.add_subplot(1, 3, 1)
plt.title('2016.1~2018.1 가격 변화율 최하위 20')
rects = plt.barh(ind, diff.sort_values()[:20].values,  align='center', height=0.5)
plt.yticks(ind, diff.sort_values()[:20].index)
for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(),
            rect.get_y() + rect.get_height() / 2.0,
            str(round(diff.sort_values()[:20].values[i],2)) + '%',
            ha='left', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))
    
ax2 = fig.add_subplot(1, 3, 3)
plt.title('2016.1~2018.1 가격 변화율 최상위 20')
rects2 = plt.barh(ind, diff.sort_values()[-20:].values,  align='center', height=0.5)
plt.yticks(ind,  diff.sort_values()[-20:].index)
for i, rect in enumerate(rects2):
    ax2.text(0.95 * rect.get_width(),
             rect.get_y() + rect.get_height() / 2.0,
             str(round(diff.sort_values()[-20:].values[i],2)) + '%', 
             ha='right', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))

plt.show()


# [예제 2.24] 특정 지역만 선택해서 가격지수 증감률을 막대그래프로 시각화

loca =  '전국 서울 부산 경기 대구 광주 울산 대전'

temp_list = loca.split(" ")
loca_list = []
for temp in temp_list:
    if ',' in temp:
        temp_split = temp.split(",")
        loca_list.append((temp_split[0], temp_split[1]))
    else:
        loca_list.append((temp, temp))

diff = ((new_data.loc['2018-1-1', loca_list] - new_data.loc['2016-1-1', loca_list]) / new_data.loc['2016-1-1', loca_list] * 100).sort_values()

num = len(loca_list)
fig = plt.figure(figsize=(13, 7))
ind = np.arange(num)

ax = fig.add_subplot(1, 3, 1)
plt.title('2016.1~2018.1 가격지수 변화율')
rects = plt.barh(ind, diff.head(num).values,  align='center', height=0.5)
plt.yticks(ind, diff.head(num).index)
for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0, str(round(diff.head(20).values[i], 2)) + '%',
            ha='left', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))


plt.show()