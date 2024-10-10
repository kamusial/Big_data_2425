import foo.some
from bar.other import Example

foo.some.function()

print(foo.__doc__)
print(foo.some.__doc__)


ex = Example()
ex.attribute = 1000

print(ex)
print(dir(ex))
