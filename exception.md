# **Errors and Exception Handling in Python**

## 🧨 What is an Error?

* An **error** is a problem in a program that stops the execution.
* Errors can happen due to:

  * Wrong code
  * Unexpected input
  * External factors (like missing files, network issues)


## 🧱 Two Types of Errors in Python

| Type              | Meaning                                                        |
| ----------------- | -------------------------------------------------------------- |
| **Syntax Errors** | Mistakes in the code structure (missing colon, brackets, etc.) |
| **Exceptions**    | Errors that happen **during execution** (e.g., divide by zero) |


## 🧾 Example of Syntax Error

```python
# Missing colon
if True
    print("Hello")
```

📌 Output:

```
SyntaxError: expected ':'
```


## ⚠️ Example of Runtime Exception

```python
a = 10
b = 0
print(a / b)
```

📌 Output:

```
ZeroDivisionError: division by zero
```

## 🧠 Common Exception Types in Python

Here’s a table of **frequently occurring exceptions** you might see:

| Exception Name      | When it Happens                            | Example Code                        |
| ------------------- | ------------------------------------------ | ----------------------------------- |
| `ZeroDivisionError` | Divide by 0                                | `10 / 0`                            |
| `TypeError`         | Wrong data type used                       | `"2" + 2`                           |
| `ValueError`        | Correct type but wrong value               | `int("abc")`                        |
| `IndexError`        | List index out of range                    | `my_list[10]`                       |
| `KeyError`          | Accessing missing key in dictionary        | `my_dict["not_found"]`              |
| `AttributeError`    | Accessing non-existent attribute or method | `5.append(2)`                       |
| `ImportError`       | Module not found                           | `import somethingfake`              |
| `NameError`         | Using variable not defined                 | `print(x)` (when x is not declared) |
| `FileNotFoundError` | Trying to open a file that doesn’t exist   | `open("missing.txt")`               |


## 🛡️ What is Exception Handling?

Exception Handling is a **way to protect your program** from crashing when an error occurs.

Python uses:

* `try`
* `except`
* `else`
* `finally`


### ✅ Basic Structure

```python
try:
    # Code that may raise an exception
except SomeError:
    # What to do if error happens
else:
    # Run if no error
finally:
    # Always run (cleanup, close file, etc.)
```


## 🔍 Examples of Exception Handling

### 🎯 Example 1: Catching Division by Zero

```python
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### 🎯 Example 2: Handling Multiple Exceptions

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
```


### 🎯 Example 3: Using `finally`

```python
try:
    file = open("myfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file... (even if error occurred)")
```

### ✅ Best Practice: Catch Specific Exceptions First

Avoid catching everything using just `except:` unless absolutely necessary.

✅ Good:

```python
except ValueError:
```

🚫 Avoid:

```python
except:
```



## 🏠 Homework

1. **Age Verifier**:

   * Ask the user for their age.
   * If age is valid (number), show in how many years they will be 100 years old.
   * Handle invalid input gracefully.

2. **Safe Divider**:

   * Ask two numbers from the user and divide them.
   * Handle ZeroDivisionError and ValueError.

3. **File Reader**:

   * Ask the user for a file name and try to open it.
   * Show error message if file doesn't exist.
   * Use `finally` to print “Program End”.

---
### **YouTube Reference**
Watch the following YouTube video from my channel:
- [Watch the tutorial on YouTube](https://www.youtube.com/watch?v=pee2Zl3en6I)

✅ 1️⃣ Why Do We Write class AgeError(Exception)?

Because we are creating a custom exception.

👉 Exception is the parent class of all exceptions in Python.

When we write:

class AgeError(Exception):

We are telling Python:

👉 “AgeError is also an exception type.”

So Python can:

catch it in except

treat it like other errors

❌ If you don’t inherit from Exception
class AgeError:
    pass

Python will NOT treat it as an exception.
raise AgeError → error.

So inheritance is must.

✅ 2️⃣ Why Do We Write pass?

Because sometimes we don’t need extra code inside class.

pass means:
👉 “Empty class for now.”

We only need a name to identify the error.

Example
class AgeError(Exception):
    pass

raise AgeError("Age must be 18+")

Output:

AgeError: Age must be 18+
✅ 3️⃣ Real Meaning in Simple Words

👉 We create a new error type called AgeError
👉 Python now understands it as an exception
👉 We can raise & catch it

✅ 4️⃣ Real-Life Example

ATM example:

class LowBalanceError(Exception):
    pass

Because normal errors don’t explain problem clearly.

Instead of:

Exception: Error

We get:

LowBalanceError: Not enough balance

More professional 👍

🧠 Interview One-Line Answer

class AgeError(Exception) creates a user-defined exception by inheriting from the built-in Exception class so it can be raised and handled like other exceptions.

If you want next, I can explain:
👉 How custom exception works internally
👉 When to use custom vs built-in
👉 Advanced custom exception with __init__

Just tell me, Spoorthi 😎💻✨

give me full code of ageerror

Superrr 😎🔥 Let’s write a complete working program using AgeError.

✅ Full Code – Custom AgeError Example
class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("You must be 18 or older to register.")

    print("Registration successful!")

except ValueError:
    print("Please enter a valid number.")

except AgeError as e:
    print("Custom Exception:", e)

finally:
    print("Program finished.")

1️⃣ We create custom exception
class AgeError(Exception):
    pass

Now AgeError behaves like built-in exceptions.

2️⃣ Inside try block

Convert input to integer

If age < 18 → raise custom exception

3️⃣ Except blocks

ValueError → handles wrong input like "spoo"

AgeError → handles age below 18
 Make sure to subscribe to the channel for more Python tutorial and updates!
