## Flask
- it is a python web dev framework
- aka micro framework or micro web framework as unlike Django it does't have any functionality out of the box like auth etc

---

### 🔎 What happens when you do `python -m some_module`?

1. **Python looks up the module** in `sys.path` (the list of directories where Python searches for modules).

   * This includes the current directory, installed site-packages, and the standard library.

2. **If it’s a simple module** (like `math.py` or `venv.py` in the stdlib):

   * Python just executes that file.
   * But it sets a special variable:

     ```python
     __name__ == "__main__"
     ```

     so the module can behave like a script.

3. **If it’s a package** (a directory with an `__init__.py` file):

   * Python does **not** execute `__init__.py` directly.
   * Instead, it looks for a file called:

     ```
     __main__.py
     ```

     inside that package and runs it.

---

### 📌 Examples

#### Running a single-file module:

```bash
python -m venv .venv
```

* `venv` is a module (`venv/__init__.py` and supporting files).
* It has a **`__main__.py`** file inside `venv/`.
* So Python runs `venv/__main__.py`.

#### Running a package:

```bash
python -m http.server
```

* `http` is a package.
* Inside `http/`, there’s a folder `server/` with a `__main__.py`.
* That file gets executed.

#### Your own package:

Suppose you have this structure:

```
myapp/
  __init__.py
  __main__.py
  utils.py
```

Then:

```bash
python -m myapp
```

will run `myapp/__main__.py`.

---

✅ **Summary:**

* If the target is a **module file** → Python runs it directly.
* If the target is a **package** → Python runs the package’s `__main__.py`.

---

Do you want me to also show you a **mini experiment** where you create your own `__main__.py` and run it with `-m` to see this in action?

---

Excellent follow-up 👌 — `__init__.py` and `__main__.py` often confuse people, so let’s clear it up:

---

## 📌 `__init__.py`

* **Purpose:** Marks a directory as a Python package and **runs initialization code** when you **import** that package.
* Without it (in older Python versions <3.3), Python wouldn’t even recognize the folder as a package.
* Since Python 3.3+, it’s optional (because of *implicit namespace packages*), but still widely used.

### 🔹 What it does

* Runs **only when you import the package**:

  ```python
  # mypkg/__init__.py
  print("mypkg is being imported!")
  ```

  ```python
  import mypkg   # prints "mypkg is being imported!"
  ```

* Can **expose a public API**:

  ```python
  # mypkg/__init__.py
  from .utils import add, subtract
  ```

  Now:

  ```python
  from mypkg import add
  ```

* Can hold **package-level variables/configs**:

  ```python
  __version__ = "1.0.0"
  ```

---

## 📌 `__main__.py`

* **Purpose:** Defines what happens when you run the package with `python -m package_name`.
* Think of it as the **entry point for execution**.

### 🔹 What it does

* Runs **only when executed as a script**:

  ```python
  # mypkg/__main__.py
  print("mypkg is being run directly!")
  ```

  ```bash
  python -m mypkg
  # prints "mypkg is being run directly!"
  ```

---

## ⚖️ Difference between them

| File          | When it runs                             | Used for                       |
| ------------- | ---------------------------------------- | ------------------------------ |
| `__init__.py` | When the package is **imported**         | Initialize package, expose API |
| `__main__.py` | When the package is **executed with -m** | Define package entry point     |

---

✅ **In short:**

* `__init__.py` → makes a directory a package, runs on **import**.
* `__main__.py` → makes a package executable, runs on **python -m package**.

---

Would you like me to **make a tiny package with both `__init__.py` and `__main__.py`** so you can see how `import mypkg` vs `python -m mypkg` behave differently?
Got it 👍 — here’s the **short demo**:

---

### 📂 Folder: `mypkg/`

```
mypkg/
 ├── __init__.py
 └── __main__.py
```

### `__init__.py`

```python
print("mypkg imported!")
```

### `__main__.py`

```python
print("mypkg executed with -m!")
```

---

### ✅ Usage:

```python
import mypkg
# 👉 prints: mypkg imported!
```

```bash
python -m mypkg
# 👉 prints: mypkg executed with -m!
```

---

⚡ That’s the difference:

* **import → `__init__.py`**
* **-m run → `__main__.py`**

Do you also want me to show what happens if **both files have functions**, so you can see how they differ in practice?
---
Perfect 👌 Let’s extend the demo with **functions** in both files.

---

### 📂 Folder: `mypkg/`

```
mypkg/
 ├── __init__.py
 └── __main__.py
```

### `__init__.py`

```python
def hello():
    print("Hello from __init__.py!")

print("mypkg imported!")   # runs on import
```

### `__main__.py`

```python
def run():
    print("Running from __main__.py!")

print("mypkg executed with -m!")   # runs on `python -m mypkg`
```

---

### ✅ Usage:

**Importing as a library:**

```python
import mypkg
mypkg.hello()
```

Output:

```
mypkg imported!
Hello from __init__.py!
```

**Running as a script:**

```bash
python -m mypkg
```

Output:

```
mypkg executed with -m!
```

---

👉 Summary:

* `__init__.py` → setup + functions available when **imported**.
* `__main__.py` → entry point when **executed with `-m`**.

Do you want me to also explain what happens if `__main__.py` is missing?
