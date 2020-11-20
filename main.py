import json
import re

if __name__ == '__main__':
    file = open('replies.jsonl')
    next(file)

    keywords = {
        # 'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        # 'nine': 9,
        # 'صفر': 0,
        'یک': 1,
        'دو': 2,
        'سه': 3,
        'چهار': 4,
        'پنج': 5,
        'شش': 6,
        'هفت': 7,
        'هشت': 8,
        # 'نه': 9,
        # 'صفرم': 0,
        'اول': 1,
        'دوم': 2,
        'سوم': 3,
        'چهارم': 4,
        'پنجم': 5,
        'ششم': 6,
        'هفتم': 7,
        'هشتم': 8,
        # 'نهم': 9,
        # '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        # '9': 9,
        # '۰': 0,
        '۱': 1,
        '۲': 2,
        '۳': 3,
        '۴': 4,
        '۵': 5,
        '۶': 6,
        '۷': 7,
        '۸': 8,
        # '۹': 9,
    }

    votes = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

    for row in file:
        line = json.loads(row)
        text: str = line['full_text']

        # ---- pre-process ----
        # remove usernames
        text = re.sub(r'(^|[^@\w])@(\w{1,15})\b', '', text).strip()

        # remove links
        text = re.sub(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b'
                      r'([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', '', text).strip()

        # todo: need good pre-process on text (I don't know how)

        # ---- search for keywords ----
        person_votes = set()
        words_re = re.compile("|".join(keywords.keys()), re.IGNORECASE)
        if words_re.search(text):
            for found in words_re.findall(text):
                person_votes.add(keywords[found])

        # ---- count votes ----
        for person_vote in person_votes:
            votes[person_vote] += 1

    # ---- print votes ----
    for i, vote in enumerate(votes):
        print("option {}: {}".format(i, vote))
