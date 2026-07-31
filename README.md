# viz_library

A small, beginner-friendly Python visualization library built with
`pandas` and `matplotlib`.

## Features

- `histogram(df, column)` — plot a histogram of one column
- `scatterplot(df, x_column, y_column)` — plot a scatterplot of two columns

## Installation

Clone this repository and install it locally with pip:

```bash
pip install .
```

For development (editable install), use:

```bash
pip install -e .
```

## Usage

```python
import pandas as pd
from viz_library import histogram, scatterplot

df = pd.DataFrame({
    "Absences": [2, 8, 15, 0, 5, 11, 3, 9],
    "Scores": [92, 85, 74, 96, 88, 79, 90, 83],
})

# Both functions return the Axes object, so you can customize it further,
# like overriding the auto-generated title:
ax1 = histogram(df, "Absences")
ax1.set_title("Student Scores and Absenteeism")

ax2 = scatterplot(df, "Absences", "Scores")
ax2.set_title("Student Scores and Absenteeism")
```

## License

MIT License. See [LICENSE](LICENSE) for details.
