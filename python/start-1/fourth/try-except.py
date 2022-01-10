try:
    123 + 'hello'
except ValueError:
    print('wrong value')
except TypeError:
    print('wrong type')
finally:
    print("Execpt")

# except (ValueError, TypeError):
#     print('wrong value or type')
# int('lol')
