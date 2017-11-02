import os  # The notifier function


def notify(title, subtitle, message):
    t = 'title {!s}'.format(title)
    s = 'subtitle {!s}'.format(subtitle)
    m = 'message {!s}'.format(message)
    os.system(
        """osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Pop"'""".format(m, t, s))


#
#
if __name__ == '__main__':
    # Calling the function
    notify(title='A Real Notification', subtitle='with python', message='Hello, this is me, notifying you!')
