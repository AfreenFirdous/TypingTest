import random

class Typing_Handler:
    _VALID_CONTENT = str()
    _SENTENCE_STARTER = ['About 100 years ago', 'In the 20 BC', 'Once upon a time']
    _CHARACTER = [' there lived a king.',' there was a man named Jack.',
                ' there lived a farmer.']
    _TIME = [' One day', ' One full-moon night']
    _STORY_PLOT = [' he was passing by',' he was going for a picnic to ']
    _PLACE = [' the mountains', ' the garden']
    _SECOND_CHARACTER = [' he saw a man', ' he saw a young lady']
    _AGE = [' who seemed to be in late 20s', ' who seemed very old and feeble']
    _WORK = [' searching something.', ' digging a well on roadside.']

    @classmethod
    def _sentence_generator(cls):
        for i in range(2):
            data = random.choice(cls._SENTENCE_STARTER) + random.choice(cls._CHARACTER) + \
                random.choice(cls._TIME) + random.choice(cls._STORY_PLOT) + \
                random.choice(cls._PLACE) + random.choice(cls._SECOND_CHARACTER)+ \
                random.choice(cls._AGE) + random.choice(cls._WORK) + ' '
            cls._VALID_CONTENT += data
        return cls._VALID_CONTENT

    @classmethod
    def display_home(cls):
        cls._VALID_CONTENT = str()
        content = cls._sentence_generator()
        return content

    @classmethod
    def _get_correct_incorrect_count(cls, input_list, valid_list):
        total_entries = 0
        total_errors = 0
        accurate_entries = 0
        for i in range(len(input_list)):
            if input_list[i] == valid_list[i]:
                accurate_entries += len(input_list[i])
                total_entries += len(input_list[i])
            else:
                for j in range(len(valid_list[i])):
                    input_char = input_list[i][j]
                    valid_char = valid_list[i][j]
                    if input_char == valid_char:
                        accurate_entries += 1
                        total_entries += 1
                    else:
                        total_errors += 1
                        total_entries +=1
        return total_entries, accurate_entries, total_errors

    @classmethod
    def get_typing_result(cls, input_content):
        accuracy = 0
        valid_list = cls._VALID_CONTENT.split()
        input_list = input_content.split()
        total_entries, accurate_entries, total_errors = cls._get_correct_incorrect_count(input_list, valid_list)
        wpm = int((total_entries / 5) - total_errors)
        if total_entries > 0 and accurate_entries > 0:
            accuracy = int((accurate_entries/total_entries) * 100)
        return total_entries, accurate_entries, total_errors,  accuracy, wpm
