# Curriculum Vitae

## Experience

### Career Break

_May 2023 – present_

• Career break for health reasons; now recovered and returning to full-time work.

• The projects below were built during this period through sustained self-directed study (and are available on
GitHub), alongside courses in computer architecture, memory management and others.

### Junior Software Consultant

_July 2022 – April 2023 | Realworld Systems | Cambridge, UK_

• Worked as a developer on the GIS software GE Smallworld using Magik (OOP)

• Built a new address database and implemented an importer to load approx. 6 million records for production use.

• Wrote and maintained code: regression testing, code reviews, wrote and delivered patches; used Git for version control.

### Research Intern

_June 2019 – August 2019 | Institute for Mathematical Innovation, University of Bath | Bath, UK_

• Independently scoped and conducted a research project on university transport logistics, working without a defined brief to formulate research questions and gather data from the university and local council.

• Analysed and visualised geospatial data using QGIS; produced a research poster and presented findings to academic staff.

## Projects

### grape (NFA-based regex engine)

_C++ | 2026_

• Built a grep-style regex engine by using Thompson’s NFA construction to create an NFA from a regex, and then running the NFA on an input string.

• Diverged from the backtracking approach recommended by the CodeCrafters’ tutorial after discovering that some regex engines avoid this approach due to its worst-case behaviour (exponential time complexity), and favour DFA/NFA instead. I had studied these during my degree and was curious to see a real-world application.

• Pipeline: tokeniser → shunting-yard postfix conversion → Thompson’s construction → NFA simulation.

• Supports character classes, shorthand classes (\d, \w, \s), alternation, quantifiers, concatenation, and substring matching.

### Ray Tracer with Photon Mapping

_C++ | 2026_

• Undergraduate project extended and refactored in 2026: a Whitted-style ray tracer with global illumination via photon mapping, implemented using Jensen’s 1996 paper.

• Implements separate caustic and global photon maps stored in a kd-tree with k-NN lookup, multi-object scenes (including spheres and polymeshes), Fresnel refraction, reflection, Phong shading, point lights.

• Returned to this project in 2026 with more experience: reworked it to use smart pointers, rather than the C++98 style memory management I was previously using, finalised a few features (Phong normal interpolation for smooth mesh shading) and extended it to include features from my Rust path tracer, such as gamma correction and anti-aliasing.

### Lambda Calculus Interpreter with Krivine Abstract Machine

_Haskell | 2026_

• Undergraduate project revisited in 2026. Evaluates lambda calculus expressions (a minimal model of computation) using the Krivine Abstract Machine, a call-by-name evaluator.

• Rewrote the Krivine Abstract Machine from scratch using closures for a correct implementation.

### Hack Assembler

_Haskell | 2026_

• A two-pass assembler for the Hack instruction set, from the course ’From NAND to Tetris’.

### CHIP-8 Emulator

_Rust | 2025_

• An interpreter capable of running any standard CHIP-8 program. Passes Timendus’ test suite and runs the games in John Earnest’s CHIP-8 Archive.

### Path Tracer

_Rust | 2025_

• Path tracer following Peter Shirley’s Ray Tracing series, translating it from C++ to Rust. Features include: positionable camera, BVH, volumes, emissive surfaces, materials (lambertian, dielectric, metal), Perlin noise, spheres and quadrilaterals.

## Education

### Mathematics MSc

_2021 | University of London | London, UK_

Modules : Graph Theory, Number Theory & Geometry, Algebraic Number Theory, Linear & Non-Linear Optimisation, Methods in Finance, essay on Fermat’s Last Theorem, dissertation on Riemann surfaces.

### Mathematics BSc (Hons.)

_2020 | University of Bath | Bath, UK_

Studied 7 computer science modules (42 ECTS credits), including cryptography, algorithms and time complexity. I particularly enjoyed programming projects:

• Advanced Computer Graphics: building a ray tracer with photon mapping in C++,

• Functional Programming coursework: building a lambda calculus interpreter with the Krivine Abstract Machine in Haskell,

• Numerical Analysis coursework in MATLAB

Throughout my degree I completed coursework in C++, Haskell, MATLAB and R.

I also studied pure and applied maths modules such as: Algebraic Curves, Representation Theory of Finite Abelian Groups, Continuum Mechanics, Modelling and Dynamical Systems, Vector Calculus and PDEs.

### A-Levels

_Gower College Swansea | 2017 | Swansea, UK_

A Levels: Mathematics (A*), Further Mathematics (A*), Chemistry (A).
UKMT Gold award, and represented Gower College in the team challenge.

## Courses

### From NAND to Tetris Pt 1

_2025-2026 | Hebrew University of Jerusalem | Online_

Built a general-purpose computer from first principles in a hardware description language (HDL), from elementary NAND-based logic gates through an ALU, RAM, and a working CPU. Wrote two programs in Hack assembly and a Hack-to-binary assembler.

### Boot.dev

_2025 - 2026 | Online_

_Courses_: Memory Management in C, Data Structures & Algorithms, Object-Oriented Programming, Functional Programming, HTTP Clients, Go, SQL, and Python.

_Projects_: an RSS feed aggregator and a Pokedex CLI (PokeAPI) in Go; and a Static Site Generator, Maze Solver, and an AI Agent (Google Gemini API) in Python.

## Technical Skills

**Languages & Tools:** C++, Rust, Python, Go, Haskell, Magik, Git

