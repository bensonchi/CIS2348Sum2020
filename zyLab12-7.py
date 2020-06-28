# Name:Baichuan Chi
# PSID:1938207


def fat_burning_heart_rate(user_age):

    return float(0.7 * (220-user_age))


def get_age():
    data = int(input())
    if data < 18 or data > 75:
        raise ValueError('Invalid age.')
    return data


if __name__ == '__main__':
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {:.1f} bpm'.format(age, rate))
    except ValueError as exc:
        print(exc)
        print('Could not calculate heart rate info.\n')