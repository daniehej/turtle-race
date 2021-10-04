# GeoGebra Version

The exciting turtle race has expanded to new platforms. After hours of hard work, we have finally implemented it in our favorite programming language: GeoGebra.

## Usage

Copy and paste the following command into the Input bar of GeoGebra Classic 5

```
Execute({"n=100", "score_t1 = 0", "score_t2 = 0", "score_t3 = 0", "a=0", "b=0", "c=0", "t1 = Turtle()", "t2 = Turtle()", "t3 = Turtle()", "StartAnimation()", "TurtleLeft(t1, 90°)", "TurtleForward(t1, 2)", "TurtleRight(t1, 90°)", "TurtleRight(t3, 90°)", "TurtleForward(t3, 2)", "TurtleLeft(t3, 90°)", "TurtleLeft(t2, 360°)", "Text(UnicodeToText({74, 105, 109}), (-1.5, 2))", "Text(UnicodeToText({74, 111, 104, 110, 110, 121}), (-1.5, 0))", "Text(UnicodeToText({74, 111, 110, 110, 97}), (-1.5, -2))", "r1 = RandomUniform(0, 9, n)", "r2 = RandomUniform(0, 9, n)", "r3 = RandomUniform(0, 9, n)", "i=1", "Repeat(n, SetValue(a, floor(r1(i))*360°), TurtleLeft(t1, a), TurtleForward(t1, 1), SetValue(b, floor(r2(i))*360°), TurtleLeft(t2, b), TurtleForward(t2, 1), SetValue(c, floor(r3(i))*360°), TurtleLeft(t3, c), TurtleForward(t3, 1), SetValue(i, i+1))"})
```

For other languages, replace the `Execute` command with the relevant command for your language as described in the (GeoGebra Wiki)[https://wiki.geogebra.org/en/Execute_Command]. (Use the selector at the bottom of the page.)

For example, if your GeoGebra is in Danish, use

```
Udfør({"n=100", "score_t1 = 0", "score_t2 = 0", "score_t3 = 0", "a=0", "b=0", "c=0", "t1 = Turtle()", "t2 = Turtle()", "t3 = Turtle()", "StartAnimation()", "TurtleLeft(t1, 90°)", "TurtleForward(t1, 2)", "TurtleRight(t1, 90°)", "TurtleRight(t3, 90°)", "TurtleForward(t3, 2)", "TurtleLeft(t3, 90°)", "TurtleLeft(t2, 360°)", "Text(UnicodeToText({74, 105, 109}), (-1.5, 2))", "Text(UnicodeToText({74, 111, 104, 110, 110, 121}), (-1.5, 0))", "Text(UnicodeToText({74, 111, 110, 110, 97}), (-1.5, -2))", "r1 = RandomUniform(0, 9, n)", "r2 = RandomUniform(0, 9, n)", "r3 = RandomUniform(0, 9, n)", "i=1", "Repeat(n, SetValue(a, floor(r1(i))*360°), TurtleLeft(t1, a), TurtleForward(t1, 1), SetValue(b, floor(r2(i))*360°), TurtleLeft(t2, b), TurtleForward(t2, 1), SetValue(c, floor(r3(i))*360°), TurtleLeft(t3, c), TurtleForward(t3, 1), SetValue(i, i+1))"})
```

## Random Direction
For a fun version where turtles go in random directions use the following command and try modifying the `angle` parameter (The unit is radians, or degrees with °).

```
Execute({"n=100", "angle=1", "score_t1 = 0", "score_t2 = 0", "score_t3 = 0", "a=0", "b=0", "c=0", "t1 = Turtle()", "t2 = Turtle()", "t3 = Turtle()", "StartAnimation()", "TurtleLeft(t1, 90°)", "TurtleForward(t1, 2)", "TurtleRight(t1, 90°)", "TurtleRight(t3, 90°)", "TurtleForward(t3, 2)", "TurtleLeft(t3, 90°)", "TurtleLeft(t2, 360°)", "r1 = RandomUniform(-1*angle, angle, n)", "r2 = RandomUniform(-1*angle, angle, n)", "r3 = RandomUniform(-1*angle, angle, n)", "i=1", "Repeat(n, SetValue(a, r1(i)), TurtleLeft(t1, a), TurtleForward(t1, 1), SetValue(b, r2(i)), TurtleLeft(t2, b), TurtleForward(t2, 1), SetValue(c, r3(i)), TurtleLeft(t3, c), TurtleForward(t3, 1), SetValue(i, i+1))"})
```
