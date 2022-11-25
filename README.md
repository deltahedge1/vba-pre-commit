# vba_pre_commit

pre-commit for vba solutions
-   pre-commit for vba projects
-   Free software: MIT license

# Quick Start
This works with pre-commit

1. Install pre-commit (if you have'nt already)
```
pip install pre-commit
```

2. Add a pre-commit yaml
```
touch .pre-commit-config.yaml
```

3. Inside the pre-commit yaml add
```yaml
repos:
-   repo: https://github.com/deltahedge1/vba-pre-commit
    rev: v0.1.1
    hooks:
    -   id: vba-pre-commit
```
4. Install hooks
```
pre-commit install
```

# Features

-   before each commit
    - extracts the vba code
    - zips the excel document which has the code
    - add all of this to src.vba
    - git adds ./src.vba/*

# TODO
- Handles only one excel vba code in the source folder