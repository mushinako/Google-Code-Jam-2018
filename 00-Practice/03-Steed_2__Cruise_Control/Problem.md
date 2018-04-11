# Steed 2: Cruise Control
## Welcome to the Practice Session!
If you experience any technical issues interfering with your ability to
participate in the Practice Session, please email us immediately at
codejam@google.com. We will have limited support during the session, but will
get back to you as soon as possible. For all other feedback, we invite you to
submit your thoughts and suggestions via this
[feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfE09X8Zdotkf8FYe-YczYs2eUBZtOC1yoxObpJrQiMAo0Qqg/viewform)
after the Practice Session.

## Problem
Annie is a bus driver with a high-stress job. She tried to unwind by going on a
Caribbean cruise, but that also turned out to be stressful, so she has recently
taken up horseback riding.

Today, Annie is riding her horse to the east along a long and narrow one-way
road that runs west to east. She is currently at kilometer 0 of the road, and
her destination is at kilometer **D**; kilometers along the road are numbered
from west to east.

There are **N** other horses traveling east on the same road; all of them will
go on traveling forever, and all of them are currently between Annie's horse
and her destination. The i-th of these horses is initially at kilometer **Kᵢ**
and is traveling at its maximum speed of **Sᵢ** kilometers per hour.

Horses are very polite, and a horse H₁ will not pass (move ahead of) another
horse H₂ that started off ahead of H₁. (Two or more horses can share the same
position for any amount of time; you may consider the horses to be single
points.) Horses (other than Annie's) travel at their maximum speeds, except
that whenever a horse H₁ catches up to another slower horse H₂, H₁ reduces its
speed to match the speed of H₂.

Annie's horse, on the other hand, does not have a maximum speed and can travel
at any speed that Annie chooses, as long as it does not pass another horse. To
ensure a smooth ride for her and her horse, Annie wants to choose a single
constant "cruise control" speed for her horse for the entire trip, from her
current position to the destination, such that her horse will not pass any
other horses. What is the maximum such speed that she can choose?

## Input
The first line of the input gives the number of test cases, **T**; **T** test
cases follow. Each test case begins with two integers **D** and **N**: the
destination position of all of the horses (in kilometers) and the number of
other horses on the road. Then, **N** lines follow. The i-th of those lines has
two integers **Kᵢ** and **Sᵢ**: the initial position (in kilometers) and
maximum speed (in kilometers per hour) of the i-th of the other horses on the
road.

## Output
For each test case, output one line containing `Case #x: y`, where `x` is the
test case number (starting from 1) and `y` is the maximum constant speed (in
kilometers per hour) that Annie can use without colliding with other horses. y
will be considered correct if it is within an absolute or relative error of
10⁻⁶ of the correct answer. See the
[FAQ](https://codejam.withgoogle.com/codejam/resources/faq#real-number-behavior)
for an explanation of what that means, and what formats of real numbers we
accept.

## Limits
1 ≤ **T** ≤ 100.
0 < **Kᵢ** < **D** ≤ 109, for all i.
**Kᵢ** ≠ **Kⱼ**, for all i ≠ j. (No two horses start in the same position.)
1 ≤ **Sᵢ** ≤ 10000.
Time limit: 10 seconds per test set.
Memory limit: 1GB.

## Test set 1 (Visible)
1 ≤ **N** ≤ 2.

## Test set 2 (Hidden)
1 ≤ **N** ≤ 1000.

## Sample
### Input
```
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
```

### Output
```
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
```

In Sample Case #1, there is one other (very slow!) horse on the road; it will
reach Annie's destination after 25 hours. Anything faster than 101 kilometers
per hour would cause Annie to pass the horse before reaching the destination.

In Sample Case #2, there are two other horses on the road. The faster horse
will catch up to the slower horse at kilometer 240 after 2 hours. Both horses
will then go at the slower horse's speed for 1 more hour, until the horses
reach Annie's destination at kilometer 300. The maximum speed that Annie can
choose without passing another horse is 100 kilometers per hour.
