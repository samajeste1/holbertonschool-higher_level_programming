#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# Trying to instantiate Animal will raise TypeError (expected behaviour)
try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print("TypeError:", e)
