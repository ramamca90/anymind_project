import pytest
import sys
from mock import patch, MagicMock

sys.modules['APPLICATION'] = MagicMock()
