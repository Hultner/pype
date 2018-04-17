# pype | functional piplines
**Add pipe operators to python through introspection**  
This is created for fun interpreter and script usage, not meant for production systems.

The idea is to allow for pipestyle programming in python eg.
```python
>>> p(
...   [1,2,3]
...   | lambda x: x*2
...   | sum
... )
 12
 ```

## Roadmap
This is rough roadmap  
 [x] Basic PoC using commas instead of pipes
 [ ] Use introspection to allow usage with the "|" pipe character
 [ ] Set up proper python module with setup.py
 [ ] Add generative testing using hypothesis
 [ ] Set up static analysis and automatic testing (travis and codeclimate)
 [ ] Publish to pypi
 [ ] Write a short article on the project and
 
## PoC version
 This is how the tool can currenly be used

```python
>>>
 >>> p(
 ...  [True, False, 1, 3],
 ...  all,
 ...  lambda x: "It's true" if x else "They lie"
 ... )
 'They lie'

```
