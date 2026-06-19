# Key Definitions — Problem Solving with Algorithms & Data Structures

## Core Concepts

**Computer Science** — The study of problems, problem-solving, and the solutions that result (including problems with _no_ solution). Not the study of computers — those are just tools.

**Algorithm** — A finite, step-by-step set of instructions that solves any instance of a problem. _Algorithms are solutions._

**Computable** — A problem is computable if an algorithm exists to solve it.

**Programming** — Encoding an algorithm into a notation (a programming language) so a computer can run it. No algorithm → no program.

---

## Abstraction

**Abstraction** — Separating the _logical_ view (what it does) from the _physical_ view (how it works).

**Logical perspective** — The user's view: using a system through its interface, without knowing the internal details. _(e.g. driving a car)_

**Physical perspective** — The "under the hood" view: how something actually works internally. _(e.g. a mechanic's view of a car)_

**Interface** — The operations/functions exposed to the user; hides the implementation.

**Procedural abstraction** — Knowing _what_ a function does and how to call it, without knowing _how_ it works inside. A "black box" view.
_Example:_ `math.sqrt(16)` → you use it without knowing the algorithm behind it.

---

## Data Concepts

**Data type** — Gives meaning to raw binary data so it matches a real-world concept (e.g. integers, with operations like `+`, `−`, `×`).

**Primitive data type** — A basic, built-in data type provided by the language (int, float, etc.).

**Control constructs** — Language features used to express algorithm steps: **sequence**, **selection** (decisions), **iteration** (loops).

---

## Data Abstraction

**Abstract Data Type (ADT)** — A logical description of data + the operations allowed on it, independent of implementation. Defines the _what_, not the _how_.

**Information hiding** — Hiding implementation details from the user; only the interface is visible.

**Data structure** — The actual _implementation_ of an ADT — the concrete way the data is organized in code.

---

## Algorithm Analysis

**Intractable problem** — A problem with no algorithm that can solve it in a realistic amount of time.

**Algorithm comparison** — Different algorithms can solve the same problem with different efficiency (time/memory). Studying algorithms gives tools to compare them independent of the machine running them.
