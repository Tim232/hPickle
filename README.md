# hPickle

A package for handling pickle binary files

`pip install py-hPickle`

Example : 
```python
import hPickle

data = hPickle.load('example.bin')
print(data)
print()

data['test'] = 100
data = hPickle.save('example.bin', data)
print(data)
print()

check = hPickle.check('example.bin')
print(check)
```

Output : 
```
{
    'test' : 0
}

{
    'test' : 100
}

True
```
