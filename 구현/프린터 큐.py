class myQueue:
    def __init__(self, get_list):     # 큐 생성 초기값 한번에 대입
        self.container = get_list

    def enqueue(self, data):  # 큐 push (마지막에)
        self.container.append(data)

    def dequeue(self):  # 큐 pop
        return self.container.pop(0)  # 가장 앞에있는 요소 추출


testcase = int(input())  # 테스트 케이스 개수
for i in range(testcase):
    info = list(map(int, input().split()))
    n = info[0]   # 문서 개수
    m = info[1]   # 확인하고 싶은 문서의 현재 큐의 위치
    queue_info = list(map(int, input().split()))   # 현재 큐 상태
    find_num = queue_info[m]      # 찾을 중요도 값 저장
    set_queue = [(val, idx) for idx, val in enumerate(queue_info)]   # 값, 인덱스가 모두 저장된 리스트
    queue = myQueue(set_queue)     # 나의 큐 생성
    queue_info.sort(reverse=True)  # 중요도 크기순 정렬
    count = 0     # 나올 순서
    j = 0
    #print(f'{i}번째 시작')
    while True:
        out_set = queue.dequeue()

        if out_set[0] == queue_info[j]:  # 가장 큰 값이 나오면 출력
            #print(f'출력 숫자: {out_set[0]}')
            count += 1
            j += 1
            if out_set[0] == find_num:  # 출력한게 찾는 문서면 중단
                if out_set[1] == m:
                    break
                    
        else:  # 가장 중요한 문서가 아님 -> 큐의 맨 뒤로 다시 push
            #print('다음것 출력')
            queue.enqueue(out_set)

    print(count)
