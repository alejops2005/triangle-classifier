# Triangle Classifier

## Project Description

This project classifies three side lengths as Invalid, Equilateral, Isosceles, Scalene, Right Isosceles, or Right Scalene. A valid triangle must have three positive side lengths, and the sum of any two sides must be greater than the remaining side. After checking validity, the classifier compares the squared longest side with the sum of the squares of the other two sides to detect a right angle. It uses a floating-point tolerance for that comparison.

## How to Run the Tests

You need Python and pytest. The project lists pytest in `requirements.txt`; install the listed test dependency with:

```powershell
py -m pip install -r requirements.txt
```

Run the tests from the project folder with:

```powershell
py -m pytest -v
```

## Equivalence Classes and Boundary Values

The unit tests cover these input categories:

- A zero side length and a negative side length are invalid.
- Positive side lengths that violate the triangle inequality, such as (1, 2, 4), are invalid.
- The boundary case (1, 2, 3) is degenerate: two sides add up exactly to the third, so it is not a valid triangle.
- Valid triangles include an equilateral triangle (4, 4, 4), an isosceles triangle (3, 3, 5), and a scalene triangle (4, 5, 6).
- The tests also cover a right scalene triangle with its longest side listed first (5, 3, 4), and a right isosceles triangle with floating-point side lengths (5, 5, 5 * sqrt(2)).

The triangle inequality requires the sum of each pair of sides to be greater than the third side. Equality is the degenerate boundary, not a valid triangle. To identify right triangles with floating-point side lengths, the classifier uses a closeness check rather than requiring the two calculations to be exactly equal. An equilateral triangle cannot be right: for three equal positive sides x, the sum of the squares of two sides is 2x², not x².

## Copilot Review Log

All nine unit tests were drafted using Copilot autocomplete and reviewed.

| Test name | Copilot suggested it? | Kept or edited? | Why |
|---|---|---|---|
| `test_zero_side_is_invalid` | Yes | Edited | Removed redundant assertions. |
| `test_negative_side_is_invalid` | Yes | Edited | Removed redundant assertions. |
| `test_triangle_inequality_failure_is_invalid` | Yes | Edited | Removed redundant assertions. |
| `test_degenerate_triangle_is_invalid` | Yes | Kept | The test covers the equality boundary of the triangle inequality. |
| `test_equilateral_triangle` | Yes | Kept | The test checks the equilateral classification. |
| `test_isosceles_triangle` | Yes | Kept | The test checks the isosceles classification. |
| `test_scalene_triangle` | Yes | Edited | Copilot incorrectly expected "Scalene" for (3, 4, 5), but the specification requires "Right Scalene". I changed the input to (4, 5, 6). |
| `test_reordered_right_triangle` | Yes | Kept | The test checks right-triangle detection when the longest side is listed first. |
| `test_floating_point_right_isosceles_triangle` | Yes | Edited | Changed the input to use `math.sqrt(2)` instead of `math.hypot(1, 1)`. |

### Rejected Copilot Suggestion

While generating the unit tests, Copilot suggested the following assertion for the scalene triangle test:

```python
assert classify_triangle(3, 4, 5) == "Scalene"
```

I rejected this assertion because (3, 4, 5) is a right triangle, since 3² + 4² = 5². According to the assignment requirements, the expected output should be "Right Scalene", not "Scalene".

Instead, I changed the test input to (4, 5, 6), which is a valid scalene triangle without a right angle. This allowed me to test the correct classification while fixing Copilot's mistake.

## Acceptance Criteria

Given a customer provides the side lengths of a triangle (2, 3, 4)

When the triangle classifier analyzes these points

Then the expected output should be "Scalene", providing confirmations that it is a valid triangle.

Given a customer provides the side lengths of a triangle (5, 3, 8)

When the triangle classifier analyzes these points

Then the expected output should be "Invalid", these measurements don't make a valid triangle.

Given a customer provides the side lenghts of a triangle (3, 4, 5)

When the triangle classifier analyzes these points

Then the expected out should be "Right Scalene", these measurements make a valid triangle.

## AI Use Disclosure

GitHub Copilot was used to draft the unit tests and assist with this README documentation. ChatGPT was used for planning, guidance, and reviewing suggestions. I wrote the acceptance criteria and the acceptance test manually; Copilot did not generate them. AI assistance was reviewed, and the test changes are described above.