한줄로 줄이기 연습
1.for문 한 개 있을 때
list1 = [1,2,3,4,5]
list2 = []

for i in list1 :
    list2.append(i*2)

print(list2)

==> list2 = [i*2 for i in list1]

list1 = [1,2,3]

2.이중 for문 한줄로 작성하기
# 1번 for
for i in list1 :
    # 2번 for
    for j in list1 :
        print(i*j,end=" ") # 1 2 3 2 4 6 3 6 9
이중 for문을 한 줄로 작성할 때는 바깥쪽의 for 문을 맨 마지막에 작성하고,
내포된 for문을 앞부분에 작성해야 한다.

==>  [i*j for j in list1 for i in list1]

3. if else 가 함께 쓰일 경우, if 문을 for문 보다 앞에 적는다

[i*j if i> 1 else 0 for j in list1 for i in list1]

4. 만약 else 가 없다면, if 문은 맨 마지막 위치에 적는다

[i*j for j in list1 for i in list1 if i>1]


[i if i == 12 else "No" for i in v]
 ==> 12빼고 다 No로 출
