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
    "age": [22, 25, 47, 35, 46, 29, 31],
    "income": [30000, 32000, 58000, 45000, 60000, 41000, 47000],
})

histogram(df, "age")
scatterplot(df, "age", "income")
```

## License

MIT License. See [LICENSE](LICENSE) for details.
