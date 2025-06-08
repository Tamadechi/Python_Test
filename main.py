def in_autotests_we_trust(a, b):
    if a == b:
        print('PASSED')
    else:
        print('FAILED')

in_autotests_we_trust(9, '10')

in_autotests_we_trust(0, 0)
