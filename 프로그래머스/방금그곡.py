def solution(m, musicinfos):
    answer = ''

    # (#제거 코드)
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    len_m = m

    information = []  # 곡정보 재저장
    i = 1  # 곡이 입력된 순서
    for info in musicinfos:
        s, e, name, m_sheet = info.split(",")
        s_h, s_m = s.split(":")  # 시작 시간, 분
        e_h, e_m = e.split(":")  # 끝 시간, 분
        if s_h == e_h:
            play_time = int(e_m) - int(s_m)
        else:
            hour_cha = int(e_h) - int(s_h)  # 시간 차이
            play_time = (int(e_m) + 60 * hour_cha) - int(s_m)
        print(play_time)
        m_sheet = m_sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        m_len = len(m_sheet)  # 음악 길이
        information.append([play_time, i, name, m_sheet, m_len])
        i += 1

    information.sort(key=lambda x: (-x[0], x[1]))  # 플레이 시간 큰 순으로 정렬(플레이 시간이 같으면 입력 순)
    print(information)

    # 음악 확인
    for info in information:
        repeat = info[0] // info[4]  # 음악 반복 횟수
        rest = info[0] % info[4]  # 남은 멜로디
        rythm = info[3] * repeat + info[3][:rest]  # 전체 멜로디
        print(rythm)

        # 정렬이 되어 있으므로 해당 음악을 찾으면 빠져나옴
        if m in rythm:
            answer = info[2]
            break

    if answer == '':
        answer = '(None)'

    return answer