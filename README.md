# OUK-AI-Training-Repo-2025
Name : Cheruiyot Kipngeno Email;Cherukip@gmail.com Tel : 254722432764
This repository contains a small, well-tested BMI calculator.

Contact
-------
Name: Cheruiyot Kipngeno
Email: Cherukip@gmail.com
Tel: 254722432764

Files added
-----------
- `bmi/bmi_calculator.py` - small library with `calculate_bmi` and `bmi_category` functions.
- `bmi.py` - lightweight CLI wrapper so you can run `python bmi.py` as shown below.
- `tests/test_bmi.py` - pytest unit tests for the library.

Usage
-----
Interactive (prompts):

```sh
python bmi.py
```

Command-line (weight kg, height m):

```sh
python bmi.py 70 1.75
```

Or import the functions in your code:

```py
from bmi.bmi_calculator import calculate_bmi, bmi_category

print(calculate_bmi(70, 1.75))
print(bmi_category(22.86))
```

Testing
-------
Install test dependency and run pytest:

```powershell
pip install pytest; pytest -q
```

Notes
-----
- The library validates inputs and raises ValueError for non-positive weight/height.
- This README replaces the inline script that was previously shown here and provides small reusable modules and tests.
