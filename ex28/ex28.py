# LPTHW ex28.py - Boolean Practice

print("True and True: %r" % (True and True))
print("False and True: %r" % (False and True))
print("1 == 1 and 2 == 1: %r" % (1 == 1 and 2 == 1))
print('"test" == "test": %r' % ("test" == "test"))
print("1 == 1 or 2 != 1: %r" % (1 == 1 or 2 != 1))
print("True and 1 == 1: %r" % (True and 1 == 1))
print("False and 0 != 0: %r" % (False and 0 != 0))
print("True or 1 == 1: %r" % (True or 1 == 1))
print(': %r' % ("test" == "testing"))
print("1 != 0 and 2 ==1: %r" % (1 != 0 and 2 ==1))
print('"test" != "testing": %r' % ("test" != "testing"))
print('"test" == 1: %r' % ("test" == 1))
print("not (True and False): %r" % (not (True and False)))
print("not (1 == 1 and 0!= 1): %r" % (not (1 == 1 and 0!= 1)))
print("not (10 == 1 or 1000 == 1000): %r" % (not (10 == 1 or 1000 == 1000)))
print("not (1 != 10 or 3 == 4): %r" % (not (1 != 10 or 3 == 4)))

result = not ("testing" == "testing" and "Zed" == "Cool Guy")
print('not ("testing" == "testing" and "Zed" == "Cool Guy"): %r' % (result))

result = 1 == 1 and not ("testing" == 1 or 1 == 0)
print('1 == 1 and not ("testing" == 1 or 1 == 0): %r' % (result))

result = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print('"chunky" == "bacon" and not (3 == 4 or 3 == 3): %r' % (result))

result = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print('3 == 3 and not ("testing" == "testing" or "Python" == "Fun"): %r' % (result))
