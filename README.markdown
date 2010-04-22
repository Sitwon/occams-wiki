# Occam's Wiki
## Designing a Unix-style Wiki framework

### Description
Occam's Wiki is a project to develop a simple but extensible Wiki framework. The code here is intended to serve as the reference implementation of that framework.

### Structure
* `wiki.py` - This is the Conductor component. The entry-point to the whole system.
* `auth/` - The authentication-related component(s)
* `backend/` - The storage/retrieval-related component(s)
* `input/` - The input-related component(s)
* `output/` - The output-related components
	* `output/render` - The rendering component(s)
	* `output/decorate` - The output decorating component(s)
