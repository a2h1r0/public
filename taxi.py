import numpy as np


#*** 変数 ***#
# 初乗運賃[m]
first_distance = 1700
first_price = 680

# 加算運賃[m]
add_distance = 241
add_price = 80
add_price_par_meter = add_price/add_distance

# 経由地
# ベクトル座標は全て[km]
goal = np.array([0, 0])
a = np.array([5, 1])
b = np.array([3, 2])
c = np.array([4, 4])
d = np.array([0.5, 3])

# [m]変換
a *= 2000
b *= 2000
c *= 2000
d *= 2000



#*** 個別で向かう場合 ***#
# 距離計算(初乗り距離を除く)
a_to_goal = np.linalg.norm(a-goal) - first_distance
if a_to_goal < 0:
    a_to_goal = 0
b_to_goal = np.linalg.norm(b-goal) - first_distance
if b_to_goal < 0:
    b_to_goal = 0
c_to_goal = np.linalg.norm(c-goal) - first_distance
if c_to_goal < 0:
    c_to_goal = 0
d_to_goal = np.linalg.norm(d-goal) - first_distance
if d_to_goal < 0:
    d_to_goal = 0

# 金額
a_price = first_price + (a_to_goal*add_price_par_meter)
b_price = first_price + (b_to_goal*add_price_par_meter)
c_price = first_price + (c_to_goal*add_price_par_meter)
d_price = first_price + (d_to_goal*add_price_par_meter)

#*** 周回する場合 ***#
# 距離計算(初乗り距離を除く)
a_to_c = np.linalg.norm(a-c)
c_to_b = np.linalg.norm(c-b)
b_to_d = np.linalg.norm(b-d)
d_to_goal = np.linalg.norm(d-goal)
route = a_to_c + c_to_b + b_to_d + d_to_goal - first_distance

# 金額
route_price = first_price + (route*add_price_par_meter)


'''
print('\n初乗り運賃：', end='')
print(first_price, end='')
print('円')
print('初乗り距離：', end='')
print(first_distance/1000, end='')
print('km\n')
print('加算運賃：', end='')
print(add_price, end='')
print('円')
print('加算距離：', end='')
print(add_distance, end='')
print('m')
print('-------------\n')

print('個別で向かう場合\n')
print('A運賃：', end='')
print(a_price, end='')
print('円')
print('A距離：', end='')
print((a_to_goal+first_distance)/1000, end='')
print('km\n')
print('B運賃：', end='')
print(b_price, end='')
print('円')
print('B距離：', end='')
print((b_to_goal+first_distance)/1000, end='')
print('km\n')
print('C運賃：', end='')
print(c_price, end='')
print('円')
print('C距離：', end='')
print((c_to_goal+first_distance)/1000, end='')
print('km\n')
print('D運賃：', end='')
print(d_price, end='')
print('円')
print('D距離：', end='')
print((d_to_goal+first_distance)/1000, end='')
print('km')
print('-------------\n')

print('A-C距離：', end='')
print(a_to_c/1000, end='')
print('km')
print('C-B距離：', end='')
print(c_to_b/1000, end='')
print('km')
print('B-D距離：', end='')
print(b_to_d/1000, end='')
print('km')
print('D-Goal距離：', end='')
print(d_to_goal/1000, end='')
print('km')
print('-------------\n')

print('周回する場合\n')
print('運賃：', end='')
print(route_price, end='')
print('円')
print('総距離：', end='')
print((route+first_distance)/1000, end='')
print('km\n')
print('1人あたりの運賃：', end='')
print(route_price/4, end='')
print('円')
print('-------------\n')



#*** 周回する場合2 ***#
# 距離計算(初乗り距離を除く)
a_to_b = np.linalg.norm(a-b)
b_to_goal = np.linalg.norm(b-goal)
c_to_d = np.linalg.norm(c-d)
d_to_goal = np.linalg.norm(d-goal)
route1 = a_to_b + b_to_goal - first_distance
route2 = c_to_d + d_to_goal - first_distance

# 金額
route1_price = first_price + (route1*add_price_par_meter)
route2_price = first_price + (route2*add_price_par_meter)


print('A-B距離：', end='')
print(a_to_b/1000, end='')
print('km')
print('B-Goal距離：', end='')
print(b_to_goal/1000, end='')
print('km')
print('C-D距離：', end='')
print(c_to_d/1000, end='')
print('km')
print('D-Goal距離：', end='')
print(d_to_goal/1000, end='')
print('km')
print('-------------\n')

print('ルート1距離：', end='')
print((route1+first_distance)/1000, end='')
print('km')
print('ルート1運賃：', end='')
print(route1_price/2, end='')
print('円')
print('ルート2距離：', end='')
print((route2+first_distance)/1000, end='')
print('km')
print('ルート2運賃：', end='')
print(route2_price/2, end='')
print('円')
'''


