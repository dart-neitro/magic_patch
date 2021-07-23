magic_patch is a simple library that provides the ability to patch all instances of classes at once.


* Example 1 *
A project contains a few modules that imports datetime library
  
```python
# module 1
from datetime import datetime

...
```

```python
# module 2
from datetime import datetime

...
```

Using magic_patch you don't need to mock each module 

```python
# test
from unittest.mock import Mock
from magic_patch import magic_patch

from datetime import datetime  # import target object
from ... import start_module  # necessary to run imports 

datetime_mock = Mock()

with magic_patch(start_module, datetime, datetime_mock):
    # all done! - all modules patched!!!
    ...
```
