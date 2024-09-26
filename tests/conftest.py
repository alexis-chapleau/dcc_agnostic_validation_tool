import sys
from unittest.mock import MagicMock

# Mock maya.cmds
sys.modules['maya'] = MagicMock()
sys.modules['maya.cmds'] = MagicMock()

# Mock hou
sys.modules['hou'] = MagicMock()
