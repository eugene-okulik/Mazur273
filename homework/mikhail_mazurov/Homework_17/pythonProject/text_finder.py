import argparse
import os


def is_timestamp(line):
    return (
        len(line) >= 19 and
        line[4] == '-' and
        line[7] == '-' and
        line[10] == ' ' and
        line[13] == ':' and
        line[16] == ':'
    )


def parse_log(filepath):
    with open(filepath, encoding='utf-8', errors='ignore') as file:
        current_time = None
        buffer = []

        for line in file:
            line = line.strip()

            if is_timestamp(line):
                if current_time:
                    yield current_time, ' '.join(buffer)

                current_time = line[:19]
                buffer = [line[20:]]
            else:
                if current_time:
                    buffer.append(line)

        if current_time:
            yield current_time, ' '.join(buffer)


def find_context(text, query):
    words = text.split()
    q = query.lower()

    for i, w in enumerate(words):
        if q in w.lower():
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            return ' '.join(words[start:end])

    return None


def iter_files(path):
    if os.path.isdir(path):
        for name in os.listdir(path):
            yield os.path.join(path, name)
    else:
        yield path


def analyze(path, query):
    for file in iter_files(path):
        for timestamp, text in parse_log(file):
            text_log = find_context(text, query)

            if text_log:
                print(f'Файл: {os.path.basename(file)}')
                print(f'Время: {timestamp}')
                print(f'Текст ошибки: {text_log}')
                return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to folder or file')
    parser.add_argument('-t', '--text', help='text to search')

    args = parser.parse_args()
    analyze(args.path, args.text)


if __name__ == '__main__':
    main()
