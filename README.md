# duplicador

Description. 
Pacote simples para duplicar valores de uma lista de inteiros:
	- Recebe uma lista de inteiros
	- Retorno os valores duplicados

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install duplicador
```

## Usage

```python
from duplicador import duplicar_lista
print(duplicar_lista([1, 2, 3]))  # [2, 4, 6]


---

### ⚙️ `pyproject.toml` (moderno e recomendado)

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "duplicador"
version = "0.1.0"
description = "Pacote simples para duplicar valores de uma lista"
authors = [{ name="Michael Santos", email="mackellmichael@hotmail.com" }]
license = "MIT"
readme = "README.md"
requires-python = ">=3.7"


```

## Author
Michael Santos

## License
[MIT](https://choosealicense.com/licenses/mit/)