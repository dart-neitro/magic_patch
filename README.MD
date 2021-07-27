The magic_patch is a simple library that provides the ability to patch an object in different scopes at once.
Now you can patch objects easily like magic.


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

Using magic_patch you don't need to patch each module manually 

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



* Example 2 *
  A project contains a few modules that import the datetime class from datatime library
  There are different names for the target object.
  The magic_patch provides the ability to examine all available variables in each module

```python
# module 1
from datetime import datetime

...
```

```python
# module 2
from datetime import datetime as new_name_datetime

...
```

Just set up the option search_by_all_names=True and magic_patch finds your target with other names

```python
# test
from unittest.mock import Mock
from magic_patch import magic_patch

from datetime import datetime  # import target object
from ... import start_module  # necessary to run imports 

datetime_mock = Mock()
with magic_patch(start_module, datetime, datetime_mock, search_by_all_names=True):
    # all done! - all modules patched!!!
    ...
```

Happy magic patching!