first_distance *= 4
first_price *= 4

#*** 個別で向かう場合 ***#
# 距離計算(初乗り距離を除く)
a_to_goal = np.linalg.norm(a-goal) - first_distance
if a_to_goal < 0:
    a_to_goal = 0
b_to_goal = np.linalg.norm(b-goal) - first_distance
if b_to_goal < 0:
    b_to_goal = 0
c_to_goal = np.linalg.norm(c-goal) - first_distance
if c_to_goal < 0:
    c_to_goal = 0
d_to_goal = np.linalg.norm(d-goal) - first_distance
if d_to_goal < 0:
    d_to_goal = 0

# 金額
a_price = first_price/4 + (a_to_goal*add_price_par_meter)
b_price = first_price/4 + (b_to_goal*add_price_par_meter)
c_price = first_price/4 + (c_to_goal*add_price_par_meter)
d_price = first_price/4 + (d_to_goal*add_price_par_meter)

#*** 周回する場合 ***#
# 距離計算(初乗り距離を除く)
a_to_c = np.linalg.norm(a-c)
c_to_b = np.linalg.norm(c-b)
b_to_d = np.linalg.norm(b-d)
d_to_goal = np.linalg.norm(d-goal)
route = a_to_c + c_to_b + b_to_d + d_to_goal - first_distance

# 金額
route_price = first_price + (route*add_price_par_meter)


print('\n初乗り運賃：', end='')
print(first_price, end='')
print('円')
print('初乗り距離：', end='')
print(first_distance/1000, end='')
print('km\n')
print('加算運賃：', end='')
print(add_price, end='')
print('円')
print('加算距離：', end='')
print(add_distance, end='')
print('m')
print('-------------\n')

print('個別で向かう場合\n')
print('A運賃：', end='')
print(a_price, end='')
print('円')
print('A距離：', end='')
print((a_to_goal+first_distance)/1000, end='')
print('km\n')
print('B運賃：', end='')
print(b_price, end='')
print('円')
print('B距離：', end='')
print((b_to_goal+first_distance)/1000, end='')
print('km\n')
print('C運賃：', end='')
print(c_price, end='')
print('円')
print('C距離：', end='')
print((c_to_goal+first_distance)/1000, end='')
print('km\n')
print('D運賃：', end='')
print(d_price, end='')
print('円')
print('D距離：', end='')
print((d_to_goal+first_distance/4)/1000, end='')
print('km')
print('-------------\n')

print('A-C距離：', end='')
print(a_to_c/1000, end='')
print('km')
print('C-B距離：', end='')
print(c_to_b/1000, end='')
print('km')
print('B-D距離：', end='')
print(b_to_d/1000, end='')
print('km')
print('D-Goal距離：', end='')
print(d_to_goal/1000, end='')
print('km')
print('-------------\n')

print('周回する場合\n')
print('運賃：', end='')
print(route_price, end='')
print('円')
print('総距離：', end='')
print((route+first_distance)/1000, end='')
print('km\n')
print('1人あたりの運賃：', end='')
print(route_price/4, end='')
print('円')
print('-------------\n')
