def right_justify(s):
    buffer = 70 - len(s)
    print(' ' * buffer, s)

right_justify('monty')
