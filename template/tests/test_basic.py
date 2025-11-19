import pytest

def test_imports():
    """Test that key libraries can be imported."""
    import pandas
    import polars
    import numpy
    
    assert pandas.__version__ is not None
    assert polars.__version__ is not None
    assert numpy.__version__ is not None

def test_project_structure():
    """Test that essential directories exist."""
    import os
    
    required_dirs = [
        "data",
        "notebooks",
        "reports",
        "scripts",
        "src",
        "config",
    ]
    
    # This test assumes it's running from the project root
    # In the template, we might need to be careful about where pytest is run
    # But for a generated project, this should pass if run from root.
    for d in required_dirs:
        assert os.path.exists(d), f"Directory {d} missing"
