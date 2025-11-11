-- Day 1: Introduction to Lean
-- Basic arithmetic and expressions

def add (x y : Nat) : Nat := x + y

def factorial : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * factorial n

#eval add 3 4
#eval factorial 5
