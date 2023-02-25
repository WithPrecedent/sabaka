"""
test_sabaka: tests functions and classes in the sabaka package
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2023, Corey Rayburn Yung
License: Apache-2.0

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

ToDo:
    Figure out how to design unit tests for exceptions and design those tests.
        
    
"""
from __future__ import annotations
import dataclasses
from typing import Any, ClassVar, Optional

import sabaka


@dataclasses.dataclass
class TestClass(object):
    
    some_attribute: Optional[Any] = None


def test_errors() -> None:
    instance = TestClass()
    for attribute in ['some_attribute', 'another_attribute']:
        try:
            getattr(instance, attribute)
        except AttributeError:
            raise sabaka.NotAttribute(instance, attribute)
    return
        
if __name__ == '__main__':
    test_errors()
