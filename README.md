# py|pe | functional piplines
**Add pipe operators to python through introspection**  
The name **pype** was picked for it's _punny_ similarity to pipe. But it's also a [backronym](https://en.wikipedia.org/wiki/Backronym) for _**py**thon **p**ipe **e**xrpression_. 
 

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
This is rough roadmap, subject to change.    
- [x] Basic PoC using commas instead of pipes  
- [ ] Use introspection to allow usage with the "|" pipe character  
- [ ] Set up proper python module with setup.py
- [ ] Add generative testing using hypothesis
- [ ] Set up static analysis and automatic testing (travis and codeclimate)
- [ ] Publish to pypi
- [ ] Write a short article on the project and documentation
- [ ] Integrate external tools
  - [ ] [whatever](https://pypi.org/project/whatever/#description)
  - [ ] [PyToolz](https://github.com/pytoolz/toolz)
 
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

---
_pype is built for fun interpreter and script usage, it's not meant for production systems_
