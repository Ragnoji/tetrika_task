def appearance(intervals: dict[str, list[int]]) -> int:
    res = 0
    p = []
    t = []
    for i in range(0, len(intervals['pupil']) - 1, 2):
        l, r = intervals['pupil'][i], intervals['pupil'][i + 1]
        if p and l <= p[-1]:
            p[-1] = max(r, p[-1])
        else:
            p.append(l)
            p.append(r)

    for i in range(0, len(intervals['tutor']) - 1, 2):
        l, r = intervals['tutor'][i], intervals['tutor'][i + 1]
        if t and l <= t[-1]:
            t[-1] = max(r, t[-1])
        else:
            t.append(l)
            t.append(r)
    p_i = 0
    t_i = 0
    if not p or not t or not intervals['lesson']:
        return 0
    p_left, p_right = p[p_i], p[p_i + 1]
    t_left, t_right = t[t_i], t[t_i + 1]
    lesson_left, lesson_right = intervals['lesson'][0], intervals['lesson'][1]
    while True:
        if t_left >= lesson_right or p_left >= lesson_right:
            break
        if t_left < lesson_left:
            t_left = lesson_left
        if p_left < lesson_left:
            p_left = lesson_left
        if t_right > lesson_right:
            t_right = lesson_right
        if p_right > lesson_right:
            p_right = lesson_right
        if t_left >= t_right:
            t_i += 2
            if t_i >= len(t) - 1:
                break
            t_left, t_right = max(t[t_i], t_left), max(t[t_i + 1], t_right)
            continue
        if p_left >= p_right:
            p_i += 2
            if p_i >= len(p) - 1:
                break
            p_left, p_right = max(p[p_i], p_left), max(p[p_i + 1], p_right)
            continue
        if t_left >= p_right:
            p_i += 2
            if p_i >= len(p) - 1:
                break
            p_left, p_right = max(p[p_i], p_left), p[p_i + 1]
            continue
        if p_left >= t_right:
            t_i += 2
            if t_i >= len(t) - 1:
                break
            t_left, t_right = max(t[t_i], t_left), t[t_i + 1]
            continue

        res += min(t_right, p_right) - max(t_left, p_left)
        t_left, p_left = min(t_right, p_right) + 1, min(t_right, p_right) + 1
    return res



tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'intervals': {'lesson': [0, 0],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 0
    },
    {'intervals': {'lesson': [1594692033, 1594692034],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 1
    },
    {'intervals': {'lesson': [1594692033, 1594692034],
             'pupil': [1594692033, 159469633],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 0
    },
    {'intervals': {'lesson': [],
             'pupil': [],
             'tutor': []},
    'answer': 0
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
