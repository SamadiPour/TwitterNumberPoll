import json
import re

from config import keywords, votes

if __name__ == '__main__':
    
    file = open('replies.jsonl')
    next(file)

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
