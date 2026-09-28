Installing NumPy
-We know that it is a python library.
HOW TO INSTALL NumPy:
1. We initialize our current working file using : "uv init"
-This creates a file which stores information about our project and dependencies.
- In the file we have "dependencies = []" this means no external python package has been listed as dependency
-It is all under (project.toml())

2. We install NumPy.
-We will use :"uv add NumPy" since it tells the project that NumPy is a dependency,uv then:
 -> creates the project env
  ->resolves the appropriate package version
  ->install NumPy
  ->record the dependency in the pyproject.toml
  ->create /update uv/lock: it stores resolved versions of our dependencies. When other people clone our projects, this file will be used to get the exact versions of our libraries.
  - This then is added as an external python dependency

3. We run python : "uv run python" ->run python using the projects env
4. We import NumPy into our code in a new/already made file. Happy Hacking!


