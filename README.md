# Work Requirement 2: Managing Technical Debt and Improving Legacy Code

In this assignment, I looked at four code examples from Chapter 3.2 and tried to improve them. The main goal was to make the code easier to understand, change and test. I focused on keeping the solutions simple because we don't need a real database or any external libraries for this assignment.

## 1. Undocumented Converter (`converter.py`)

**What was the problem?**

The original code was quite confusing because the class was just called `Converter`. It wasn't clear what it was converting, and there was no explanation for the numbers being used. You would have to look at the formula to work out that it converts Fahrenheit to Celsius.

**What I changed and why**

I changed it to a function called `fahrenheit_to_celsius` and added a short docstring explaining what it does. I also wrote the calculation in a way that makes it easier to recognise. I don't think a whole class is needed for one simple conversion. This makes the code easier for someone else to understand without having to guess what it does.

## 2. Tightly Coupled Order Class (`order.py`)

**What was the problem?**

The original `Order` class was doing too much. It depended on details from the `User` object and also contained SQL code for saving orders. This means that if something changed in the user model or database, the `Order` class might also need to be changed. The hardcoded order ID of `123` was another problem.

**What I changed and why**

I separated the responsibilities. The `Order` class now only holds information about the order. I used an `OrderService` to handle saving, and an `InMemoryOrderRepository` as a simple example of storage. The order also receives the user information it needs instead of depending on the whole `User` object. I think this is better because each part has a clearer purpose, and we can change how orders are stored without changing the order itself.

## 3. Duplicated Discount Logic (`discount.py`)

**What was the problem?**

The same discount calculation was written in two places: when calculating the cart total and when creating the invoice. The problem with this is that if the discount changes, we would need to remember to update both places. If we forget one, the cart and invoice could show different totals.

**What I changed and why**

I created one function called `discounted_total(items)` and used it in both places. I also gave the discount amount and minimum total clear names instead of leaving the numbers directly in the calculation. This avoids repeating the same logic and makes future changes easier. I kept the original rule where a 10% discount applies when the total is **over** 5000 cents.

## 4. Long `process_order` Method (`process_order.py`)

**What was the problem?**

The original `process_order` function was responsible for too many things at once. It calculated the total, applied discounts, saved the order and sent a notification. Having everything in one function makes it harder to understand what is happening and harder to test individual parts.

**What I changed and why**

I split some of the work into smaller functions, including `calculate_total` and `apply_discount_code`. The main `process_order` function now uses those functions and calls a repository and an optional notifier for the other tasks. I used simple stubs instead of connecting to a real database or sending notifications. This makes the code easier to follow, and it also means that one part can be changed without having to rewrite everything else.

## How to run the code

The examples use Python 3.9 or newer and don't need any extra packages. Run these commands in the project folder:

```bash
python converter.py
python order.py
python discount.py
python process_order.py
```

To run the tests:

```bash
python -m unittest test_examples.py
```

## Personal reflection

I think tight coupling is the most difficult of these problems because it can affect several parts of a project at the same time. If I was working on code that someone else had written, I would find it stressful to change one thing without knowing what else might break. The Order example made me understand why it is important to separate responsibilities. It is much easier to work with code when each class has a clear purpose. I also think this makes testing less complicated, especially when you don't need to set up a real database just to check whether the code works.
